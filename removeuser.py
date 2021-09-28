import csv
import os

def kick_user():
    with open("userdetails.csv","r+") as f:
        lines = f.readlines()
        f.seek(0)

        sname = input("Enter a name to remove:")
        for l in lines:
            if not sname in l.split(",")[0]:
                f.write(l)
        f.truncate()