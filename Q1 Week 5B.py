import random

choice = 1
while choice != 0 :
    
    password = list() #password

    for i in range(0,2):

        rand_num=random.randint(48,57)
        password.append(chr(rand_num))
        
        rand_upper=random.randint(65,90)
        password.append(chr(rand_upper))
        
        rand_lower=random.randint(97,122)
        password.append(chr(rand_lower))
        
        rand_special=['@','$','%','&','*','!']
        rand = random.randint(0,5)
        password.append(rand_special[rand])

    for i in range(0,8):

        rand1 = random.randint(0,7)
        rand2 = random.randint(0,7)

        password[rand1],password[rand2] = password[rand2],password[rand1]

    final = ''.join(password)
    print(f"Password generated : {final}")
    choice = int(input("\nEnter your choice[1/0] :"))
    
    

