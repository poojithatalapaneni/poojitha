username=str(input("enter user name"))
userage=int(input("enter your age"))

def age(userage):
    turn=100-userage+2021
    print('%s,your age is %d and you will turn 100 in year %d'%(username,userage,turn))
    return turn

print(age(userage))