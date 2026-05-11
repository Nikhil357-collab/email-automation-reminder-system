import asyncio
import os
import email.utils

from dotenv import load_dotenv
import aiosmtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()


async def send_email(
    to_email,
    subject,
    body
):

    msg = MIMEMultipart()

    msg["From"] = email.utils.formataddr(
        ("Automation System", os.getenv("SMTP_USER"))
    )

    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "html"))

    try:

        smtp = aiosmtplib.SMTP(
            hostname=os.getenv("SMTP_HOST"),
            port=int(os.getenv("SMTP_PORT")),
            use_tls=True
        )

        await smtp.connect()

        await smtp.login(
            os.getenv("SMTP_USER"),
            os.getenv("SMTP_PASS")
        )

        await smtp.send_message(msg)

        await smtp.quit()

        print(f"✅ Email sent to {to_email}")

    except Exception as e:

        print("❌ Error:", e)


if __name__ == "__main__":

    asyncio.run(
        send_email(
            os.getenv("SMTP_USER"),
            "Portfolio Project Test",
            "<h2>Email Automation Working</h2>"
            f"<p>Hello {os.getenv('COMPANY_UNIVERSITY')},</p>"

            "This is an automated reminder regarding:"

            f"<p>{os.getenv('SUBJECT')}</p>"

            "Please take the necessary action."

            "Regards,"
            "Automation Team"
            "<p>Regards, NB <br>AI Automation System</p>"
            "<p>Thank you.</p>"
        )
    )