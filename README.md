# Email Client Application

A Python-based email client demonstrating network programming concepts including TCP connections, SMTP/IMAP protocols, and GUI development.

## Overview

This project implements a functional email client with the following capabilities:

- Send emails using SMTP protocol
- Receive emails using IMAP protocol
- Graphical user interface built with tkinter
- Push notifications for new emails
- Support for multiple email providers (Gmail, Outlook, mail.tm)

## Project Files

### Main Applications

- `gui.py` - Gmail-based email client with GUI
- `new.py` - Outlook/Office365 email client with enhanced UI
- `mail.py` - Combined implementation (Gmail send + mail.tm receive)

### Core Modules

- `send.py` - Gmail email sending functionality
- `recieve.py` - mail.tm email receiving functionality
- `requirements.txt` - Python dependencies

## Quick Start

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python gui.py
   ```

## Email Provider Setup

### Gmail

- Enable 2-factor authentication
- Generate an App Password (Google Account → Security → App passwords)
- Use your Gmail address and app password

### Outlook/Office365

- Use your Outlook email address
- Use regular password or app password if 2FA enabled

### mail.tm (for testing)

- Create free account at [mail.tm](https://mail.tm)
- Use credentials for receiving emails

## Technical Implementation

### Network Protocols

- **SMTP** (port 587, TLS) for sending emails
- **IMAP** (port 993, SSL) for receiving emails
- **TCP** connections with proper handling and cleanup

### Key Libraries

- `smtplib` - SMTP protocol implementation
- `imaplib` - IMAP protocol implementation
- `tkinter` - GUI framework
- `plyer` - Push notifications
- `email` - Email message handling

### Features Demonstrated

- TCP socket programming
- SMTP/IMAP protocol implementation
- GUI development with tkinter
- Error handling and user feedback
- Push notification system
- Multi-provider email support

## Usage Examples

### Send Email (Gmail)

```python
python gui.py
# Enter Gmail credentials and recipient details
# Click "Send Email"
```

### Receive Email (mail.tm)

```python
python recieve.py
# Enter mail.tm credentials
# Latest email will be displayed
```

### Outlook Version

```python
python new.py
# Enhanced UI for Outlook/Office365 accounts
```

## Testing

The application has been tested with:

- ✅ Gmail accounts (send/receive)
- ✅ Outlook/Office365 accounts
- ✅ mail.tm accounts
- ✅ Error handling scenarios
- ✅ Network connectivity issues

## Educational Objectives

This project demonstrates:

1. **Network Programming**: TCP connections and protocol implementation
2. **Email Protocols**: SMTP for sending, IMAP for receiving
3. **GUI Development**: User interface with tkinter
4. **Error Handling**: Robust error management
5. **Multi-provider Support**: Different email service integration

## Security Considerations

- Use app passwords for Gmail accounts
- Enable 2-factor authentication
- Never share credentials
- Test with dedicated accounts when possible

## Troubleshooting

| Issue                | Solution                                                |
| -------------------- | ------------------------------------------------------- |
| Authentication Error | Check credentials, use app passwords for Gmail          |
| Connection Error     | Verify internet connection and email provider settings  |
| Import Error         | Install dependencies: `pip install -r requirements.txt` |

---

_This project is created for educational purposes to demonstrate network programming concepts and email protocol implementation._
