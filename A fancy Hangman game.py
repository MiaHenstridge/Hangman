# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:10:55 2021

@author: congc
"""
#Import modules
import random
rng=random.Random()
from english_words import english_words_lower_alpha_set
wordlist = list(english_words_lower_alpha_set)
import turtle
import time
import string


#Setting up turtle screen playground
turtle.clear()
wn = turtle.Screen()
wn.setup(width = 1.0, height = 1.0)
wn.bgcolor('White')
wn.title("Let's play Hangman!")

#Setting up turtles
mia = turtle.Turtle()
mia.penup()
mia.hideturtle()

hidden = turtle.Turtle()
hidden.penup()
hidden.hideturtle()

comment = turtle.Turtle()
comment.penup()
comment.hideturtle()

attempt = turtle.Turtle()
attempt.penup()
attempt.hideturtle()

hangman = turtle.Turtle()
hangman.penup()
hangman.hideturtle()

halp = turtle.Turtle()
halp.penup()
halp.hideturtle()


#Functions to reset, enter, and reposition turtles (to save time typing)
def enter(turtle_name,lineheight):
    turtle_name.penup() 
    turtle_name.right(90)
    turtle_name.forward(lineheight)
    turtle_name.left(90)
    turtle_name.pendown()

    
def reset_turtle(turtle_name):
    turtle_name.reset()
    turtle_name.hideturtle()
    

def reposition(turtle_name,x,y):
    turtle_name.penup()
    turtle_name.forward(x)
    turtle_name.left(90)
    turtle_name.forward(y)
    turtle_name.right(90)
    turtle_name.pendown()
  

#Hangman drawing functions, skip this part if you're not interested
def hangman_base():
    reposition(hangman, 200, -150)
    hangman.pencolor(hman)
    hangman.pensize(5)
    hangman.forward(150)
    hangman.penup()
    hangman.forward(-75)
    hangman.left(90)
    hangman.pendown()

    
def hangman_pole():
    hangman.forward(400)
    hangman.right(90)


def hangman_3rd_stroke():
    hangman.forward(150)
    hangman.right(90)
    
    
def hangman_hanger():
    hangman.forward(40)
    hangman.right(90)


def hangman_head():
    hangman.circle(40,360)
    hangman.left(90)
    hangman.penup()
    hangman.forward(80)
    hangman.pendown()
    
    
def hangman_body():
    hangman.forward(175)
    hangman.penup()
    hangman.forward(-150)
    hangman.pendown()
    
    
def hangman_leftarm():
    hangman.right(45)
    hangman.forward(80)
    hangman.penup()
    hangman.forward(-80)
    hangman.left(90)
    hangman.pendown()
    
    
def hangman_rightarm():
    hangman.forward(80)
    hangman.penup()
    hangman.forward(-80)
    hangman.right(45)
    
    
def hangman_leftleg():
    hangman.pendown()
    hangman.forward(150)
    hangman.right(45)
    hangman.forward(100)
    hangman.penup()
    hangman.forward(-100)
    hangman.left(90)
    hangman.pendown()
    
    
def hangman_rightleg():
    hangman.forward(100)
    hangman.penup()
 
    
def halp_me():
    halp.pencolor(scream)
    halp.pensize(3)
    reposition(halp, 550, 270)
    halp.write('Halp me!!! (●＞д＜)',False,font = ('Roboto Slab',18,'bold'),align = 'center')
           
    
#Game functions
def welcome():
    wn.bgcolor(bg)
    turtle.color(bg)
    mia.pencolor(text)
    mia.write('Welcome to Hangman!',move=False,font=('Roboto Slab',32,'normal'),align= 'center')
    enter(mia, 50)
    mia.write('Press Space to start...',move=False,font=('Roboto Slab',16,'normal'),align= 'center')
    wn.onkey(instructions, 'space')
    wn.onkey(bye,'Escape')

    
    
def instructions():
    reset_turtle(mia)
    mia.pencolor(text)
    mia.write('Guess the letters to get the correct word before the hangman is executed!', move = False,font = ('Roboto Slab',20,'normal'),align = 'center')
    enter(mia,50)
    mia.write('Press Space to start playing :3',move=False,font=('Roboto Slab',16,'normal'),align= 'center')
    wn.onkey(game_start,'space')
    wn.onkey(bye,'Escape')
    

def game_start():  
    global word
    global hidden_word_list
    global attempts_left
    global guessed_letters
    global definition
    
    
    attempts_left = 10   
    word = wordlist[rng.randrange(0,len(wordlist)-1)] 
    hidden_word_list = list()
    guessed_letters = ''
    for i in word:
        hidden_word_list.append('_')  

    time.sleep(0.5)
    reset_turtle(mia)
    mia.pencolor(text)
    reposition(mia,-250, 100)   
    mia.write('Guess this {0}-letter word!'.format(len(word)),move=False,font= ('Roboto Slab',24,'normal'),align='center')
    enter(mia,30)
    mia.write('Input guess in the popup window.',move=False,font= ('Roboto Slab',16,'normal'),align='center')
    
    reset_turtle(attempt)
    reposition(attempt, -250, 40)
    attempt.pencolor(text)
    attempt.write('You have {0} attempts left.'.format(attempts_left),font=('Roboto Slab',16,'normal'),align='center')
    
    reposition(hidden, -250, -70) 
    hidden.pencolor(text)
    hidden_word = ''
    for k in hidden_word_list:
        hidden_word += k
    hidden.write(hidden_word,move=False,font=('Roboto Slab',30,'normal'),align= 'center')
    game_over()
    wn.onkey(bye,'Escape')
    
    
def game_over():
    global word
    global hidden_word_list
    global attempts_left
    global guessed_letters
    
    word_guessed = False
    while word_guessed == False:
        if "_" not in hidden_word_list:
            time.sleep(1)
            reset_turtle(mia)
            reset_turtle(hidden)
            reset_turtle(comment)
            reset_turtle(attempt)
            reset_turtle(hangman)
            reset_turtle(halp)
            mia.pencolor(text)
            mia.write('Congratulations! You have guessed the word: "{0}"!'.format(word),False,font=('Roboto Slab',24,'normal'),align='center')
            enter(mia, 50)
            mia.write("You've saved the Hangman!",False, font=('Roboto Slab',16,'normal'),align='center')
            word_guessed = True

        elif attempts_left==0:
            time.sleep(1)
            reset_turtle(mia)
            reset_turtle(hidden)
            reset_turtle(comment)
            reset_turtle(attempt)
            reset_turtle(hangman)
            reset_turtle(halp)
            mia.pencolor(text)
            mia.write('Oops! You ran out of attempts. The word is "{0}"!'.format(word),False,font=('Roboto Slab',24,'normal'),align='center')
            enter(mia, 50)
            mia.write("Hangman has been executed!",False, font=('Roboto Slab',16,'normal'),align='center')
            word_guessed = True

        else:
            game_process()
        
    if word_guessed == True:
        time.sleep(3)
        game_start()    
    
    
def bye():
    wn.bye()
    
    
def game_process():
    global word
    global hidden_word_list
    global attempts_left
    global guessed_letters
    global guess
    
    wn.onkey(bye,'Escape')
    player_input = turtle.textinput('Your guess', 'Enter your guess here:')
    if player_input is None:
        bye()
    else:
        guess = player_input.lower()
        if len(guess) >1:
            reset_turtle(comment)
            reposition(comment, -250, -150)
            comment.pencolor(text)
            comment.write('Chill! I can only take single-letter inputs!',False,font=('Roboto Slab',18,'normal'),align='center')
            wn.onkey(bye,'Escape')
        else:
            if guess not in string.ascii_lowercase:
                reset_turtle(comment)
                reposition(comment, -250, -150)
                comment.pencolor(text)
                comment.write('Letters only, please!',False,font=('Roboto Slab',18,'normal'),align='center')
                wn.onkey(bye,'Escape')
            else:
                if guess in guessed_letters:
                    reset_turtle(comment)
                    reposition(comment, -250, -150)
                    comment.pencolor(text)
                    comment.write('You have already tried that letter.',False,font=('Roboto Slab',18,'normal'),align='center')
                    wn.onkey(bye,'Escape')
                else:
                    if guess in word:
                        guessed_letters += guess
                        indexes =[]
                        start = 0
                        for i in word:
                            if i == guess:
                                indexes.append(word.index(i,start))
                                start = indexes[len(indexes)-1] + 1
                        for k in indexes:
                            hidden_word_list[k]=guess
                            
                        hidden_word = ''
                        for k in hidden_word_list:
                            hidden_word += k
                        reset_turtle(hidden)
                        reposition(hidden, -250, -70) 
                        hidden.pencolor(text)
                        hidden.write(hidden_word,move=False,font=('Roboto Slab',30,'normal'),align= 'center')
                        
                        reset_turtle(comment)
                        reposition(comment, -250, -150)
                        comment.pencolor(text)
                        comment.write('Yay! There is/are {0} letter(s) {1} in the word.'.format(word.count(guess), guess),False,font=('Roboto Slab',18,'normal'),align='center')
                        wn.onkey(bye,'Escape')
                    else:
                        guessed_letters += guess
                        attempts_left = attempts_left - 1
                        
                        reset_turtle(comment)
                        reposition(comment, -250, -150)
                        comment.pencolor(text)
                        comment.write('Oops! There is no letter {0} in the word.'.format(guess),False,font=('Roboto Slab',18,'normal'),align='center')
                        
                        reset_turtle(attempt)
                        reposition(attempt, -250, 40) 
                        attempt.pencolor(text)
                        attempt.write('You have {0} attempts left.'.format(attempts_left),font=('Roboto Slab',16,'normal'),align='center')
                        
                        if attempts_left == 9:
                            hangman_base()
                        elif attempts_left == 8:
                            hangman_pole()
                        elif attempts_left == 7:
                            hangman_3rd_stroke()
                        elif attempts_left == 6:
                            hangman_hanger()
                        elif attempts_left == 5:
                            hangman_head()
                        elif attempts_left == 4:
                            hangman_body()
                        elif attempts_left == 3:
                            hangman_leftarm()
                        elif attempts_left == 2:
                            hangman_rightarm()
                            halp_me()
                        elif attempts_left == 1:
                            hangman_leftleg()
                        elif attempts_left == 0:
                            hangman_rightleg()

      
#setting up some color themes to make the game more fancy
color_palettes = [['#E0FBFC','#253237','#5C6B73','#C2DFE3'],['#FFFAFB','#131515','#339989','#7DE2D1'],['#DDDDDF','#111D13','#415D43','#A1CCA5'],['#DCC48E','#27233A','#EAEFD3','#B3C0A4'],['White','#172A3A','#BB4430','#AE759F'],['#FFFFFF','#6D696A','#A2A7A5','#E2DADB'],['#EAD2AC','#1D201F','#C58882','#D1DEDE'],['#AAB9CF','#212227','#BDD4E7','#637074'],['#DCEDFF','#343F3E','#8F91A2','#94B0DA'],['#0D1F2D','#E4C3AD','#9EA3B0','#546A7B'],['#1D1E18','#D9FFF5','#2C3A2E','#6B8F71'],['#230903','#D3B88C','#656256','Brown'],['#495867','#BDD5EA','#FE5F55','RoyalBlue14'],['#9B1D20','#D0FFCE','#3D2B3D','#635D5C'],['#6A381F','#FFFFB3','#6E0D25','#774E24'],['#104547','#D2D6EF','#4B5358','#727072'],['#E83151','#DBD4D3','#387780','#757780']]                       
player_choice = turtle.numinput('Color theme','Choose your color theme from 0 to {0}:'.format(len(color_palettes)-1))

if player_choice is None:
    bye()
elif player_choice < 0 or player_choice >= len(color_palettes):
    color_theme = color_palettes[rng.randrange(0,len(color_palettes))]
    [text,bg,hman,scream] = color_theme
    welcome()
else:
    if player_choice > len(color_palettes)-1 or player_choice < 0:
        color_theme = color_palettes[rng.randrange(0,len(color_palettes))]
    else:
        color_theme = color_palettes[int(player_choice)]
        [text,bg,hman,scream] = color_theme
        welcome()
    
wn.listen() 
wn.mainloop()
