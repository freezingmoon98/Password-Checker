import re


def check_digit(pwd: str) -> bool:
    return bool(re.search(r'[0-9]',pwd))

def check_upper(pwd: str) -> bool:
    return bool(re.search(r'[A-Z]',pwd))

def check_lower(pwd: str) -> bool:
    return bool(re.search(r'[a-z]',pwd))

def check_special(pwd: str) -> bool:
    return bool(re.search(r'[~!@#$%^&?]',pwd))

def check_white_space(pwd: str) -> bool:
    return bool(re.search(r'\s',pwd))

def check_length(pwd: str) -> bool:
    return 10 <= len(pwd) <= 20

def check_word():
    pass

def help():
    print("Rules:\n At least 10 characters long, max 20 \n Needs to contain: Upper case and lower case characters, digits, special characters.\n Should not contain: Whitespaces, full words.\n")
    
def main():
    print("---Password Checker--- \n")
    help()
    pwd = input("Please enter a password: ")
    if all([check_digit(pwd),check_upper(pwd),check_lower(pwd),check_length(pwd),check_special(pwd), not check_white_space(pwd)]):
        print("Your password is strong! All requirements met.\n")
    else:
        print("Requirements have not been met.\n")
        
        if not check_digit(pwd):
            print("- Your password needs to have at least one digit (0-9) \n")  
             
        if not check_upper(pwd):
             print("- Your password needs to have at least one upper case character (A-Z) \n")  
              
        if not check_lower(pwd):
             print("- Your password needs to have at least one lower case character (a-z) \n") 
              
        if not check_special(pwd):
             print("- Your password needs to have at least one special character (~!@#$%^&?) \n")  
             
        if not check_length(pwd):
             print("- Your password needs to be at least 10 characters long and maximum 20 long \n") 
              
        if check_white_space(pwd):
             print("- Your password must NOT contain white spaces \n")  
        
             
    
if __name__ == '__main__':
    main()