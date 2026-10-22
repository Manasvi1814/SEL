# SNAKE ,WATER,GUN GAME 

# PLAYER - 1 & PLAYER - 2
import random
dic={
    1:"snake",
    0:"water",
    -1:"gun"
}
computer=random.choice([0 , 1 , -1])


def game(life_1 , life_2) :
    while life_1 !=0 and life_2 !=0 :
        ch_1 =input("PLAYER - 1 ! , CHOICE : ")
        ch_2 =input("PLAYER - 2 ! , CHOICE : ")
        if ch_1 =="snake" and ch_2 =="water":
            life_1=life_1-1
            print(f" PLAYER - 2 WINSS !! \n PLAYER - 1 : LIVES: {life_1}")
            
        elif ch_1 =="water" and ch_2 =="snake":
            life_2=life_2-1
            print(f" PLAYER - 1 WINSS !! \n PLAYER - 2 : LIVES: {life_2}")
            
        elif ch_1 =="water" and ch_2 =="gun":
            life_2=life_2-1
            print(f" PLAYER - 1 WINSS !! \n PLAYER - 2 : LIVES: {life_2}")
            
        elif ch_1 == "gun" and ch_2 =="water":
            life_1=life_1-1
            print(f" PLAYER - 2 WINSS !! \n PLAYER - 1 : LIVES: {life_1}")
            
        
        elif ch_1 =="gun" and ch_2 =="snake":
            life_2=life_2-1
            print(f" PLAYER - 1 WINSS !! \n PLAYER - 2 : LIVES: {life_2}")
            
        
        elif ch_1 =="snake" and ch_2 =="gun":
            life_2=life_2-1
            print(f" PLAYER - 2 WINSS !! \n PLAYER - 1 : LIVES: {life_1}")
            

        elif ch_1 == ch_2:
            print("TIE!!")
            
    
    print(" GAME OVER !! ")
    if life_1 ==0:
        print("PLAYER 2 IS WINNER !! ")
    else:
        print(" PLAYER 1 IS WINNER !! ") 
    return (life_1,life_2)

game(3,3)
