import class_pwrd_check

def enter_email(): 
    enter_email = input('Enter email: ')
    return enter_email


def enter_pwrd():
    enter_pwrd = input('Enter password: ')
    return enter_pwrd

def create_account():
    user_email = enter_email() 
    user_password = enter_pwrd() 
    password = print_pwrd_check(user_password) 
    account = {   
        "email": user_email,  
        "password": password 
    }
    return account
    
def print_pwrd_check(user_password):    
    while class_pwrd_check.PasswordCeck(user_password).validate() == False:
        print("Use at least 8 characters")  
        print("Use at least 1 digit number")
        print("Use at least 1 letter")
        print("Use at least 1 upper case")
        print("Use at least 1 lower case")
        print("Use at least 1 special character")
        user_password = input("Reenter new password: ")
    return user_password