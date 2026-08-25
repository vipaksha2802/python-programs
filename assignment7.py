import re

def find_emails(text):
    # Regular expression pattern for email addresses
    pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}'

    # Find all email addresses
    emails = re.findall(pattern, text)

    return emails


# Main program
text = input("Enter a text containing email addresses: ")

result = find_emails(text)

print("Email addresses found:")
for email in result:
    print(email)