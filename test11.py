print("in the name of Allah")

print("if you wana play choose : S , if you dont wana play choose : E")

import random

while True :
    player_choose = input("your choice : ")

    if player_choose == "S" :  
       roll = random.randint(1,6)
       print("your number is : ", roll)
       if roll == 6 :
        print("nice one you can roll again")
        roll_num_2 = random.randint(1,6)
        print("your second_roll number is :" , roll_num_2)
       else :
          break
    if player_choose == "E" :
       break
    else :
       print("wrong choice")
print("good luck and have fun")