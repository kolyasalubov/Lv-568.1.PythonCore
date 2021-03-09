import re 
  
def valid_password(): 
    password = input("Enter your password: ")
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$#]{6,16}$"
      

    pattern_reg = re.compile(reg) 
    mat = re.search(pattern_reg, password) 
      

    if mat: 
        print("Password is valid.") 
    else: 
        print("Password invalid !!") 

valid_password() 
