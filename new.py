import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox
from plyer import notification


def send_email(sender_email, sender_pass , reciever_email, subject, body):
    try:
        # try to setup connection with smtp server
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(sender_email, sender_pass)
        server.sendmail(sender_email, reciever_email, f"Subject: {subject}\n\n{body}")
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")
        
     
     
    
        
def receive_email(email_user, email_pass):
    try:
        mail = imaplib.IMAP4_SSL('outlook.office365.com')
        mail.login(email_user, email_pass)
        mail.select('inbox')
        
        result, data = mail.search(None, 'ALL')
        mail_ids = data[0].split()
        latest_email_id = mail_ids[-1]
        
        result, data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    email_body = part.get_payload(decode=True).decode()
                    break
        else:
            email_body = msg.get_payload(decode=True).decode()
            
        messagebox.showinfo("Latest Email", email_body)
        notification.notify(
            title='New Email',
            message=email_body
        )
    except Exception as e:
        messagebox.showerror("Error", f"Failed to receive email: {e}")
        
        
        


def create_gui():
    def on_send():
        send_email(
            sender_email_entry.get(),
            password_entry.get(),
            recipient_email_entry.get(),
            subject_entry.get(),
            body_entry.get("1.0", tk.END)
        )

    def on_receive():
        receive_email(
            sender_email_entry.get(),
            password_entry.get()
        )

    # Create the main window
    root = tk.Tk()
    root.title("Email Client")

    # Sender Email
    tk.Label(root, text="Sender Email:").grid(row=0, column=0, padx=10, pady=5)
    sender_email_entry = tk.Entry(root, width=50)
    sender_email_entry.grid(row=0, column=1, padx=10, pady=5)

    # Password
    tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(root, show='*', width=50)
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    # Recipient Email
    tk.Label(root, text="Recipient Email:").grid(row=2, column=0, padx=10, pady=5)
    recipient_email_entry = tk.Entry(root, width=50)
    recipient_email_entry.grid(row=2, column=1, padx=10, pady=5)

    # Subject
    tk.Label(root, text="Subject:").grid(row=3, column=0, padx=10, pady=5)
    subject_entry = tk.Entry(root, width=50)
    subject_entry.grid(row=3, column=1, padx=10, pady=5)

    # Body
    tk.Label(root, text="Body:").grid(row=4, column=0, padx=10, pady=5)
    body_entry = tk.Text(root, height=10, width=50)
    body_entry.grid(row=4, column=1, padx=10, pady=5)

    # Send Button
    send_button = tk.Button(root, text="Send Email", command=on_send)
    send_button.grid(row=5, column=0, padx=10, pady=10)

    # Receive Button
    receive_button = tk.Button(root, text="Receive Email", command=on_receive)
    receive_button.grid(row=5, column=1, padx=10, pady=10)

    # Run the GUI
    root.mainloop()


if __name__ == "__main__":
    create_gui()