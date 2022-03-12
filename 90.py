dict={}
while True:
    print("---------------------------Employ Info---------------------------")
    print("1. Search User Info")
    print("2. Add Email ID")
    print("3. Exit")
    try:
        a=int(input("Select Your Option\n"))
        if a==1:
            if len(dict.keys()) == 0:
               print("Nothing to show")
            else:
                User=input("Enter your UserName\n")
                if User in dict.keys():
                    print(dict.get(User))
        elif a==2:
            dict3={}
            UserName=input("Enter your User_Name\n")
            if UserName in dict.keys():
                print("Please Enter Different your User_Name !!")
            elif UserName not in dict.keys(): 
                Name=input('Enter Your Name\n')
                dict3['Name']=Name
                Number=int(input("Enter your Phone Number  :+91"))
                n1=str(Number)
                if len(n1)==10  :
                    if  Number not in dict3.values() :
                        dict3['Number']=Number 
                        Company=input("Enter your Company Name\n")
                        dict3['Company']=Company
                        dict[UserName]=dict3 
                        print("-----------------------Your Account Has Been Successfully Created--------------------------")
                    else:
                         print("The Number is already Use !!")
                else:
                    print("Please Cheack your Number !!")    
        elif a==3:
            print("----------------------------------Exit----------------------------------")  
            break        
    except:
        print("kljhsad")    