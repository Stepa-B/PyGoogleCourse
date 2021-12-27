import re
import csv
old_domain, new_domain = r"abc.edu", r"xyz.edu"
f = open("user_emails2.csv","w")
f.close()
with open("user_emails.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    newlist=[]
    for row in csv_reader:
        email=row[1].strip()
        if re.match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
            new_email_address = re.sub(old_domain,new_domain,email)
            #print(new_email_address)
            with open("user_emails2.csv", "a") as file:
                file.write(row[0]+ ","+ new_email_address +"\n")
        else:
            with open("user_emails2.csv", "a") as file:
                file.write(row[0]+ ","+ row[1] +"\n")