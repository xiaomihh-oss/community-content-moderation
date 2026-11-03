
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.moderation import moderate_content

app = FastAPI(
    title="Community Content Moderation",
    description="A lightweight content moderation system",
    version="1.0.0"
)


class ContentRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=5000
    )


@app.get("/")
def home():
    return {
        "message": "Content Moderation API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/moderate")
def moderate(request: ContentRequest):

    text = request.text.strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Content cannot be empty"
        )

    return moderate_content(text)
