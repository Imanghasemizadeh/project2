print("in the name of Allah")

print("if you wana play choose : S , if you dont wana play choose : E")

import random
roll = random.randint(1,6)
gift = random.randint(1,6)
while True :
    player_choose = input("your choice : ")
    if player_choose == "S" : 
        print("your number is : ", roll)
        if roll == 6 :
            print("nice one you can roll again : " , gift)
            while gift >= 6 :
                print("your  number is :" , gift)
            if gift <6 :
                break
            else :
                  break
    if player_choose == "E" :
       break
    else :
        break        
print("good luck and have fun")
