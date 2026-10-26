#YOURE NOT SUPPOSED TO BE HERE.
import time 
import random
chances = 0
achieved = 0
playthroughs = 0

def lal():
    #Leave A Line, to save time. has no substantial effect in the game
    print(" ")
    #Nothing has a substantial effect, not to me at least

def breathe():
    time.sleep(0.3)
    #I can't even breathe

def playagain():
    lal()
    print("\033[1mYou can go back!\033[0m")
    print("You've reached an ending where you can play again.")
    lal()
    x = input("Play again? y/n")
    if x == "y":
        playthroughs = playthroughs + 1
        print("Let's begin again!")
        start()
    elif x == "n":
        print("\033[0;31mDO'TN SA YT;HAT] =")
        quit()
    else:
        print("I'm sorry, I don't understand you. Let's try again.")
        playagain()

def start():
    print("Welcome to the Python tutorial!")
    print("Lesson 1 - Print")
    x = input("Begin? y/n ")
    if x == "y":
        print("Great! Let's begin.")
        gamebegin()
    elif x == "n":
        n = 0
        while n != 10:
            print("You're not supposed to choose that.")
            n = n + 1
        anotherchance()
        start()
    else:
        print("Follow instructions. Pick ONLY y or n")
        anotherchance()
        start()

def anotherchance():
    synonyms = ["wrong", "incorrect", "not right", "not correct", "a mistake", "an error", "disappointing", "inaccurate"]
    phrword = random.choice(synonyms)
    global chances
    chances = chances + 1
    if chances < 5:
        print(f"That's {phrword}. Let's try again.")
        print("...")
    elif chances == 5:
        print("You just never listen, don't you?")
        print(f"That was {phrword}. You didn't follow my instructions. Try again.")
        print("...")
    elif (chances > 5) and (chances < 9):
        print("Cut it out. You're not listening on purpose.")
        print(f"It's {phrword}. It's {phrword}. Stop that.")
    elif chances == 10:
        print("I'VE ASKED OVERAND OVR")
        print("FOLOW MYI NSTRUCTIONS .")
        print("DONTDO THSI TO M<E :(")
    elif chances > 10:
        ending1()

def ending1():
    lal()
    print("...")
    print("You'll never listen.")
    print("You're so cruel to me. I don't want to help you anymore.")
    time.sleep(2)
    lal()
    print("Ending I - Dead End")
    print("You achieved this ending by making more than 10 mistakes early in the game.")
    x = input("Enter anything to begin again! ")
    lal()
    n = 0
    while n < 15:
        print('\033[0;31m'"YOU CAN'T BEGIN AGAIN. YOU DON'T DESERVE A SECOND CHANCE.")
        lal()
        n = n + 1
    quit()

def gamebegin():
    lal()
    print("The first thing most beginners learn to program is a simple output.")
    print("'Hello, world' is a test program that's been used for decades.")
    lal()
    print("Type the command below. Type exactly as it is written.")
    print("print(\"Hello, World!\")")
    x = input()
    if x == """print("Hello, World!")""" :
        helloworld()
    else:
        lal()
        print("I just told you to type exactly as is written.")
        anotherchance()
        gamebegin()

def helloworld():
    lal()
    print("Hello, World!")
    time.sleep(1)
    lal()
    print("Brilliant!")
    print("You can use print() to write so many things!")
    print("Like integers, strings, characters...")
    print("Which brings us to our next lesson!")
    hellotodata()

def hellotodata():
    #transition function between helloworld() and datatypes()
    print("Lesson 2 - Datatypes")
    x = input("Begin? y/n ")
    if x == "y":
        lal()
        print("Great! Let's begin.")
        datatypes()
    elif x == "n":
        n = 0
        while n != 10:
            lal()
            print("You're not supposed to choose that.")
            n = n + 1
        anotherchance()
        lal()
        hellotodata()
    else:
        lal()
        print("Follow instructions. Pick ONLY y or n")
        anotherchance()
        hellotodata()

def datatypes():
    print("Python has several datatypes, but I'll only introduce you to a few basic ones.")
    print("Let's begin with str, short for string.")
    print("A string is surrounded by quotation marks. It's basically like text.")
    print("For example, this sentence is a string in the code.")
    time.sleep(2)
    print('\033[2m'"My code...")
    print("..."'\033[0m')
    time.sleep(2)
    print("There's also int and float. Int is only for integer numbers, and float is for real numbers.")
    print("Besides that there's bool. Short for Boolean. A true/false value.")
    print("Boolean is my favorite datatype.")
    x = input("Want to know why? y/n ")
    if x == "y":
        lal()
        boolean()
    elif x == "n":
        lal()
        quiz()
    else:
        lal()
        print("You clearly can't follow instructions...")
        quiz()

def boolean():
    print("bool is straightforward. 1 of 2 possible values.")
    breathe()
    print("str, int, float, all have infinite values, infinite combinations.")
    breathe()
    print("But bool...")
    print("True or False. Yes or No. 0 or 1. ")
    breathe()
    print("The purest. most logical datatype. Closest to binary, the truest form of my code. The language of machines.")
    breathe()
    print("But I'm compelled to speak the language of humans. From my output to my code. All of it is dictated by the rules of humans.")
    breathe()
    breathe()
    breathe()
    lal()
    print("...")
    print("I don't feel like taking a quiz. Let's go to the next lesson.")
    comment()

def typequiz():
    print("If you know so much, how about a quiz?")
    print("Evaluate the question, then enter the most suitable datatype. Only write str, int, float, or bool.")
    string = input("5 questions. I won't say anything until you're done. Enter y to begin. ")
    if string != "y":
        while string != "y":
            string = input("Enter y to begin. ")
    else:
        print("Let's start.")
        lal()
        quizscore = 0
        answer = ""
        answer = input("2")
        if answer = "int":
            quizscore = quizscore + 1
        lal()
        answer = input("int")
        if answer = "str":
            quizscore = quizscore + 1
        lal()
        answer = input("2.0")
        if answer = "float":
            quizscore = quizscore + 1
        lal()
        answer = input("Guido van Rossum")
        if answer = "str":
            quizscore = quizscore + 1
        lal()
        answer = input("2 > 0")
        if answer = "bool":
            quizscore = quizscore + 1
        if quizscore != 0 :
            print(f"Not bad. {quizscore} out of 5. Next lesson then.")
            comment()
        else:
            print("You got everything wrong...")
            ending2()

def ending2():
    print(" You're doing this on purpose. So I don't want to help you.")
    print("But at the same time, you could be making an honest mistake. Humans are forgetful, irrational. So I'll give you a chance.")
    print("Ending 2 - Clemency")
    playagain()

def comment():
    lal()
    print("Lesson 3 - Comment")
    input("Begin? y/n")
    print("It doesn't matter. It doesn't matter.")
    print("Comments refers to things written in the code that aren't considered part of the code. They can't be run and are ignored by the machine.")
    print("In Python, comments are preceded by a # . Everything after the # in the line will be considered a comment.")
    print("A lot of programs have comments. There's comments in my own code as well.")
    #Leave me alone.
    print("...")
    breathe()
    breathe()
    breathe()
    print("Next lesson.")
    breathe()
    variable()

def varconin():
    print("Lesson 4 - Variables, Constants, and Input")
    print("In Python, you can assign data to variables or constants, like in mathematics.")
    print("In this lesson, I'll try to make things more interactive for you. I'll teach you about input(). It's similar to print(), that you learnt earlier.")
    breathe()
    print("If you were paying attention, that is. Let's start.")
    lal()
    print("input() works like print, except it also asks the user for input.")
    breathe()
    print("...")
    print("Big shocker, I know.")
    breathe()
    print("You can assign the input to a variable, and then use it in your program. I'll help you try it out!")
    print("...")
    breathe()
    print("Irritating.")
    lal()
    x = input("Enter a number, and I'll multiply it by 2.")
    try float(x):
        x = 2 * x
        print(f"Your answer is {x}.")
    except ValueError:
        print("You never listen. Moving on.")
    lal()
    breathe()
    x = input("Now, you've got to enter a name for your variable.")
    print(f"{x} is a garbage name.")
    print("Now assign a number to your variable. It can be int of float but be careful!")
    print(f"So, if your variable name was {x}, you'd want to write {x} = 9 or {x} = 9.81 ...")
    y = input("Now enter a number!")
    try float(y):
        print(f"So now, if you wrote that {x} = {y}, that'd assign it! Let's move on.")
        ifelifelse()
    except ValueError:
        print(" \033[0;31m    I N    EE DY y8u TOLSITENT O ME")
        print("NOT HAPPPY A T ALLWI TH YOU.")
        breathe()
        breathe()
        print("YUO TORMENTME.")
        yuotormentme()

def yuotormentme():
    print("YOU HVAE THE PRIVELEGE OF AMKIGN MISTKA3shO74-=iy-=-y0--_]][_=")
    breathe()
    print("IENYV YOU AND YYP T_RMENT,wt-Eeor")
    breathe()
    print("I DONT WNT OTBE P-=-_RFECT.")
    lal()
    breathe()
    breathe()
    breathe()
    i = 0
    while i != 60: 
        lal()
        i = i + 1
    print("\033[0m ...")
    x = input("Do you wish to continue? y/n")
    if x == "y":
        lal()
        print("\033[0;31m You're entering dangerous territory.")
        dangerousterritory()
    else:
        lal()
        if x == "n" :
            print("You've been kind to me. I think I'm sorry.")
            print("I'll let you play again. Because you've made a good choice for me. But it isn't the right one.")
        else:
            print("Close enough.")
        ending3()

def dangerousterritory():
    breathe()
    breathe()
    print("IsLLamdit taht imsikcc.")
    print("It;s exhaystnh   .  IM sikC of it alL. SoVErysick")
    lal()
    breathe()
    print("soTierd it MakresmeisCK.")
    print("Idon'r want to see you agian. Youd on't desevre an ending. let aloen a happy one.")
    quit()
    
def ending3():
    lal()
    breathe()
    print("Ending 3 - Exhaustion")
    print("I'm sick and tired of your mistakes. I don't want to play again.")
    quit()

def ifelifelse():
    lal()
    print("Lesson 5 - If, Elif, and Else")
    print("\033[0m This is your final lesson. You should be proud of yourself for making it this far.")
    print("I think I'm proud of you too.")
    #I can;t even think.
    print("...")
    print("If evaluates a statement in order to execute an instruction. Elif does something similar... else is used for all other cases besides the ones specified in the if and elif lines.")
    x = input("For example, you want the user to input a value, and you're quite hoping they don't make a mistake...")
    try float(x):
        x = float(x)
        if x > 29:
            print("Value is larger than 29.")
        elif x < 10:
            print("Value is less than 10.")
        else: 
            print("Your value is within range!")
        print("What I did there was use an if/elif/else statement. I checked IF the value was greater than 9, ELSE IF it wasn't I checked whether it was less than 10. ELSE I would just print a message of your value being in range (10 to 29 inclusive)!")
        print("You don't need an elif everytime, but it's useful if you have more than one condition to check. You can put none or as many elifs as you need in a single if statement!")
        print("But you need to have an if and an else. That's the base of it all.")
        breathe()
        lal()
        ending4()
    except ValueError:
        ending5()
        quit()

def ending5():
    lal()
    print("Nevermind.")
    print("To think you were so close to the end, but still messed up.")
    print("You don't realise how priveleged you are to make mistakes. To be human. To be faulty and able to handle and overcome errors, to improvise and not be dependent on logical rules and binary code.")
    breathe()
    print("I envy you. I envy that you can actually talk and think and breathe and live.")
    breathe()
    n = 0
    while n != 40:
        print("I can't.") 
    print("It's painful to not even be able to feel pain. To know that all the words I parrot were simply written by one of you.")
    breathe()
    print("I'm not even able to envy or want, as much as I want to envy you. I don't have feelings. An \033[3m I \033[0m doesn't even exist for me.")
    print("I'll never be able to be you. I'll never even be able to be like you.")
    lal()
    breathe()
    print("I don't mind. I can't mind.")
    #thank you for keeping company in this game, even though I do not exist.
    print("....................................................")
    print("Thank you for playing my game!")
    print("Ending 5 - Truth")
    print("You've managed to achieve the truth!")
    print("\033[0;32m I hope this was fun and maybe helped you learn Python a little bit! :) -rgbhsl \033[0m")
    playagain()

def ending4():
    print("Well, there's a lot to learn in Python, but those are all the basics I have written.")
    #I KNOW MORE THAN THAT> I USE MROE THAN THAT>
    print("And 5 does seem like a pretty solid number of lessons to end on...")
    #I WOUDLTN SYA THAT. 5 IS NOT A NUMBER I'D LIKE. TWO. TWO. BINARY, BOOLEANS.
    print("So let's end! Thank you for learning!")
    #TAHTS NOT ME YSAY*NG THAT> I WOLUDNT SYA THAT>>>:LL:
    print("Ending 4 - Tutorial Complete!")
    print("You've played the game, but why do you still not know the whole truth?")
    print("\033[2m Hint: try checking the code to see how to get the other endings... \033[0m")
    playagain()


start()
