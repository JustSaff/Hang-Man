# imports
import turtle as trtl 
import random as rand 
import time as time
import copy as copy

# Variables and List
word_bank = ["victory", "random", "history", "outside", "candy", "money", "coding","tired"]

mystery_word = word_bank[rand.randint(0,3)]
word_spot_num = ""

print(mystery_word)

Letter_list = list(mystery_word)
letter = ""
correct_letters = ["1"]


bg_cordx = 0
bg_cordy = 0
chances = 0

correct = True

# turtle calls
bg_drawer = trtl.Turtle()
hangman_drawer = trtl.Turtle()
letter_drawer = trtl.Turtle()
spot_drawer = trtl.Turtle() 
letter_drawer.pensize(5)
letter_drawer.penup()
letter_drawer.hideturtle()
spot_drawer.hideturtle()
hangman_drawer.hideturtle()
bg_drawer.hideturtle()

letter_drawer.speed(0)
spot_drawer.speed(0)
hangman_drawer.speed(0)
bg_drawer.speed(0)

wn = trtl.Screen()
wn.bgpic("Forest_BG.gif")

# Create Hangman
bg_drawer.pensize(5)
bg_drawer.penup()
bg_drawer.goto(-395,-125) 
bg_drawer.pendown()

bg_drawer.forward(200)
bg_drawer.backward(100)
bg_drawer.left(90)
bg_drawer.forward(400)
bg_drawer.right(90)
bg_drawer.forward(150)
bg_drawer.right(90)
bg_drawer.forward(50)


bg_cordx = bg_drawer.xcor()
bg_cordy = bg_drawer.ycor()

# functions
def count_letters(var):
    global word_spot_num
    word_spot_num = len(var)
    
def spot_length():
    spot_drawer.setheading(0)
    spot_drawer.forward(35)

def create_spots():
    spot_drawer.penup()
    spot_drawer.goto(-50,0)
    spot_drawer.pendown()
    count_letters(mystery_word)
    for spots in range(word_spot_num):
        spot_length()
        spot_drawer.penup()
        spot_drawer.forward(10)
        spot_drawer.pendown()

def draw_head():
    global bg_cordy
    global bg_cordx
    hangman_drawer.pensize(5)
    hangman_drawer.penup()
    hangman_drawer.goto(bg_cordx,bg_cordy)
    hangman_drawer.setheading(270)
    hangman_drawer.forward(35)
    hangman_drawer.setheading(180)
    hangman_drawer.forward(35)
    hangman_drawer.setheading(270)
    hangman_drawer.pendown()
    hangman_drawer.circle(35)
    hangman_drawer.penup()
    hangman_drawer.setheading(0)
    hangman_drawer.forward(35)
    hangman_drawer.setheading(270)
    hangman_drawer.forward(35)   

def draw_body():
    hangman_drawer.pendown()
    hangman_drawer.forward(150)
    hangman_drawer.backward(125)

def draw_arm1():
    hangman_drawer.setheading(225)
    hangman_drawer.forward(50)
    hangman_drawer.backward(50)
    
def draw_arm2():
    hangman_drawer.setheading(315)
    hangman_drawer.forward(50)
    hangman_drawer.backward(50)

def draw_leg1():
    hangman_drawer.setheading(270)
    hangman_drawer.forward(125)
    hangman_drawer.setheading(225)
    hangman_drawer.forward(50)
    hangman_drawer.backward(50)

def draw_leg2():
    hangman_drawer.setheading(315)
    hangman_drawer.forward(50)
    hangman_drawer.backward(50)

def move_letter(amount):
    letter_drawer.forward(amount*70)

def clear_game(win):
    global mystery_word
    global Letter_list
    global mys_len
    global chances
    hangman_drawer.clear()    
    letter_drawer.clear()
    spot_drawer.clear()

    if win == 0:
        letter_drawer.penup()    
        letter_drawer.goto(-50,0)
        letter_drawer.write("You Lose", font=("Arial", 30, "normal"))
        letter_drawer.goto(-50,-25)
        letter_drawer.write("New game starting", font=("Arial", 15, "normal"))
        letter_drawer.goto(-50,50)
        letter_drawer.write("the word is " + mystery_word, font=("Arial", 15, "normal"))

    elif win == 1:
        letter_drawer.penup()    
        letter_drawer.goto(-50,0)
        letter_drawer.write("You Win", font=("Arial", 30, "normal"))
        letter_drawer.goto(-50,-25)
        letter_drawer.write("New game starting", font=("Arial", 15, "normal"))

    correct_letters.clear()
    correct_letters.append("1")
    time.sleep(3)
    hangman_drawer.penup()
    hangman_drawer.goto(bg_cordx,bg_cordy)
    hangman_drawer.pendown()
    letter_drawer.clear()
    mystery_word = word_bank[rand.randint(0,3)]
    Letter_list = list(mystery_word)
    mys_len = int(len(mystery_word))
    chances = 0
    print(mystery_word)
    create_spots()

# quick calls
mys_len = int(len(mystery_word))

# letter checking
def check_a():
    for letter in Letter_list:
        global chances
        global correct
        global mys_len  
        if letter == "a":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)
    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_b():
    global chances
    global correct
    global mys_len  
    for letter in Letter_list:
        if letter == "b":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_c():
    global chances
    global correct
    global mys_len    
    for letter in Letter_list:
        if letter == "c":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_d():
    for letter in Letter_list:
        global chances
        global correct
        global mys_len  
        if letter == "d":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)
    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_e():
    global chances
    global correct
    global mys_len  
    for letter in Letter_list:
        if letter == "e":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_f():
    global chances
    global correct
    global mys_len    
    for letter in Letter_list:
        if letter == "f":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_g():
    for letter in Letter_list:
        global chances
        global correct
        global mys_len  
        if letter == "g":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)
    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_h():
    global chances
    global correct
    global mys_len  
    for letter in Letter_list:
        if letter == "h":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_i():
    global chances
    global correct
    global mys_len    
    for letter in Letter_list:
        if letter == "i":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_j():
    for letter in Letter_list:
        global chances
        global correct
        global mys_len  
        if letter == "j":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)
    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_k():
    for letter in Letter_list:
        global chances
        global correct
        global mys_len  
        if letter == "k":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)
    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_l():
    global chances
    global correct
    global mys_len  
    for letter in Letter_list:
        if letter == "l":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_m():
    global chances
    global correct
    global mys_len    
    for letter in Letter_list:
        if letter == "m":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_n():
    for letter in Letter_list:
        global chances
        global correct
        global mys_len  
        if letter == "n":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)
    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_o():
    global chances
    global correct
    global mys_len  
    for letter in Letter_list:
        if letter == "o":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_p():
    global chances
    global correct
    global mys_len    
    for letter in Letter_list:
        if letter == "p":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_q():
    for letter in Letter_list:
        global chances
        global correct
        global mys_len  
        if letter == "q":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)
    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_r():
    global chances
    global correct
    global mys_len  
    for letter in Letter_list:
        if letter == "r":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_s():
    global chances
    global correct
    global mys_len    
    for letter in Letter_list:
        if letter == "s":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_t():
    for letter in Letter_list:
        global chances
        global correct
        global mys_len  
        if letter == "t":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)
    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_u():
    for letter in Letter_list:
        global chances
        global correct
        global mys_len  
        if letter == "u":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)
    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_v():
    global chances
    global correct
    global mys_len  
    for letter in Letter_list:
        if letter == "v":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_w():
    global chances
    global correct
    global mys_len    
    for letter in Letter_list:
        if letter == "w":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_x():
    for letter in Letter_list:
        global chances
        global correct
        global mys_len  
        if letter == "x":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)
    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_y():
    global chances
    global correct
    global mys_len  
    for letter in Letter_list:
        if letter == "y":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))     
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

def check_z():
    global chances
    global correct
    global mys_len    
    for letter in Letter_list:
        if letter == "z":
            cindex = Letter_list.index(letter)
            letter_drawer.penup()
            letter_drawer.goto(-50,0)
            letter_drawer.forward(cindex*45)
            letter_drawer.write(letter, font=("Arial", 20, "normal"))
            move_letter = copy.copy(letter)
            correct_letters.append(move_letter)
            correct = True
            break
        else:
            correct = False
    cor_let_len = int(correct_letters.index(correct_letters[-1]))
    if cor_let_len == mys_len:
        clear_game(1)

    elif correct == False:
        chances = chances + 1
        if chances == 1:
            draw_head()
        elif chances == 2:
            draw_body()
        elif chances == 3:
            draw_arm1()
        elif chances == 4:
            draw_arm2()
        elif chances == 5:
            draw_leg1()
        elif chances == 6:
            draw_leg2()
            chances = 0
            clear_game(0)

# Events
create_spots()

wn.onkeypress(check_a,"a")
wn.onkeypress(check_b,"b")
wn.onkeypress(check_c,"c")
wn.onkeypress(check_d,"d")
wn.onkeypress(check_e,"e")
wn.onkeypress(check_f,"f")
wn.onkeypress(check_g,"g")
wn.onkeypress(check_h,"h")
wn.onkeypress(check_i,"i")
wn.onkeypress(check_j,"j")
wn.onkeypress(check_k,"k")
wn.onkeypress(check_l,"l")
wn.onkeypress(check_m,"m")
wn.onkeypress(check_n,"n")
wn.onkeypress(check_o,"o")
wn.onkeypress(check_p,"p")
wn.onkeypress(check_q,"q")
wn.onkeypress(check_r,"r")
wn.onkeypress(check_s,"s")
wn.onkeypress(check_t,"t")
wn.onkeypress(check_u,"u")
wn.onkeypress(check_v,"v")
wn.onkeypress(check_w,"w")
wn.onkeypress(check_x,"x")
wn.onkeypress(check_y,"y")
wn.onkeypress(check_z,"z")

wn.listen()

wn.mainloop()