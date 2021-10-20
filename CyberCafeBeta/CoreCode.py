from ccmspackage.cafemanagement import pcusage
import ccmspackage.adduser
import ccmspackage.userinit
import ccmspackage.removeuser

ccmspackage.userinit.Userinit()

#ADD A USER
ask = input("Would you like to add a user? (y/n)")
if ask == "y":
    ccmspackage.adduser.Add_User()
elif ask == "N":
    x = 0
else:
    pass

ask2 = input("Would you like to remove a user from the entered data? (y/n)")
if ask2 == "y":
    ccmspackage.removeuser.kick_user()
elif ask2 == "n":
    pass

print("Welcome to the cafe management section!")
for i in range(30):
    print("*",end="")

#FUNCTION FOR CAFE RELATED MANAGEMENT
print("\n")
pcusage()

#Written by: Ammar Bin Hashim
