
data_base_dict={}




def get_name():
    while True:
      name=input("enter your name:")
      if not name.isalpha():
          print("please enter a valid name")
          continue
      return name
      
def get_age():
    while True:
        year=(input("enter your birth date:"))
        try:
            int(year)
        except:
            print("please enter a valid date")
            continue
        if int(year) <= 0 :
            print("please enter a valid date")
            continue
        if int(year) in range(2004,2023) :
            print("No Entry")
            break
        if int(year) in range(1942,2004) :
            print("You are welcome")
            break
        else:
            print("please enter a valid date")
            continue
             
    birth=2022-int(year)
    return birth


        
        


def  create_account():
    retries=1
    while retries <=3:
            ask_for_username=input("User name:").lower()
            if not ask_for_username.isalpha():
              print("please enter a valid name")
              retries+=1
              continue
            ask_for_pass=input("password:")
            if len(ask_for_pass) <=5 :
                print("Password must be bigger than five ")
                retries+=1
                continue
            if ask_for_username not in data_base_dict:
                data_base_dict[ask_for_username]=ask_for_pass
                print(f"Now You Have A New Account")
            else:  
                print("This account is already added  before") 
                print("------------------------")
                print("Please Try Again")
                retries+=1
                continue
            if retries > 2 :
                print("Error")
            break 
            
                     
           

def get_signin():
    retries=1
    while retries <=3:
        username_signin=input("USER NAME:").lower()
        password_singin=input("PASSWORD:")
        if username_signin not in data_base_dict :
            print("Please Enter A Valid Account")
            retries+=1
            continue
        
        if  password_singin != data_base_dict[username_signin]:
            print("Please Enter A Valid Password")
            retries+=1
            continue
        if retries > 2 :
            print("Error")
            break
        else:
            print("You Are Sign In")
            break
            
        
        
        
def user_options():
    ask_for_option=input("To 'log in' put '1' , To makw an 'Account' put '2': ")
    if ask_for_option == '1':
        get_signin()
    if ask_for_option == '2':
        create_account()
    

    
get_name()
get_age()
user_options()           
        
    
         
           
             
 




            
        