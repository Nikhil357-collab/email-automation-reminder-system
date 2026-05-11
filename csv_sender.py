import pandas as pd
import asyncio

from email_sender import send_email


contacts = pd.read_csv("Email_Automation_System\\data\\contacts.csv")

reminders = pd.read_csv("Email_Automation_System\\data\\reminders.csv")


async def main():

    tasks = []

    subject = reminders.loc[0, "subject"] ##column name
    template = reminders.loc[0, "message"]

    for _, row in contacts.iterrows():

        name = row["name"]
        email = row["email"]

        personalized_message = template.replace(
            "{{name}}",
            name
        )

        tasks.append(

            send_email(
                email,
                subject,
                f"<h2>{personalized_message}</h2>"
            )

        )

    await asyncio.gather(*tasks)

    print("✅ All Reminder Emails Sent")


asyncio.run(main())