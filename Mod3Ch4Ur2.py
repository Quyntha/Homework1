import json
login = input('Введите логин ')
passwd = input('Введите пароль ')
def register(login, passwd):

    with open('login.json','w') as l:
        json.dump(login, l)
    with open('login.json','r') as l:
        login1 = json.load(l)

    print(login1==login)

    with open('passwd.json','w') as p:
        json.dump(passwd, p)
        
    

register(login, passwd)