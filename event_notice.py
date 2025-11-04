 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import random
import gmail
import yagmail
from pathlib import Path

GMAIL_USERNAME = '[REDACTED]'
GMAIL_PASSWORD = '[REDACTED]'

RECIPIENT1_EMAIL = '[REDACTED]'
RECIPIENT2_EMAIL  = '[REDACTED]'
RECIPIENT3_EMAIL  = '[REDACTED]'

REASONS = [] //fill it

IMAGES_FOLDER = Path("/") //fill it
IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp"]

REASON = random.choice(REASONS)
EMAIL_BODY = f"Today is {REASON}..."
EMAIL_SUBJECT = "" // subject

yagmail.register(GMAIL_USERNAME, GMAIL_PASSWORD)

def get_random_image():

    images = [f for f in IMAGES_FOLDER.iterdir() if f.suffix.lower() in IMAGE_EXTENSIONS]
    
    return random.choice(images)

def send_email(title: str):

    yag = yagmail.SMTP(GMAIL_USERNAME, GMAIL_PASSWORD)
    
    recipients = [RECIPIENT1_EMAIL,RECIPIENT2_EMAIL,RECIPIENT3_EMAIL]
    
    random_image = get_random_image()
    
    contents = [EMAIL_BODY]
    
    if random_image:
        contents.append(str(random_image))
    
    headers = {
        "X-Priority": "1",
        "X-MSMail-Priority": "High",
        "Importance": "High"
    }
    
    yag.send(
        to=recipients,
        subject=title,
        contents=contents,
        headers=headers
    )

if __name__ == "__main__":
    send_email(EMAIL_SUBJECT)
