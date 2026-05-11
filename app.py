from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

from email_sender import send_email


app = FastAPI(
    title="Email Automation System"
)

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EmailRequest(BaseModel):

    to_email: EmailStr
    subject: str
    body: str


@app.get("/")
def home():

    return {
        "project": "Email Automation System",
        "status": "running"
    }


@app.post("/send-email")
async def send_email_api(data: EmailRequest):

    await send_email(
        data.to_email,
        data.subject,
        data.body
    )

    return {
        "message": "Email Sent Successfully"
    }