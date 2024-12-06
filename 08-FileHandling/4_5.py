import re

file_name = "email.txt"
pattern_sender = r'^From:\s*([^<>\s]+@[^<>\s]+)'
recipient_pattern = r'^To:\s*([^<>\s]+@[^<>\s]+)'
subject_pattern = r'^Subject:\s*(.+)$'
body_pattern = r'\n\n(.*)'

with open(file_name, "r") as file:
    email_content = file.read()

# Extract sender
sender_match = re.search(pattern_sender, email_content, re.MULTILINE)
if sender_match:
    sender_email = sender_match.group(1)  # Get the matched email address
    print("Sender Email Address:", sender_email)
else:
    print("Sender Email Address: Not found")

# If you want to extract and print recipient, subject, and body, you can do so as well:
# Extract recipient
recipient_match = re.search(recipient_pattern, email_content, re.MULTILINE)
if recipient_match:
    recipient_email = recipient_match.group(1)
    print("Recipient Email Address:", recipient_email)
else:
    print("Recipient Email Address: Not found")

# Extract subject
subject_match = re.search(subject_pattern, email_content, re.MULTILINE)
if subject_match:
    subject = subject_match.group(1)
    print("Email Subject:", subject)
else:
    print("Email Subject: Not found")

# Extract body
body_match = re.search(body_pattern, email_content, re.DOTALL)
if body_match:
    body = body_match.group(1).strip()  # Strip leading/trailing whitespace
    print("Email Body:", body)
else:
    print("Email Body: Not found")