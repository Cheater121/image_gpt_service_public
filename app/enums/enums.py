from enum import Enum


class ChatModels(Enum):
    dalle3 = "dall-e-3"
    dalle2 = "dall-e-2"


class ImageSize(Enum):
    extra_low = "256x256"
    low = "512x512"
    medium = "1024x1024"
    portrait = "1024x1792"
    landscape = "1792x1024"


class ImageQuality(Enum):
    standard = "standard"
    hd = "hd"
