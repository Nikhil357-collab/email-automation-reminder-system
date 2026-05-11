from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column

from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import Text


metadata = MetaData()
email_history = Table(
    "email_history",
    metadata,

    Column("id", String, primary_key=True),
    Column("to_email", String),
    Column("subject", String),
    Column("status", String),
    Column("sent_at", String)
)
#-------------------------
contacts = Table(
    "contacts",
    metadata,

    Column("id", String, primary_key=True),
    Column("name", String),
    Column("email", String),
)

templates = Table(
    "templates",
    metadata,

    Column("id", String, primary_key=True),
    Column("name", String),
    Column("subject", Text),
    Column("body_md", Text),
)

campaigns = Table(
    "campaigns",
    metadata,

    Column("id", String, primary_key=True),
    Column("name", String),
    Column("template_id", String),
    Column("sender_name", String),
    Column("sender_email", String),
)

reminders = Table(
    "reminders",
    metadata,

    Column("id", String, primary_key=True),
    Column("title", String),
    Column("contact_id", String),
    Column("campaign_id", String),
    Column("start_at_utc", DateTime),
    Column("active", Boolean),
)

messages = Table(
    "messages",
    metadata,

    Column("id", String, primary_key=True),
    Column("campaign_id", String),
    Column("contact_id", String),
    Column("scheduled_at_utc", DateTime),
    Column("status", String),
    Column("sent_at_utc", DateTime),
    Column("provider_msg_id", String),
    Column("body_rendered_html", Text),
)
print("Models Loaded")
