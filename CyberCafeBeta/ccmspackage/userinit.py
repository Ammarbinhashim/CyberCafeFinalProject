import csv
from email_validator import validate_email, EmailNotValidError

def Userinit():
    try:
        writefile = open("userdetails.csv","r")
        print("File Exist")
        writefile.close()
        pass
    except IOError:
        print("File Doesn't Exist")
        writefile = open("userdetails.csv","w",newline="")
        tophead = ["NAME","AGE","EMAIL","PHONE No:"]
        addrow = csv.writer(writefile)
        addrow.writerow(tophead)
        writefile.close()
    u_name = input("Enter UserName:")
    u_age = input("Enter Age:")
    u_email = input("Enter Email Adress:")
    def email():
        try:
            valid = validate_email(u_email)
            email = valid.email
        except EmailNotValidError as e:
            print(str(e))

    validate_email(u_email)
    u_phone = input("Enter Phone Number:")
    pt1 = tuple(u_phone)
    if len(pt1) != 10:
        print("Error: Please enter the right number")
        u_phone = input("Enter Phone Number:")
    writefile = open("userdetails.csv","w",newline="")
    tophead = ["NAME","AGE","EMAIL","PHONE No:"]
    addrow = csv.writer(writefile)
    addrow.writerow(tophead)
    addrow.writerow([u_name,u_age,u_email,u_phone])
    writefile.close()
