import csv
import datetime
from time import strptime, time
from email_validator import EmailNotValidError,validate_email
import random

def pcusage():
        pctypes = ["PC1","PC2","PC3","PC4","PC5","PC6"]
        select = random.choice(pctypes)
        u_name = input("Enter UserName:")
        u_email = input("Enter Email Adress:")
        def email():
            try:
                valid = validate_email(u_email)
                email = valid.email
            except EmailNotValidError as e:
                print(str(e))

        validate_email(u_email)
        pcused = str(select)
        timepanel = datetime.datetime.now()
        hour = timepanel.strftime("%x")
        day = timepanel.strftime("%X")
        hour1 = random.randrange(1,12)
        min = random.randrange(0,60)
        s = []
        s.append(min)
        sdash = "".join(map(str,s))
        so = sdash.zfill(2)
        s.append(so)
        s.remove(min)
        du = random.randint(0,60)
        hour2 = (hour1+(min+du)//60)%24
        min2 = (min+du)%60
        z = []
        z.append(min2)
        zdash = "".join(map(str,z))
        zo = zdash.zfill(2)
        z.append(zo)
        z.remove(min2)
        hour2which = timepanel.strftime("%p")
        print("Started using at:",str(hour1),":",str(min),str(hour2which))
        print("Finished Using at:",str(hour2),":",str(min2),str(hour2which))
        def convert_tup(tuple):
            str = "".join(tuple)
            return str
        du1 = (str(hour1),":",str(min),str(hour2which))
        du2 = (str(hour2),":",str(min2),str(hour2which))
        dut1 = convert_tup(du1)
        dut2 = convert_tup(du2)
        def hourtominute():
            x_ = hour2 - hour1
            y_ = min2 - min
            hm = (x_*60)+y_
            return hm
        htm = hourtominute()
        usagecharge = round(htm*0.41,2)



        global total_charge
        global pcharge
        printer = ["PR1","PR2","PR3"]
        printsel = random.choice(printer)
        selector = ["y","n"]
        autoselector = random.choice(selector)
        pcharge = 0
        if autoselector == "y":
            print("You've used printer",printsel)
            colored = 50
            noncolored = 20
            setrange = range(1,11)
            numpaper = random.choice(setrange)
            selector1 = ["y","n"]
            colornot = random.choice(selector1)
            if colornot == "y":
                pcharge = numpaper*colored
            else:
                pcharge = numpaper*noncolored
        else:
            pass
        total_charge = usagecharge + pcharge



        neededlist = [u_name,u_email,pcused,hour,day,dut1,dut2,htm,usagecharge,pcharge,total_charge]
        print(neededlist)

        billing = open("billing.csv","w",newline="")
        bw = csv.writer(billing)
        tophead = ["NAME","EMAILID","PC USED","DATE","LOGIN TIME","STARTING TIME","ENDING TIME","MINUTES USED","CHARGE/HOUR","PRINTING CHARGE","TOTAL:(in Rs.)"]
        bw.writerow(tophead)
        bw.writerow(neededlist)
        billing.close()
        from ccmspackage.subpackage import addforcafeai
        addforcafeai.addforcafe()
