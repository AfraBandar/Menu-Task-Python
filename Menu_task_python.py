selection = True 
while selection:
    print("""
    please choose a task to do: 

    1- add user 
    2- remove user
    3- add group
    5- add user to group 
    6- show groups and users

       """)
    
    selection = input("please insert task number :")
    if selection=="1": 
      print("\n User added") 
    elif selection=="2":
      print("\n User removed") 
    elif selection=="3":
      print("\n group added") 
    elif selection=="4":
      print("\n user added to group") 
    elif selection=="5":
      print("\n show groups and users")   
    elif selection !="":
      print("\n Not Valid Choice Try again") 