import re 
import class_pwrd_check
import db
from helpers import enter_email, enter_pwrd, create_account, print_pwrd_check


def start_application():
    print("----------------Hi, welcome to the password manager!.-----------------")
    connect = input('Press (p) if you login to the password manager and press (o) if login to other accounts: ').lower()
    if connect == 'p':
        user_email = enter_email()
        check_existing_email(user_email)
    if connect == 'o':
        where_to_connect()


def where_to_connect():
    user_input = input('Where would you like to connect, (y) - Youtube, (g) - Gmail, (f) - Facebook  or (b) - go back: ').lower()
    if user_input == 'y':
        login_to_url('YouTube')
    elif user_input == 'f':
        login_to_url('Facebook')
    elif user_input == 'g':
        login_to_url('Gmail')
    elif user_input == 'b':
        start_application()
    else:
        print('Wrong choice!!')
        where_to_connect()


def login_to_url(url):
    user_email = enter_email()
    for accounts in db.list_of_accounts[url]:
        if user_email == accounts['email']:
            user_password = enter_pwrd()
            check_while = True
            while check_while == True:
                if user_password == accounts['password']:
                    print('You have successfully logged in!')
                    print('Well Done!')
                    check_while = False
                    start_application()
                elif user_password == db.list_of_accounts['Master_Password']:
                    print('You have successfully logged in!')
                    print('Well Done!')
                    check_while = False
                    start_application()
                else: 
                    print('Password doesn\'t match')
                    user_password = enter_pwrd()
                
 
def check_existing_email(email): 
    if len(db.manager_account) > 0:  
        login_to_account(email) 
    else:
        print('email does not exist')
        new_account = input('Would you like to create new account, (y) yes, (n) no?: ').lower()
        if new_account == 'y':
            new_manager_acc = create_account()
            return new_manager_acc
        if new_account == 'n':
            return False
       

def login_to_account(given_email):  
    for val in db.manager_account:  
        if given_email == val["email"]: 
            pwrd = enter_pwrd() 
            while pwrd != val["password"]:   
                print("Password does not match")
                pwrd = enter_pwrd()
            else:
                print('Succesfully logged in') 
                db.current_logged_in["email"] = given_email   
                db.current_logged_in['password'] = pwrd  
                questions_to_do()                              
    else:
        print("Email does not exist")
        new_account_offer()


def questions_to_do():
    question = input('What would you like to do: (c) - create/edit master password, (a) - add accounts to websites, (d) - delete master password, (l) - logout: ').lower()
    if question == 'c': 
        master_password = enter_pwrd() 
        m_password = print_pwrd_check(master_password)
        db.list_of_accounts['Master_Password'] = m_password
        print('Master password was successfully added to the account')
        questions_to_do()
    elif question == 'a':
        add_account_to_websites()
    elif question == 'd':
        delete_account_from_website()
    elif question == 'l':
        logout()   
    else:
        print('Wrong choice')
        questions_to_do()


def logout():
    db.current_logged_in = {}
    print('Successfully logged out')
    start_application()
      
      
def add_account_to_websites():
    account_name = input("To which website would you like to add an account, (y) - Youtube, (g) - Gmail, (f) - Facebook, (b) - go back: ").lower()
    if account_name == 'y':
        new_account = create_account()
        db.list_of_accounts['YouTube'].append(new_account)
        print('Account successfully added')
        questions_to_do()
    elif account_name == 'g':
        new_account = create_account()
        db.list_of_accounts['Gmail'].append(new_account)
        print('Account successfully added')
        questions_to_do()      
    elif account_name == 'f':
        new_account = create_account()
        db.list_of_accounts['Facebook'].append(new_account)
        print('Account successfully added')
        questions_to_do()
    elif account_name == 'b':
        questions_to_do()
    else:
        print('Wrong choice')
        add_account_to_websites()
   

def delete_account_from_website():
    url_choice = input(
        'Where would you like to delete account from? (y) - Youtube, (g) - Gmail, (f) - Facebook or (b) - go back : ')
    if url_choice == 'y':
        if len(db.list_of_accounts['YouTube']) < 1:
            print('There is no accounts to be deleted')
            return questions_to_do()
        else:
            print('Please provide account email and password ')
            user_email = enter_email()
            for account in db.list_of_accounts['YouTube']:
                if user_email == account['email']:
                    user_password = enter_pwrd()
                    db.list_of_accounts['YouTube'].remove(
                    {'email': user_email, 'password': user_password})
                    print('Account have been successfully deleted!')
                    return questions_to_do()        
            print('Email does not exist')
            return questions_to_do()                               
    elif url_choice == 'g':
        if len(db.list_of_accounts['Gmail']) < 1:
            print('There is no accounts to be deleted')
            return questions_to_do()
        else:
            print('Please provide account email and password ')
            user_email = enter_email()
            for account in db.list_of_accounts['Gmail']:
                if user_email == account['email']:
                    user_password = enter_pwrd()
                    db.list_of_accounts['Gmail'].remove(
                    {'email': user_email, 'password': user_password})
                    print('Account have been successfully deleted!')
                    return questions_to_do()        
            print('Email does not exist')
            return questions_to_do()
    elif url_choice == 'f':
        if len(db.list_of_accounts['Facebook']) < 1:
            print('There is no accounts to be deleted')
            return questions_to_do()
        else:
            print('Please provide account email and password ')
            user_email = enter_email()
            for account in db.list_of_accounts['Facebook']:
                if user_email == account['email']:
                    user_password = enter_pwrd()
                    db.list_of_accounts['Facebook'].remove(
                    {'email': user_email, 'password': user_password})
                    print('Account have been successfully deleted!')
                    return questions_to_do()        
            print('Email does not exist')
            return questions_to_do()
    elif url_choice == 'b':
        questions_to_do()
    else:
        print('Wrong choice')
        delete_account_from_website()

 
def new_account_offer():
    new_account = input('Would you like to create new account, (y) yes, (n) no?: ').lower() 
    if new_account == 'y':
        new_manager_acc = create_account()  
        db.manager_account.append(new_manager_acc)  
        login_to_account(new_manager_acc['email'])
    if new_account == 'n':
        return False
  




