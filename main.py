from create_message import create_message
from send_message import send_message
import logging_config
import logging
import os

LOG = logging.getLogger(os.path.basename(__file__))

if __name__ == "__main__":
    try:
        created_message = create_message()
        LOG.info("message created") 
        send_message(created_message)
        LOG.info("message sucessfully sent!")
    except Exception as e:
        LOG.error("Error sending message {e}")


