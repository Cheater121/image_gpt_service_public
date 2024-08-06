import uvicorn  # noqa
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.routers import all_routers


app = FastAPI()

for router in all_routers:
    app.include_router(router)

allowed_headers = [
    "Content-Type",
    "Set-Cookie",
    "Access-Control-Allow-Headers",
    "Access-Control-Allow-Origin",
    "Authorization",
    "X-os-type",
    "X-current-version",
    "X-localization",
    "X-jwt-token",
    "X-secret-code",
    "X-subscribed",
    "X-store",
    "Host",
    "X-Real-IP",
    "X-Forwarded-For",
    "Accept",
    "Accept-Language",
    "Content-Language",
]

allowed_methods = ["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"]

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=allowed_methods,
    allow_headers=allowed_headers,
)


@app.get("/")
def read_root():
    return {"message": "Welcome!"}


# if __name__ == "__main__":
#     uvicorn.run(app="main:app", port=8080)
