domains = ['www.google.com',
           'openai.com',
           'localhoct',
           'WWW.DATAWITHBARAA.COM']
cleaned = [domain.lower().replace('www.','') 
           for domain in domains
           if '.' in domain ]
print(cleaned)
cleaned = [ d.lower().replace('www.','') for d in domains if '.' in d]
print(cleaned)