import json
login = input('Введите логин ')
passwd = input('Введите пароль ')
def login_function(login, passwd):

    with open('login.json','r') as l:
        login1 = json.load(l)

    print(login1==login)

    with open('passwd.json','r') as p:
        passwd1 = json.load(p)

    print(passwd1==passwd)
        
    

login_function(login, passwd)
