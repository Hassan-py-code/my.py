import os
import time


def clear():
    os.system('cls') if os.name == 'nt' else os.system("clear")


class User_managment():
    def __init__(self, first_name, last_name, email, password, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def display_user(self):
       print(f"first_name {self.first_name}")
       print(f'last_name {self.last_name}')
       print(f"email {self.email}")
       print(f"password {self.password}")
       print(f"status {self.status}")


def qouition():
    first_name = input('Entre the first_name please:')
    last_name = input('Entre the last_name:')
    email = input('Entre the email:')
    password = input('Entre the password:')
    return User_managment(first_name, last_name, email, password)


new = []
while True:
    print("""
   welcomme to manafment
   1-add 
   2-review
   3-exit""")
    choice = int(input('Entre the choice:'))
    if choice == 1:
        clear()
        new.append(qouition())
        time.sleep(2)
        print('User successfuly!')
    elif choice == 2:
        clear()
        if new:
            print('Display all new.....')
            time.sleep(2)
            for i in new:
                i.display_user()
            time.sleep(2)
    elif choice == 3:
        print('Exit....')
        break
