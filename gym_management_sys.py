import pickle
import os

# will be used as index to access values in data
FILENAME =  "gym_file.dat"

def load_data(filename=FILENAME) -> dict:
    with open(filename, 'rb') as file:
        try:
            data = pickle.load(file)
        except:
            data = {'users': [], 'main_user': ['avinash', 'avinash']}
    return data

def write_data(data, filename=FILENAME):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

users_data          =  load_data(FILENAME)
# write_data({'users': [], 'main_user': ['avinash', 'avinash']})
MAIN_USER_NAME      =  0
MAIN_USER_PASSWORD  =  1
access_granted      =  False

def add_user(name, age, salary):
    users_data['users'].append([name, age, salary])  

def remove_user(name):
    users = users_data['users']
    for i in range(len(users)):
        if users[i][0] == name:
            users.pop(i)
            return True
    return False

def update_user_data(old_name, new_name, new_age, new_salary):
    users = users_data['users']
    for i in range(len(users)):
        if users[i][0] == old_name:
            new_age     = (new_age    + 1 or users[i][1] + 1) - 1
            new_salary  = (new_salary + 1 or users[i][2] + 1) - 1
            users[i] = [new_name, new_age, new_salary]
            return True
    return False


def convertable_to_int(s):
    try:
        int(s)
        return True
    except:
        return False

def main_sys():
    if not access_granted:
        return
    prev_msgs = ["Welcome " + users_data['main_user'][MAIN_USER_NAME]]
    while True:
        os.system('cls')
        print()
        for msg in prev_msgs:
            print(" " * 40, ' ⚠️ ', msg, ' ❗')
        prev_msgs.clear()
        print('''
                      ___ __   __ __  __        __  __  ___  _  _  ___   ___  ___  __  __  ___  _  _  _____       
                     / __|\ \ / /|  \/  |      |  \/  |/   \| \| |/   \ / __|| __||  \/  || __|| \| ||_   _|      
                    | (_ | \   / | |\/| |      | |\/| || - || .  || - || (_ || _| | |\/| || _| | .  |  | |        
                     \___|  |_|  |_|  |_|      |_|  |_||_|_||_|\_||_|_| \___||___||_|  |_||___||_|\_|  |_|        

                     ''')

        print("                                                                                                    ")
        print("                                         1. Add new User 🤵🏻                                         ")
        print("                                         2. Remove a User 👈🏻                                        ") 
        print("                                         3. Update User Data 🛠️                                   ")
        print("                                         4. Show Users️                                            ")
        print("                                         5. Change Your Password 🔐                                 ")
        print("                                         6. Change Your Registered Name 🆔                          ") 
        print("                                         7. Exit 👋                                                 ") 

        user_input = input() 
            
        if user_input == '1':
            new_user_name       =    input("         Enter New User Name         :   ") 

            new_user_age        =    input("         Enter New User Age          :   ")
            while not (convertable_to_int(new_user_age) and int(new_user_age) > 0):
                new_user_age    =    input("         Enter Valid New User Age    :   ")
            new_user_age        =    int(new_user_age)

            new_user_salary     =    input("         Enter New User salary       :   ")
            while not (convertable_to_int(new_user_salary) and int(new_user_salary) > 0):
                new_user_salary =    input("         Enter Valid New User salary :   ")

            new_user_salary     =    int(new_user_salary)

            add_user(new_user_name, new_user_age, new_user_salary)
            prev_msgs.append("Successfully Added New User")

        elif user_input == '2':
            user_name           =    input("         Enter the Name of the User  :   ")
            if remove_user(user_name):
                prev_msgs.append("Successfully Removed")
            else:
                prev_msgs.append("User Doesn't exist")

        elif user_input == '3':
            user_name           =    input("         Enter the user name         :   ")
            new_user_name       =    input("         Enter User's New Name       :   ") 

            new_user_age        =    input("         Enter User's New Age        :   ") or -1
            while not convertable_to_int(new_user_age):
                new_user_age    =    input("         Enter Valid User Age        :   ")
            new_user_age        =    int(new_user_age)

            new_user_salary     =    input("         Enter User's New salary     :   ") or -1
            while not convertable_to_int(new_user_salary):
                new_user_salary =    input("         Enter Valid User salary     :   ")
            new_user_salary     =    int(new_user_salary)

            if update_user_data(user_name, new_user_name, new_user_age, new_user_salary):
                prev_msgs.append("Successfully Updated")
            else:
                prev_msgs.append("User Doesn't Exist")

        elif user_input == '4':
            print('''
                             ____________________________________________________________________________________
                            |____________________________________________________________________________________|
                            |          NAME            |           AGE                |          SALARY          |
                            |__________________________|______________________________|__________________________|
                            |                          |                              |                          |  ''')
            for user in users_data['users']:
                print(' '*27 ,'|' + ' ' * 8 , user[0], ' ' * (15 - len(user[0])), '|' + ' ' * 10, user[1], ' ' * (17 - len(str(user[1]))), '|' + ' ' * 10, user[2], ' ' * (13 - len(str(user[2]))), '|'  )
            print('''                            |__________________________|______________________________|__________________________|''', '\n')
            input("                              Press Any Key To Remove Table                  ")

        elif user_input == '5':
            new_password        =    input("         Enter Your New Password     :   ")

            while len(new_password) < 8:
                print('\n',"                           ⚠️  PassWord must 8 character long ❗        ",'\n')
                new_password    =    input("                                     :   ")

            users_data['main_user'][MAIN_USER_PASSWORD] = new_password
            prev_msgs.append("Password updated")

        elif user_input == '6':
            new_password        =    input("         Enter Your New User Name    :   ")
            users_data['main_user'][MAIN_USER_NAME] = new_password
            prev_msgs.append("UserName updated")
        
        elif user_input == '7':
            break

def login_ui():
        global access_granted
        main_user = users_data['main_user']
        if access_granted:
            main_sys()
        while not access_granted:
            os.system('cls')
            print('''   
                                     _          __ _  _              _   _  ___ 
                                    | |    ___ / _` |(_) _ _        | | | ||_ _|
                                    | |__ / _ \\\\__. || || ' \       | |_| | | | 
                                    |____|\___/|___/ |_||_||_|       \___/ |___|

                    ''')

            input_name     = input("         1. Enter Your Name      📜    :        ")
            input_password = input("         2. Enter Your Password  🔐    :        ")   

            if [input_name, input_password] == main_user:
                access_granted = True
                main_sys()
            else:
                print('''

                                          ⚠️ Invalid User Name or Password ❗            

                                               1. Exit 👋              
                                               2. Press Any other Key to Retry 🔄              ''')
                if input() == '1':
                    break


def main_ui():
    while True:
        os.system('cls')
        print('''

                      ___ __   __ __  __        __  __  ___  _  _  ___   ___  ___  __  __  ___  _  _  _____       
                     / __|\ \ / /|  \/  |      |  \/  |/   \| \| |/   \ / __|| __||  \/  || __|| \| ||_   _|      
                    | (_ | \   / | |\/| |      | |\/| || - || .  || - || (_ || _| | |\/| || _| | .  |  | |        
                     \___|  |_|  |_|  |_|      |_|  |_||_|_||_|\_||_|_| \___||___||_|  |_||___||_|\_|  |_|        

                     ''')

        print("                                     HOW CAN WE HELP YOU ?                                ")
        print("                                                                                          ")
        print("                                     1. Login 🤚                                          ")
        print("                                     2. Exit  👋                                           ") 

        user_input = input() 
        if user_input == '1':
            login_ui()
        elif user_input == '2':
            return

main_ui()

#write all the data before exiting
write_data(users_data)
