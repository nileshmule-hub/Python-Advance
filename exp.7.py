import re

text = """
Contact us at support@example.com or admin@test.org.
You can also email student123@university.edu.
gfsifjgeifghbefrkdgdoejheydsbakdpmxbvkhgdjd
"""

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)