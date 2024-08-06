import uuid

from fastapi import APIRouter, HTTPException
from openai import OpenAIError
from starlette import status

from app.core.config import settings
from app.enums.enums import ChatModels, ImageQuality, ImageSize
from app.logs.loggers import logger
from app.services.openai_image_generator import generate_image_openai
from app.services.s3client import s3_client
from app.utils.common import decode_base64_json_image


router = APIRouter(
    prefix="/images",
    tags=["Images"],
)


@router.post("/create_image/")
async def create_image(prompt: str, model: ChatModels, size: ImageSize, quality: ImageQuality):
    logger.info(f"Starting to create image for prompt {prompt}")
    if model == ChatModels.dalle3 or model == ChatModels.dalle2:
        try:
            base64_json = await generate_image_openai(prompt=prompt, model=model, size=size, quality=quality)
        except OpenAIError as e:
            logger.error(f"Error generating image for prompt {prompt}: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error generating image: {e}"
            ) from e

        binary_file = decode_base64_json_image(base64_json)
        filename = f"{uuid.uuid4()}.jpeg"

        await s3_client.upload_file(filename=filename, file=binary_file)

        image_s3_url = settings.S3_ENDPOINT_URL + "/" + settings.S3_BUCKET_NAME + "/" + filename
        logger.info(f"Image created and uploaded to S3: {image_s3_url}")
        return {"url": image_s3_url}
