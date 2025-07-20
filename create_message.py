from config import settings
from datetime import datetime
from email.message import EmailMessage 

SENDER = settings.SENDER
RECEIVER = settings.RECEIVER

NAME_LINKS = {
    "GE": settings.GE
}

current_month = datetime.now().strftime("%B %Y")

# Get the Month and Year fir Subject
SUBJECT = f"Automated Pay Your Bill Reminder: {current_month}"
BODY = f"""Hey,

Here are the bills you need to pay for this period {current_month}:

1. Insurance: RM X (before 13th of every month)
   Pay it here: {NAME_LINKS.get("GE")}

2. Neflix: RM Z (before 31st of every month)
   Pay it here: AUTODEBIT

3. Top up: RM Y (before 7th of every month)
   Pay it here: Hotlink App

Best,
You   
"""

def create_message(
        sender: str = SENDER,
        receiver: str = RECEIVER,
        subject: str = SUBJECT,
        body: str = BODY,
) -> EmailMessage:
    """Creates an EmailMessage to be sent"""
    
    message = EmailMessage()

    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    message.set_content(body)

    return message
    
