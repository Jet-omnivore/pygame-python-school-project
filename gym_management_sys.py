import pickle
import os
from prettytable import PrettyTable
import csv

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

def print_offseted_table(table_string, offset):
    row = ' ' * offset
    for char in table_string:
        if char == '\n':
            print(row) 
            row = ' ' * offset
            continue
        row += char
    print(row)

def load_diet_chart(filename):
    diet_table = PrettyTable()
    diet_table.left_padding_width = 0
    with open(filename) as file:
        reader = csv.reader(file, delimiter='*')
        for i in reader:
            if reader.line_num == 1:
                diet_table.field_names = list(i)
            else:
                diet_table.add_row(i)
    return diet_table

diet_chart = load_diet_chart('diet_chart.txt')

def print_diet_chart():
    os.system('cls')
    print('\n' * 2)
    print_offseted_table(diet_chart.get_string(), 2)
    print('\n' * 2)

def add_user(*args):
    users_data['users'].append(list(args))  

def remove_user(name):
    users = users_data['users']
    for i in range(len(users)):
        if users[i][0] == name:
            users.pop(i)
            return True
    return False

def update_user_data(name, new_age, new_height, new_weight):
    users = users_data['users']
    for i in range(len(users)):
        if users[i][0] == name:
            new_age     = (new_age    + 1 or users[i][1] + 1) - 1
            new_height  = (new_age    + 1 or users[i][2] + 1) - 1
            new_weight  = (new_age    + 1 or users[i][2] + 1) - 1
            users[i][1]    = new_age
            users[i][3]    = new_height
            users[i][4]    = new_weight
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
        print("                                         7. View Diet Chart                                         ") 
        print("                                         8. Exit 👋                                                 ") 

        user_input = input() 
            
        if user_input == '1':
            name       =    input("         Enter Member's Name                                             :   ") 
            while name == '':
                name   =    input("         Name Can't be Empty                                             :   ")

            age        =    input("         Enter Member's Age ( > 14)                                      :   ")
            while not (convertable_to_int(age) and int(age) > 14):
                age    =    input("         Enter Valid Member's Age                                        :   ")
            age        =    int(age)

            height     =    input("         Enter Member's height (in cms)                                  :   ")
            while not (convertable_to_int(height) and int(height) > 0):
                height =    input("         Enter Valid Member's height                                     :   ")
            height     =    int(height)

            weight     =    input("         Enter Member's weight (in kgs)                                  :   ")
            while not (convertable_to_int(weight) and int(weight) > 0):
                weight =    input("         Enter Valid Member's weight                                     :   ")
            weight     =    int(weight)
            
            gender     =    input("         Enter Member's Gender                                           :   ")

            # date of joining -> doj
            doj        =    input("         Enter Date of Joining                                           :   ")
            motive     =    input("         Enter the motive of member to join (Gaining / Leaning)          :   ").lower()[0]

            add_user(name,              # 0
                     age,               # 1
                     doj,               # 2
                     height,            # 3
                     weight,            # 4
                     gender,            # 5
                     motive             # 6
                     )
            prev_msgs.append("Successfully Added New User")

        elif user_input == '2':
            user_name           =    input("         Enter the Name of the User  :   ")
            if remove_user(user_name):
                prev_msgs.append("Successfully Removed")
            else:
                prev_msgs.append("User Doesn't exist")

        elif user_input == '3':
            member_name           =    input("         Enter the member name           :   ")
            while member_name == '':
                member_name       =    input("         Name Can't be Empty             :   ")

            member_new_age        =    input("         Enter Members's New Age         :   ") or -1
            while not convertable_to_int(member_new_age):
                member_new_age    =    input("         Enter Valid Age                 :   ")
            member_new_age        =    int(member_new_age)

            member_new_height     =    input("         Enter Member's New Height       :   ") or -1
            while not convertable_to_int(member_new_height):
                member_new_height =    input("         Enter Valid Height              :   ")
            member_new_height     =    int(member_new_height)

            member_new_weight     =    input("         Enter Member's New Weight       :   ") or -1
            while not convertable_to_int(member_new_weight):
                member_new_weight =    input("         Enter Valid Weight              :   ")
            member_new_weight     =    int(member_new_weight)

            if update_user_data(member_name, member_new_age, member_new_height, member_new_weight):
                prev_msgs.append("Successfully Updated")
            else:
                prev_msgs.append("User Doesn't Exist")

        elif user_input == '4':
            headers = ['NAME', 'AGE', 'DATE OF JOINING', 'HEIGHT', 'WEIGHT', 'GENDER']
            users_table = PrettyTable(headers)

            for user in users_data['users']:
                users_table.add_row(user[:6])

            table_string = users_table.get_string()
            print_offseted_table(table_string, 25)
            
            # print('''
                  # ____________________________________________________________________________________
                 # |____________________________________________________________________________________|
                 # |          NAME            |           AGE                |          GENDER          |
                 # |__________________________|______________________________|__________________________|
                 # |                          |                              |                          |  ''')
            # for user in users_data['users']:
            #     print(' '*16 ,'|' + ' ' * 8 , user[0], ' ' * (15 - len(user[0])), '|' + ' ' * 10, user[1], ' ' * (17 - len(str(user[1]))), '|' + ' ' * 10, user[5], ' ' * (13 - len(str(user[5]))), '|'  )
            # print('''                 |__________________________|______________________________|__________________________|''', '\n')
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
            print_diet_chart() 
            input("                              Press Any Key To Remove Table                  ")
        
        elif user_input == '8':
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
