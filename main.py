file = open("emails.txt", "r")
emails = file.read().split("\n")
for email in emails:
    username = email.split("@")[0]
    print(f"{email} is: {username}")