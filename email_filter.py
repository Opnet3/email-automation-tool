import imaplib
import email

print("Checking emails...")

try:
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login("teman.walston@gmail.com", "qpmv qpzg pwje wdqa")
    print("Login successful")
except Exception as e:
    print("Login failed:", e)
    exit()

mail.select("inbox")

status, messages = mail.search(None, '(SINCE "01-Sep-2026")')

email_list = messages[0].split()
print("Total messages found:", len(email_list))

for num in email_list:
    _, data = mail.fetch(num, "(RFC822)")
    msg = email.message_from_bytes(data[0][1])

    subject = msg["subject"]

    if subject and "job" in subject.lower():
        print("Job email:", subject)