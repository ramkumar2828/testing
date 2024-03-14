from cryptography.fernet import Fernet

'''def create_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as keyfile:
        keyfile.write(key)'''



def use_key():
    with open('key.key','rb') as keyfile:
        key = keyfile.read()
        return key




master_pwd = input("enter your master password ")

key = use_key() + master_pwd.encode()

fer = Fernet(key)



def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username,pwd = data.split("|")
            print('username',':',username,'|','password',':',fer.encrypt(pwd.encode()).decode())
        

def add():
    username = input("enter your username ")
    pwd = input("enter your password ")

    with open('passwords.txt','a') as f:
        f.write(username + " | " +fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("are you here to add or view the password or q to quit? (add/view) ").lower()

    if mode == "q":
        quit()

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("enter correct value")
        quit()



