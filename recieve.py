import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox
from plyer import notification
def receive_mail(email_user, email_pass):
    try:
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL('imap.mail.tm')
        mail.login(email_user, email_pass)
        mail.select('inbox')

        # Search for the latest email
        result, data = mail.search(None, 'ALL')
        mail_ids = data[0].split()
        latest_email_id = mail_ids[-1]

        # Fetch the email
        result, data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Get the email body
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    email_body = part.get_payload(decode=True).decode()
                    break
        else:
            email_body = msg.get_payload(decode=True).decode()

        # Show the email body in a message box
        messagebox.showinfo("Latest Email", email_body)
        notification.notify(
            title='New Email',
            message=email_body,
            timeout=10
        )
        mail.logout()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to receive email: {e}")