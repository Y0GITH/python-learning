# Scan emails to block unsafe data from entering your system
emails = [
    'data@gamil.com',
    'baraa@outlook.de',
    'DROP TABLE USER;',
    'maria@gmail.com'
]
for email in emails:
    if ';' in email:
        print(f'SQL Injection : Hacker Attack')
        break
    print(f'Processing Email : {email}')