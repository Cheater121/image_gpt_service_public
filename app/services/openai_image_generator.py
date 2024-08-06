from openai import OpenAI

from app.core.config import settings
from app.enums.enums import ChatModels, ImageQuality, ImageSize
from app.logs.loggers import logger


api_key = settings.OPEN_AI_API_KEY

client = OpenAI(api_key=api_key)


async def generate_image_openai(
    model: ChatModels,
    prompt: str,
    size: ImageSize,
    quality: ImageQuality,
) -> str:
    logger.info(f"Generating image for prompt {prompt}")
    response = client.images.generate(
        model=model.value, prompt=prompt, size=size.value, quality=quality.value, n=1, response_format="b64_json"
    )

    return response.data[0].b64_json
