# Database Connection
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client['Students_2018']

collection1  = db["CSE"]

collection2 = db["EEE"]

collection3  = db["CE"]

collection4 = db["ME"]

db1 = client["admin_Id_Pass"]

collection5 = db1["admin"]


# Display 

print('--------------------------------------------')
print('********************************************')
print("   WELCOME TO STUDENTS MANAGEMENT SYSTEM    ")
print('********************************************')


print('--------------------------------------------')
print("1. Press 1 Admin \n2. Press 2 Student")
print('--------------------------------------------')


option = int(input("Enter the choose opton : "))
print('--------------------------------------------')

if option == 1:
    id = input("User ID : ")
    passw = input("Password : ")
    print('--------------------------------------------')

    flag1 = collection5.find_one({"_id": {"$eq" : id}})
    flag2 = collection5.find_one({"password": {"$eq" : passw}})


    if (type(flag1) is dict) and (type(flag2) is dict):
        print("    User ID : {}             ".format(id))
        print('--------------------------------------------')
        print("1. Press 1 Showing all details of Students\n2. Press 2 Insert any Students Details\n3. Press 3 Update any specific Students Details\n4. Press 4 Delete any specific Students Details")
        print('--------------------------------------------')
        press = int(input("Choose the option : "))
        print('--------------------------------------------')

        if press == 1:
            print("1. CSE\n2. EEE\n3. CE\n4. ME")
            print('--------------------------------------------')
            press1 = input("Which branch : ")
            press1 = press1.upper()
            print('--------------------------------------------')

            if press1 == "CSE":
                print("         ALL STUDENTS IN CSE BRANCH         ")
                print('--------------------------------------------')
                for item in  collection1.find({}):
                    print(item)
                print('----------------END---------------------')
            
            elif press1 == "EEE":
                print("         ALL STUDENTS IN EEE BRANCH         ")
                print('--------------------------------------------')
                for item in  collection2.find({}):
                    print(item)
                print('----------------END---------------------')

            elif press1 == "CE":
                print("         ALL STUDENTS IN CE BRANCH          ")
                print('--------------------------------------------')
                for item in  collection3.find({}):
                    print(item)
                print('----------------END---------------------')

            elif press1 == "ME":
                print("         ALL STUDENTS IN ME BRANCH          ")
                print('--------------------------------------------')
                for item in  collection4.find({}):
                    print(item)
                print('----------------END---------------------')

            else:
                print("Please enter correct Branch!!")
                print('----------------END---------------------')

        
        elif press == 2:
            reg_no = int(input("Enter Registration Number : "))
            name = input("Enter Name : ")
            roll_no = input("Enter Roll Number : ")
            branch = input("Enter Branch : ")
            print('--------------------------------------------')

            if branch == "CSE":
                collection1.insert_one({"_id" : reg_no, "name" : name, "roll_no": roll_no, "branch" : branch})

            elif branch == "EEE":
                collection2.insert_one({"_id" : reg_no, "name" : name, "roll_no": roll_no, "branch" : branch})

            elif branch == "CE":
                collection3.insert_one({"_id" : reg_no, "name" : name, "roll_no": roll_no, "branch" : branch})

            elif branch == "ME":
                collection4.insert_one({"_id" : reg_no, "name" : name, "roll_no": roll_no, "branch" : branch})

            print("Insert successful!!")
            print('----------------END---------------------')


        elif press == 3:
            print("1. Press 1 Name\n2. Press 2 Roll_no")
            print('--------------------------------------------')
            press3 = int(input("Enter option : "))
            print('--------------------------------------------')
            if press3 == 1:
                ident = input("Enter specific field to identify student : ")
                new_name = input("Enter New Name : ")
                print('--------------------------------------------')
                print("1. CSE\n2. EEE\n3. CE\n4. ME")
                print('--------------------------------------------')
                pressb = input("Which branch : ")
                print('--------------------------------------------')
                pressb = pressb.upper()
                f = True
                available1 = 0
                available2 = 0
                available3 = 0

                if pressb == "CSE":
                    available1 = collection1.find_one({"name" : ident})
                    if "18105" in ident:
                        available2 = collection1.find_one({"_id" : int(ident)})
                    available3 = collection1.find_one({"roll_no" : ident})
                    if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                        if "2k18" in ident:
                            collection1.update_many({"roll_no" :  ident},{"$set" : { "name" : new_name}})
                        elif "18105" in ident:
                            collection1.update_many({"_id" :  int(ident)},{"$set" : { "name" : new_name}})
                        else:
                            collection1.update_many({"name" :  ident},{"$set" : { "name" : new_name}})
                    else:
                        f = False
                
                elif pressb == "EEE":
                    available1 = collection2.find_one({"name" : ident})
                    if "18125" in ident:
                        available2 = collection2.find_one({"_id" : int(ident)})
                    available3 = collection2.find_one({"roll_no" : ident})
                    if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                        if "2k18" in ident:
                            collection2.update_many({"roll_no" :  ident},{"$set" : { "name" : new_name}})
                        elif "18125" in ident:
                            collection2.update_many({"_id" :  int(ident)},{"$set" : { "name" : new_name}})
                        else:
                            collection2.update_many({"name" :  ident},{"$set" : { "name" : new_name}})
                    else:
                        f = False

                if pressb == "CE":
                    available1 = collection3.find_one({"name" : ident})
                    if "18115" in ident:
                        available2 = collection3.find_one({"_id" : int(ident)})
                    available3 = collection3.find_one({"roll_no" : ident})
                    if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                        if "2k18" in ident:
                            collection3.update_many({"roll_no" :  ident},{"$set" : { "name" : new_name}})
                        elif "18115" in ident:
                            collection3.update_many({"_id" :  int(ident)},{"$set" : { "name" : new_name}})
                        else:
                            collection3.update_many({"name" :  ident},{"$set" : { "name" : new_name}})
                    else:
                        f = False

                if pressb == "ME":
                    available1 = collection4.find_one({"name" : ident})
                    if "18135" in ident:
                        available2 = collection4.find_one({"_id" : int(ident)})
                    available3 = collection4.find_one({"roll_no" : ident})
                    if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                        if "2k18" in ident:
                            collection4.update_many({"roll_no" :  ident},{"$set" : { "name" : new_name}})
                        elif "18135" in ident:
                            collection4.update_many({"_id" :  int(ident)},{"$set" : { "name" : new_name}})
                        else:
                            collection4.update_many({"name" :  ident},{"$set" : { "name" : new_name}})
                    else:
                        f = False
                if f:
                    print("               UPDATED!!                ")
                else:
                    print("        STUDENTS Not Available          ")
                print('--------------------------------------------')
                print('----------------END---------------------')

            elif press3 == 2:
                ident = input("Enter specific field to identify student : ")
                new_roll_no = input("Enter New Roll Number : ")
                print('--------------------------------------------')
                print("1. CSE\n2. EEE\n3. CE\n4. ME")
                print('--------------------------------------------')
                pressb = input("Which branch : ")
                print('--------------------------------------------')
                pressb = pressb.upper()
                f = True
                available1 = 0
                available2 = 0
                available3 = 0
                
                if pressb == "CSE":
                    available1 = collection1.find_one({"name" : ident})
                    if "18105" in ident:
                        available2 = collection1.find_one({"_id" : int(ident)})
                    available3 = collection1.find_one({"roll_no" : ident})
                    if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                        if "2k18" in ident:
                            collection1.update_many({"roll_no" :  ident},{"$set" : { "roll_no" : new_roll_no}})
                        elif "18105" in ident:
                            collection1.update_many({"_id" :  int(ident)},{"$set" : { "roll_no" : new_roll_no}})
                        else:
                            collection1.update_many({"name" :  ident},{"$set" : { "roll_no" : new_roll_no}})
                    else:
                        f = False
                
                elif pressb == "EEE":
                    available1 = collection2.find_one({"name" : ident})
                    if "18125" in ident:
                        available2 = collection2.find_one({"_id" : int(ident)})
                    available3 = collection2.find_one({"roll_no" : ident})
                    if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                        if "2k18" in ident:
                            collection2.update_many({"roll_no" :  ident},{"$set" : { "roll_no" : new_roll_no}})
                        elif "18125" in ident:
                            collection2.update_many({"_id" :  int(ident)},{"$set" : { "roll_no" : new_roll_no}})
                        else:
                            collection2.update_many({"name" :  ident},{"$set" : { "roll_no" : new_roll_no}})
                    else:
                        f = False

                if pressb == "CE":
                    available1 = collection3.find_one({"name" : ident})
                    if "18115" in ident:
                        available2 = collection3.find_one({"_id" : int(ident)})
                    available3 = collection3.find_one({"roll_no" : ident})
                    if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                        if "2k18" in ident:
                            collection3.update_many({"roll_no" :  ident},{"$set" : { "roll_no" : new_roll_no}})
                        elif "18115" in ident:
                            collection3.update_many({"_id" :  int(ident)},{"$set" : { "roll_no" : new_roll_no}})
                        else:
                            collection3.update_many({"name" :  ident},{"$set" : { "roll_no" : new_roll_no}})
                    else:
                        f = False

                if pressb == "ME":
                    available1 = collection4.find_one({"name" : ident})
                    if "18135" in ident:
                        available2 = collection4.find_one({"_id" : int(ident)})
                    available3 = collection4.find_one({"roll_no" : ident})
                    if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                        if "2k18" in ident:
                            collection4.update_many({"roll_no" :  ident},{"$set" : { "roll_no" : new_roll_no}})
                        elif "18135" in ident:
                            collection4.update_many({"_id" :  int(ident)},{"$set" : { "roll_no" : new_roll_no}})
                        else:
                            collection4.update_many({"name" :  ident},{"$set" : { "roll_no" : new_roll_no}})
                    else:
                        f = False
                if f:
                    print("               UPDATED!!                ")
                else:
                    print("         STUDENT Not Available          ")
                print('---------------------------------------')
                print('----------------END---------------------')

            


        elif press == 4:
            print("1. CSE\n2. EEE\n3. CE\n4. ME")
            print('--------------------------------------------')
            pressb = input("Which branch : ")
            print('--------------------------------------------')
            pressb = pressb.upper()
            ident = input("Enter specific field to identify student : ")
            print('--------------------------------------------')
            f = True
            available1 = 0
            available2 = 0
            available3 = 0

            if pressb == "CSE":
                available1 = collection1.find_one({"name" : ident})
                if "18105" in ident:
                    available2 = collection1.find_one({"_id" : int(ident)})
                available3 = collection1.find_one({"roll_no" : ident})
                if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                    if "CSE" in ident:
                        collection1.delete_one({"branch" :  ident})
                    elif "2k18" in ident:
                        collection1.delete_one({"roll_no" :  ident})
                    elif "18105" in ident:
                        collection1.delete_one({"_id" :  int(ident)})
                    else:
                        collection1.delete_one({"name" :  ident})
                else:
                    f = False

            elif pressb == "EEE":
                available1 = collection2.find_one({"name" : ident})
                if "18125" in ident:
                    available2 = collection2.find_one({"_id" : int(ident)})
                available3 = collection2.find_one({"roll_no" : ident})
                if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                    if "EEE" in ident:
                        collection2.delete_one({"branch" :  ident})
                    elif "2k18" in ident:
                        collection2.delete_one({"roll_no" :  ident})
                    elif "18125" in ident:
                        collection2.delete_one({"_id" :  int(ident)})
                    else:
                        collection2.delete_one({"name" :  ident})
                else:
                    f = False

            if pressb == "CE":
                available1 = collection3.find_one({"name" : ident})
                if "18115" in ident:
                    available2 = collection3.find_one({"_id" : int(ident)})
                available3 = collection3.find_one({"roll_no" : ident})
                if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                    if "CE" in ident:
                        collection3.delete_one({"branch" :  ident})
                    elif "2k18" in ident:
                        collection3.delete_one({"roll_no" :  ident})
                    elif "18115" in ident:
                        collection3.delete_one({"_id" :  int(ident)})
                    else:
                        collection3.delete_one({"name" :  ident})
                else:
                    f = False


            if pressb == "ME":
                available1 = collection4.find_one({"name" : ident})
                if "18135" in ident:
                    available2 = collection4.find_one({"_id" : int(ident)})
                available3 = collection4.find_one({"roll_no" : ident})
                if type(available1) is dict or type(available2) is dict or type(available3) is dict:
                    if "ME" in ident:
                        collection4.delete_one({"branch" :  ident})
                    elif "2k18" in ident:
                        collection4.delete_one({"roll_no" :  ident})
                    elif "18135" in ident:
                        collection4.delete_one({"_id" :  int(ident)})
                    else:
                        collection4.delete_one({"name" :  ident})
                else:
                    f = False
            if f:
                print("                DELETED!!               ")
            else:
                print("         STUDENT Not Available          ")
            print('----------------------------------------')
            print('----------------END---------------------')



        else:
            print("Please choose correct option")
            print('----------------END---------------------')






    elif (type(flag1) is dict) and (type(flag2) is not dict):
        print("Incorrect Password!!")
        print('----------------END---------------------')

    elif (type(flag1) is not dict) and (type(flag2) is dict):
        print("Incorrect User ID!!")
        print('----------------END---------------------')

    else:
        print("Incorrect User ID and Password!!")
        print('----------------END---------------------')


elif option == 2:
    print("1. Press CSE\n2. Press EEE\n3. Press CE\n4. Press ME ")
    print('--------------------------------------------')
    branch = input("Which Branch : ")
    print('--------------------------------------------')
    branch = branch.upper()
    if branch == "CSE":
        print("-------------WELCOME TO CSE--------------")
        print("-----------------------------------------")
        print("1. Press 1 Searching by Name\n2. Press 2 Searching by Registration Number\n3. Press 3 Searching by Roll Number")
        print("-----------------------------------------")
        search = int(input("Choose Option :  "))
        print("-----------------------------------------")
        if search == 1:
            name = input("Enter Name : ")
            print("-----------------------------------------")
            data = collection1.find_one({"name" : {"$eq" : name}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(name))
                print('----------------END---------------------')

        
        elif search == 2:
            reg_no = int(input("Enter Registration Number: "))
            print("-----------------------------------------")
            data = collection1.find_one({"_id" : {"$eq" : reg_no}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(reg_no))
                print('----------------END---------------------')
        
        elif search == 3:
            roll_no = input("Enter Roll Number : ")
            print("-----------------------------------------")
            data = collection1.find_one({"roll_no" : {"$eq" : roll_no}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(roll_no))
                print('----------------END---------------------')

        else:
            print("Please choose Correct option!!")
            print('----------------END---------------------')


    elif branch == "EEE":
        print("-------------WELCOME TO EEE--------------")
        print("-----------------------------------------")
        print("1. Press 1 Searching by Name\n2. Press 2 Searching by Registration Number\n3. Press 3 Searching by Roll Number")
        print("-----------------------------------------")
        search = int(input("Choose Option :  "))
        print("-----------------------------------------")
        if search == 1:
            name = input("Enter Name : ")
            print("-----------------------------------------")
            data = collection2.find_one({"name" : {"$eq" : name}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(name))
                print('----------------END---------------------')

        
        elif search == 2:
            reg_no = int(input("Enter Registration Number: "))
            print("-----------------------------------------")
            data = collection2.find_one({"_id" : {"$eq" : reg_no}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(reg_no))
                print('----------------END---------------------')
        
        elif search == 3:
            roll_no = input("Enter Roll Number : ")
            print("-----------------------------------------")
            data = collection2.find_one({"roll_no" : {"$eq" : roll_no}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(roll_no))
                print('----------------END---------------------')

        else:
            print("Please choose Correct option!!")
            print('----------------END---------------------')




    elif branch == "CE":
        print("-------------WELCOME TO CE---------------")
        print("-----------------------------------------")
        print("1. Press 1 Searching by Name\n2. Press 2 Searching by Registration Number\n3. Press 3 Searching by Roll Number")
        print("-----------------------------------------")
        search = int(input("Choose Option :  "))
        print("-----------------------------------------")
        if search == 1:
            name = input("Enter Name : ")
            print("-----------------------------------------")
            data = collection3.find_one({"name" : {"$eq" : name}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(name))
                print('----------------END---------------------')

        
        elif search == 2:
            reg_no = int(input("Enter Registration Number: "))
            print("-----------------------------------------")
            data = collection3.find_one({"_id" : {"$eq" : reg_no}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(reg_no))
                print('----------------END---------------------')
        
        elif search == 3:
            roll_no = input("Enter Roll Number : ")
            print("-----------------------------------------")
            data = collection3.find_one({"roll_no" : {"$eq" : roll_no}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(roll_no))
                print('----------------END---------------------')

        else:
            print("Please choose Correct option!!")
            print('----------------END---------------------')



    elif branch == "ME":
        print("-------------WELCOME TO ME---------------")
        print("-----------------------------------------")
        print("1. Press 1 Searching by Name\n2. Press 2 Searching by Registration Number\n3. Press 3 Searching by Roll Number")
        print("-----------------------------------------")
        search = int(input("Choose Option :  "))
        print("-----------------------------------------")
        if search == 1:
            name = input("Enter Name : ")
            print("-----------------------------------------")
            data = collection4.find_one({"name" : {"$eq" : name}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(name))
                print('----------------END---------------------')

        
        elif search == 2:
            reg_no = int(input("Enter Registration Number: "))
            print("-----------------------------------------")
            data = collection4.find_one({"_id" : {"$eq" : reg_no}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(reg_no))
                print('----------------END---------------------')
        
        elif search == 3:
            roll_no = input("Enter Roll Number : ")
            print("-----------------------------------------")
            data = collection4.find_one({"roll_no" : {"$eq" : roll_no}})
            if type(data) is dict:
                for i,j in data.items():
                    print(i , " : ", j)
                print('----------------END---------------------')
            else:
                print("{} not present".format(roll_no))
                print('----------------END---------------------')

        else:
            print("Please choose Correct option!!")
            print('----------------END---------------------')




    else:
        print("Please enter correct Branch!!")
        print('----------------END---------------------')
    

else:
    print("Please choose the correct option!!")
    print('----------------END---------------------')