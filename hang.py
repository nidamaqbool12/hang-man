import random
import turtle 
import sys
import time


#----------------------------global variables-------------------------------------#
    

flagW=False
flagL=False
flafA=False
flagWr=False
gameFlag=True
wrongCount=0
hmTC=(0,0)
hm=turtle.Turtle()
hm.speed(0)
state=turtle.Turtle()
state.ht()
#-------------defining functions----------------------------------------------

#-----------------turtle library related functions-------------------#-

#defining correct function 
def correct():
    
        state.clear()
        state.color("green")
        state.write("Correct!!",font=("Arial",50,"bold"))

#defining lose function        
def lose():
    
        state.clear()
        state.color("white")
        state.write("YOU LOSE!!", font=("Arial",50,"bold"))
# now for "this was the movie"
     #cordxy is a variable
        cordxy=letter[0].pos()
        
     #temp is a variable
        temp=turtle.Turtle()
        temp.ht()
        temp.speed(0)
        temp.color("white")
        temp.penup()
        
    #position of "this was the movie"
        temp.setpos(cordxy[0],cordxy[1]+40)
        temp.pendown()
        temp.write("This was the movie:",align="left", font=("Arial", 30, "bold"))
     #at the end for showing the movie
        for i in range(len(movie)):
                if(movie[i] not in user_list_correct):
                        letter[i].color("red")
                        letter[i].write(movie[i],align="left", font=("Arial", 20, "bold"))
#defining function for win
def win():
    
	state.clear()
	state.color("white")
	state.write("YOU WIN!!", font=("Arial",50,"bold"))

#defining function for alredy pressed keys	
def already():


	state.clear()
	state.color("green")
	state.write("YOU Already pressed that key!!", font=("Arial",50,"bold"))
#deining function for wrong choice
def wrong():
    
	state.clear()
	state.color("red")
	state.write("wrong", font=("Arial",50,"bold"))


#-----------------------------Adding Coding------------------------------------------#

def A():
			evaluate(movie,"A")
def B():
			evaluate(movie,"B")
def C():
			evaluate(movie,"C")
def D():
			evaluate(movie,"D")
def E():
			evaluate(movie,"E")
def F():
			evaluate(movie,"F")
def G():
			evaluate(movie,"G")
def H():
			evaluate(movie,"H")
def I():
			evaluate(movie,"I")
def J():
			evaluate(movie,"J")
def K():
			evaluate(movie,"K")
def L():
			evaluate(movie,"L")
def M():
			evaluate(movie,"M")
def N():
			evaluate(movie,"N")
def O():
			evaluate(movie,"O")
def P():
			evaluate(movie,"P")
def Q():
			evaluate(movie,"Q")
def R():
			evaluate(movie,"R")
def S():
			evaluate(movie,"S")
def T():
			evaluate(movie,"T")
def U():
			evaluate(movie,"U")
def V():
			evaluate(movie,"V")
def W():
			evaluate(movie,"W")
def X():
			evaluate(movie,"X")
def Y():
			evaluate(movie,"Y")
def Z():
			evaluate(movie,"Z")
#function which controls the drawing of hangman figure--------------------------
def Hangman(num):
    global hmTC
    if(num==0):

        
        #for corrct characters------------------------------------

            hm.penup()
            hm.setpos(-670,-340)
            hm.pendown()
            hm.ht()
            hm.begin_fill()
            hm.fd(400)
            hm.lt(90)
            hm.fd(50)
            hm.lt(90)
            hm.fd(390)

            hm.rt(90)
            hm.fd(600)
            hm.rt(90)
            hm.fd(400)
            hm.rt(90)
            hm.fd(20)
            hm.lt(90)
            hm.fd(10)


            
            hm.lt(90)
            hmTC=hm.pos()
            hm.fd(30)

            hm.lt(90)
            hm.fd(420)
            hm.lt(90)
            hm.fd(550)
            hm.end_fill()
            
            hm.pensize(5)
            
    elif(num==1):
        
        # user looses one chance
            hm.penup()
            hm.setpos(hmTC[0],hmTC[1])
            hm.rt(90)
            hm.pendown()
            hm.circle(40)
           
    elif(num==2):
            
        #user looses two chances
            hm.penup()
            hm.setpos(hmTC[0],hmTC[1]-80)
            hm.lt(90)
            hm.pendown()
            hm.fd(140)
            hmTC=hm.pos()
           
    elif(num==3):
            
         #user looses 3 chances
            hm.penup()
            hm.rt(30)
            hm.pendown()
            hm.fd(100)
            hm.rt(60)
            hm.fd(10)
            hm.penup()
            hm.rt(180)
            hm.fd(10)
            hm.rt(30)
            hm.fd(100)
            hm.rt(90)
            hm.pendown()
            
    elif(num==4):
            
         #user looses 4 chances
        
            hm.penup()
            hm.setpos(hmTC[0],hmTC[1])

            hm.pendown()
            hm.lt(60)
            hm.fd(100)
            hm.lt(60)
            hm.fd(10)
            #hm.rt(90)



    elif(num==5):
            
         #user looses 5 chances
            hm.penup()
            hm.setpos(hmTC[0],hmTC[1])
            hm.lt(90)
            hm.fd(90)
            hm.lt(180)
            hm.rt(30)
            hm.pendown()
            hm.fd(80)
            hm.rt(60)



    elif(num==6):
         #user looses 6 chances
            hm.penup()
            hm.setpos(hmTC[0],hmTC[1])
            hm.rt(90)
            hm.fd(90)
            hm.lt(180)
            hm.lt(30)
            hm.pendown()
            hm.fd(80)

    elif(num==7):
            
         #user looses 7 chances
            hm.penup()
            hm.setpos(-235.00,265.00)
            hm.rt(90)
            hm.pendown()
            hm.circle(4)
    elif(num==8):
            
         #user looses 8 chances
            hm.penup()
            hm.setpos(-265,265.00)
            hm.rt(90)
            hm.pendown()
            hm.circle(4)

    else:
            
            
         #user looses last chance
           hm.penup()
          hm.setpos(hm.pos()[0]+25,hm.pos()[1]-35)
          hm.pendown()
          hm.rt(30)
          hm.circle(10,180)



