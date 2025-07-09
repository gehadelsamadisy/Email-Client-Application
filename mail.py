import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox
from plyer import notification

def send_mail(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.send_message(msg)
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

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

def create_gui():
    def on_send():
        send_mail(
            sender_email_entry.get(),
            password_entry.get(),
            recipient_email_entry.get(),
            subject_entry.get(),
            body_entry.get("1.0", tk.END)
        )

    def on_receive():
        receive_mail(
            sender_email_entry.get(),
            password_entry.get()
        )

    root = tk.Tk()
    root.title("Email Client")

    tk.Label(root, text="Sender Email:").grid(row=0, column=0)
    sender_email_entry = tk.Entry(root, width=50)
    sender_email_entry.grid(row=0, column=1)

    tk.Label(root, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(root, show='*', width=50)
    password_entry.grid(row=1, column=1)

    tk.Label(root, text="Recipient Email:").grid(row=2, column=0)
    recipient_email_entry = tk.Entry(root, width=50)
    recipient_email_entry.grid(row=2, column=1)

    tk.Label(root, text="Subject:").grid(row=3, column=0)
    subject_entry = tk.Entry(root, width=50)
    subject_entry.grid(row=3, column=1)

    tk.Label(root, text="Body:").grid(row=4, column=0)
    body_entry = tk.Text(root, height=10, width=50)
    body_entry.grid(row=4, column=1)

    send_button = tk.Button(root, text="Send Email", command=on_send)
    send_button.grid(row=5, column=0, pady=10)

    receive_button = tk.Button(root, text="Receive Email", command=on_receive)
    receive_button.grid(row=5, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()