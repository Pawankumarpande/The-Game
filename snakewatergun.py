l1=["s","w","g"]
import random
print("*********Welcome to the game of snake,water,gun**********")
print("I am the computer and lets play with me!")
scoreuser=0
scorecom=0
matchtied=0
i=0
c=True
while(c==True):
  user=input("Please enter your choice snake(s),water(w),gun(g)\n")
  com=random.choice(l1)
  i+=1 
 
  if(user==com):
          print(f'computer also choose {com} ')
          print("MATCH TIED!")
          matchtied+=1
  else:
          if (user=='s'):
            if(com=="g"):
              print("you choose snake computer choose gun")
              print("YOU LOST!")
              scorecom+=1
              #sc=scorecom+1
            elif(com=='w'):
              print("you choose snake computer choose water")
              print("YOU WIN!")
              scoreuser+=1
              #su=scoreuser+1
              

          elif (user=='g'):
            if(com=="s"):
              print("you choose gun computer choose snake")
              print("YOU WIN!")
              scoreuser+=1
             # su=scoreuser+1
            elif(com=='w'):
              print("you choose gun computer choose water")
              print("YOU LOST!")
              scorecom+=1
              #sc=scorecom+1
              
          elif (user=='w'):
            if(com=="g"):
              print("you choose water computer choose gun")
              print("YOU WIN!")
              scoreuser+=1
              #su=scoreuser+1
            elif(com=='s'):
              print("you choose water computer choose sanke")
              print("YOU LOST!")
              scorecom+=1
              #sc=scorecom+1
  

  in2=input('press q if you want to quit the game else press y to continue the game ')
  if(in2=='q'):
     print(f"You have quitted the game")
     print(f"Out of {i} games The total wins by the computer is {scorecom} and your total wins is {scoreuser} and {matchtied} number of matches are tied")
     if(scorecom>scoreuser):
       print("YOU HAVE LOST THE SERIES")
     elif(scorecom<scoreuser):
       print("YOU HAVE WON THE SERIES")
     else:
       print("series tied")
     c=False
  else:
     c=True
else:
  print("Thanks for playing")




