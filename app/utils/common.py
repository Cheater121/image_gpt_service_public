import base64

from app.logs.loggers import logger


def decode_base64_json_image(base64_json: str) -> bytes:
    logger.info("starting decode_base64_json_image")
    return base64.b64decode(base64_json)
