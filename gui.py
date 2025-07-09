import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox
from plyer import notification
from send import send_mail
from recieve import receive_mail

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