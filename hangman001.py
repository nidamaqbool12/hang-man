#-----------------turtle library related functions-------------------#

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

