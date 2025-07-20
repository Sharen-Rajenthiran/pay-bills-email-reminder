import smtplib
from email.message import EmailMessage
from config import settings
import logging_config
import logging
import os

LOG = logging.getLogger(os.path.basename(__file__))

SENDER = settings.SENDER
PASSWORD = settings.PASSWORD

def send_message(
        email_message: EmailMessage
) -> None:
    """Sends an EmailMessage using Gmail SMTP to receiver"""
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.send_message(email_message)
    except Exception as e:
        LOG.error(f"Error sending email {e}", exc_info=True)
        raise
