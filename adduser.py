import csv
import os
from email_validator import validate_email, EmailNotValidError

def Add_User():
    x = int(input("Enter number of Users to be added:"))
    for i in range(0,x):
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
            writefile = open("userdetails.csv","a",newline="")
            tophead = ["NAME","AGE","EMAIL","PHONE No:"]
            addrow = csv.writer(writefile)
            writefile.close()

        with open("userdetails.csv","a",newline="") as writefile:
            writerow  = csv.writer(writefile)
            writerow.writerow([u_name,u_age,u_email,u_phone])
            writefile.close()
    return
