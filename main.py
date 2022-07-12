import json
from pathlib import Path
import random
import string
from time import sleep



class Project:
    __data=[]
    __database="file.json"

    try:
        if not Path(__database).exists():
            with open(__database,'w') as fw:
                fw.write(json.dumps(__data))
        else:
            with open(__database,'r') as fr:
                __info=json.loads(fr.read())
    except Exception as err:
        print("ERROR ",err)


    def __getid(self):
        try:
            A=(random.choices(string.ascii_letters, k=3))
            B=(random.choices(string.digits, k=3))
            C=(random.choices(list("@#$*"), k=2))

            D=A+B+C

            random.shuffle(D)
            return ("".join(D))

        except Exception as err:
            print("WRONG INPUT", err)

    def rem(self):
        try:
            with open(Project.__database) as FR:
                P = json.loads(FR.read())

            n1 = input("ENTER ID to DELETE : ").strip()
            B = []
            O=False
            for i in P:
                if i["ID"] == n1:
                    B.append(i)
                    O=True
            for i in B:
                P.remove(i)
            while O:
                with open(Project.__database, 'w') as u:
                    u.write(json.dumps(P))
                return " DELETED "

            return "NO ID MATCH"

        except Exception as err:
            print("ERROR ",err)
    def develop(self):
        try:
            data={}
            while True:

                data["ID"] = self.__getid()
                data["NAME"] = input("Enter Name: ").strip()
                data["STATUS"] = input("Enter Status STUDENT OR TEACHER: ").upper()
                if data["STATUS"]=="TEACHER" or data["STATUS"]=="STUDENT":
                    pass
                else:
                    return "WRONG INPUT"
                    break

                try:
                    d=int(input("Enter 10 digits Contact number: ").strip())
                    if len(str(d))==10:
                        data["CONTACT"] =d
                    else:
                        print()
                        return ("DOO NOT FULLFILL CRITERIA")
                        break
                except Exception as err:
                    print()
                    print ("ERROR >>")
                    return err
                    break
                Project.__data.append(data)
                with open(Project.__database,'w') as f:
                    f.write(json.dumps(Project.__data))
                print()
                return (f"{data['NAME']} with ID {data['ID']} and Status {data['STATUS']} REGISTERED.")
        except Exception as err:
            print("ERROR ", err)
    def R_A(self):
        try:
            with open(Project.__database) as fr:
                T = json.loads(fr.read())

            password = input("enter password :").upper().strip()
            if password == "STUDENT":
                return (T)
            else:
                return "NO ACCESS"
        except Exception as err:
            print("ERROR ", err)
    def __str__(self):
        return "BHAG JA"
    def read(self):
        try:
            with open(Project.__database) as fw:
                x = json.loads(fw.read())

            value = input("Enter ID : ").strip()
            for i in x:
                if i["ID"] == value:
                    return (i)
            else:
                return "NOT FOUND"
        except Exception as err:
            print("ERROR", err)
    def changes(self):
        try:
            with open(Project.__database) as D:
                G = json.loads(D.read())
            en = input("Enter id to update: ").strip()
            x = False
            for i in G:
                if i["ID"] == en:
                    print(i)
                    l = i
                    G.remove(i)
                    x=True
            while x==True:
                print("what do you want to update: ")
                print("1. Name")
                print("2. Status")
                print("3. Contact")
                INP = int(input("enter your choice: ").strip())
                if INP == 1:
                    name = input("Enter new name to update: ").strip()
                    l["NAME"] = name
                    G.append(l)

                elif INP == 2:

                    Status = input("enter NEW STATUS: ").upper().strip()
                    if Status == "TEACHER" or Status == "STUDENT":
                        l["STATUS"] = Status
                        G.append(l)
                    else:
                        return "ERROR >> INPUT DO NOT FULLFILl CRITERIA"

                elif INP== 3:
                    try:
                        num = int(input("Enter new contact number: ").strip())
                        if len(str(num)) == 10:
                            l["CONTACT"] = num
                            G.append(l)
                        else:
                            G.append(l)
                            print("INVALID INPUT")
                    except Exception as err:
                        G.append(l)
                        print("ERROR ", err)
                else:
                    G.append(l)
                with open(Project.__database, 'w') as B:
                    B.write(json.dumps(G))
                return "Status updated"
            return "INVALID ID"
        except Exception as err:
            print("ERROR ", err)

STAR=Project()

while(True):
    print()
    print("1. ADD Student/teacher")
    print("2. Read Single.")
    print("3. Update student/teacher.")
    print("4. Delete student/teacher.")
    print("5. Read all Teacher/Student.")
    print("0. EXIT")
    try:
        X= int(input("Enter your choice: "))
        if X == 1:
            print(STAR.develop())
        elif X == 2:
            print(STAR.read())
        elif X == 3:
            print(STAR.changes())
        elif X == 4:
            print(STAR.rem())
        elif X == 5:
            print(STAR.R_A())
        elif X == 0:
            print("HELLO WORLD",end="")
            for i in range(3):
                sleep(1)
                print(".",end="")
            break

        else:
            print("RE-ENTER YOUR CHOICE")
    except Exception as err:
        print("ERROR ",err)















