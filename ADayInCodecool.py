import time
print("Hello mister!")
time.sleep(2)
print()
playername = input("Please enter your name! ")
playername = playername.title()
time.sleep(2)
print()
print("Hello {}!".format(playername))
input("Press ENTER to continue...")
time.sleep(2)
print()
print("You're at home on a monday morning,")
time.sleep(2)
print("too tired to do anything, but you have to go to Codecool.")
time.sleep(2)
print("You have a few minutes before going. What would you do?")
time.sleep(2)
while True:
    print()
    choice = input("[1] DRINK A COFFEE\n[2] TAKE A SHOWER\n[3] HAVE BREAKFAST\n[4] GO TO CODECOOL\n[5] WATCH TV IN BED\n")
    if choice == "1":
        time.sleep(2)
        print("You drank a mug of coffee. You feel fresh and energized.\n")
        time.sleep(2)
    elif choice == "2":
        time.sleep(2)
        print("You took a shower. You feel wet and miserable.\n")
        time.sleep(2)
    elif choice == "3":
        time.sleep(2)
        print("Unfortunately, you haven't got money for food. Well, bad for you.\n")
        time.sleep(2)
    elif choice == "4":
        time.sleep(2)
        print("You have decided to go on a marvelous adventure.\n")
        time.sleep(2)
        break
    elif choice == "5":
        time.sleep(2)
        print("You fell asleep and late from Codecool. You are pathetic. The GAME is OVER.\n")
        time.sleep(2)
        exit()
    else:
        time.sleep(2)
        print("Why did you entered '{}' ? Enter the number of the choosen option!\n".format(choice))
print()
print("You are on the streets.")  
time.sleep(2)
print("Walking.")
time.sleep(2)
print("You see a dead tree.")
time.sleep(2)
print("It is dreary as your soul.")
time.sleep(2)
print("But then, you see a happy bunny jumping across the road.")
time.sleep(2)
print("A car run over it.")
time.sleep(2)
print("Poor bastard.")
time.sleep(2)
print()
print("[AFTER TRAVELLING A WHILE...]")
print()
time.sleep(2)
print("You have arrived to Codecool.")
time.sleep(2)
print("You see some Codecoolers, smoking in the parking lot.")
time.sleep(2)
print()
choice2 = input("[1] GO THERE\n[2] GO INSIDE\n")
choice3 = ()
if choice2 == "1":
    time.sleep(2)
    print("You going to the lot, and one of them offer you a cigarette.")
    time.sleep(2)
    print()
    choice3 = input("[1] ACCEPT\n[2] REFUSE\n")
    while True:
        if choice3 == "1":
            time.sleep(2)
            print("Did you know that cigarettes are bad for your health?")
            time.sleep(2)
            print("Well, you wanted it.")
            time.sleep(2)
            print("Come on!")
            time.sleep(2)
            print("Smoke that $#*! !")
            time.sleep(2)
            print("Your lungs are slowly rotting.")
            time.sleep(2)
            print("After you finished smoking, you walk into the office.")
            time.sleep(2)
            break
        elif choice3 == "2":
            time.sleep(2)
            print("You care about the environment and your health, so you refuse that evil lung-killer piece of junk!\n")
            time.sleep(2)
            break
        else:
            time.sleep(2)
            print("Why did you entered '{}' ? Enter the number of the choosen option!\n".format(choice3))
elif choice2 == "2":
    time.sleep(2)
    print("You do not care about the others, just head to the office.")
    time.sleep(2)
    print()
else:
    time.sleep(2)
    print("Why did you entered '{}' ? Enter the number of the choosen option!\n".format(choice2))
print()
print("[IN THE OFFICE...]")
time.sleep(2)
print("You are greeted by the students and mentors.")
time.sleep(2)
print("The choice is in your hands.")
time.sleep(2)
while True:
    print()
    choice4 = input("[1] GREET THEM\n[2] BE AN ASSHOLE\n")
    if choice4 == "1":
        time.sleep(2)
        print("You greet the others and take your seat.")
        time.sleep(2)
        break
    elif choice4 == "2":
        time.sleep(2)
        print("You decided to be an asshole.")
        time.sleep(2)
        print("This incident touched one of the mentor's soul, he became an angry psychopath and beat the hell out of you.")
        time.sleep(2)
        print("GAME OVER!")
        exit()
    else:
        time.sleep(2)
        print("Why did you entered '{}' ? Enter the number of the choosen option!\n".format(choice4))
print()
print("The lessons began, and you are tired as F.")
time.sleep(2)
print()
while True:
    choice5 = input("[1] CHAT ON FACEBOOK\n[2] PAY ATTENTION\n[3] GO OUT AND DRINK A COFFEE\n[4] DANCE\n")
    if choice5 == "1":
        time.sleep(2)
        print("You can't chat on Facebook because you haven't got any friends.")
        time.sleep(2)
    elif choice5 == "2":
        time.sleep(2)
        print("Good choice! Maybe one day you will become a software developer! But I doubt it.")
        time.sleep(2)
        break
    elif choice5 == "3":
        time.sleep(2)
        print("You go out in the middle of the course to have a coffee. Not a wise decision.")
        time.sleep(2)
        break
    elif choice5 == "4":
        time.sleep(2)
        print("Congratulations! Now the people at Codecool think you're an autist.")
        time.sleep(2)
        break
    else:
        time.sleep(2)
        print("Why did you entered '{}' ? Enter the number of the choosen option!\n".format(choice5))
print()
print("It's lunchtime. You feel tired and hungry. What will you do?")
time.sleep(2)
choice6 = ()
while True:
    print()
    choice6 = input("[1] COLLECT LUNCH MONEY FROM CODECOOLERS\n[2] COLLECT LUNCH MONEY FROM MENTORS\n[3] HAVE LUNCH\n[4] WATCH HOW THE OTHERS EAT\n")
    if choice6 == "1":
        time.sleep(2)
        print("You choose your victim and perform the act. The fellow Codecooler now hates you, but at least you have money and you can buy a sandwich.")
        time.sleep(2)
        break
    elif choice6 == "2":
        time.sleep(2)
        print("'This will be a piece of cake' -you said. You threathened one of the mentors, who used a special mentor ability to ground you. You have been torn to pieces. Goodbye programming carreer in Codecool, hello disabled lifestyle! ")
        time.sleep(2)
        exit()
    elif choice6 == "3":
        time.sleep(2)
        print("You have neither lunch, nor the money to buy it.")
        time.sleep(2)
    elif choice6 == "4":
        time.sleep(2)
        print("You watch somebody with a sad smile long enough to give you some food. You have the skill to become a good hobo once.")
        time.sleep(2)
        break
    else:
        time.sleep(2)
        print("Why did you entered '{}' ? Enter the number of the choosen option!\n".format(choice6))
print()
print("Lunch time is over! Time to go back to studying!")
time.sleep(2)
print()
print("The course is tiresome and hard. What will you do?")
time.sleep(2)
while True:
    print()
    choice7 = input("[1] FALL ASLEEP\n[2] YAWN\n[3] DO PUSHUPS\n[4] PAY ATTENTION\n")
    if choice7 == "1":
        time.sleep(2)
        print("You fall asleep and start snorting. Later one of the mentor wakes you up then beats the hell out of you.")
        time.sleep(2)
        print("GAME OVER!")
        exit()
    elif choice7 == "2":
        time.sleep(2)
        print("After a big yawn you get an angry look from the mentor.")
        time.sleep(2)
    elif choice7 == "3":
        time.sleep(2)
        print("You won't be a good programmer but at least you will be strong.")
        time.sleep(2)
        break
    elif choice7 == "4":
        time.sleep(2)
        print("Good boy. You might actually learn something.")
        time.sleep(2)
        break
    else:
        time.sleep(2)
        print("Why did you entered '{}' ? Enter the number of the choosen option!\n".format(choice7))
print()
print("The day is finally over, you may do the following activities:")
time.sleep(2)
choice8 = ()
while True:
    print()
    choice8 = input("[1] GO HOME\n[2] PLAY PS4\n[3] DO PUSHUPS\n[4] PLAY DARTS\n[5] STUDY\n")
    if choice8 == "1":
        time.sleep(2)
        print("You are going home.")
        time.sleep(2)
        break
    elif choice8 == "2":
        time.sleep(2)
        print("People don't allow you to play on the PS4 because you are not a liked person.")
        time.sleep(2)
    elif choice8 == "3":
        time.sleep(2)
        print("Everybody staring at you while you do pushups all alone. They think you are an introverted faggot.")
        time.sleep(2)
    elif choice8 == "4":
        time.sleep(2)
        print("You are started to play darts, but your opponent threw the dart into your eye by accident. Your name is Dart {} from now on. You started to go home.".format(playername))
        time.sleep(2)
        break
    elif choice8 == "5":
        time.sleep(2)
        print("Good job! It's a shame you didn't learn anything.")
        time.sleep(2)
    else:
        time.sleep(2)
        print("Why did you entered '{}' ? Enter the number of the choosen option!\n".format(choice8))
print()
print("While you are going home, you see a hobo begging for money.")
time.sleep(2)
while True:
    print()
    choice9 = input("[1] GIVE HIM MONEY\n[2] MOVE ON\n[3] DO PUSHUPS\n[4] WRITE A PYTHON PROGRAM FOR HIM\n")
    if choice9 == "1":
        while True:
            if choice8 == "4":
                time.sleep(2)
                print("You haven't got any money, but the hobo feels sorry for you because of the dart in your eye, so he gives you some change. You have some money now.")
                break
            else:
                break
        time.sleep(2)
        print("You don't have any money. You should join him too.")
        time.sleep(2)
    elif choice9 == "2":
        while True:
            if choice8 == "4":
                time.sleep(2)
                print("The hobo yells at you and taunts you because of the dart in your eye.")
                break
            else:
                break
        time.sleep(2)
        print("You act like an asshole and move on. I hope you are proud of yourself.")
        time.sleep(2)
        break
    elif choice9 == "3":
        while True:
            if choice8 == "4":
                time.sleep(2)
                print("You start doing pushups. Unfortunately while doing it, the ground pushes the dart which in your eye into your skull, and your brain got spitted.")
                time.sleep(2)
                if choice6 == "1":
                    print("The hobo searches your pockets, and he steal the money what you stole from the Codecooler.")
                    time.sleep(2)
                    print("GAME OVER!")
                    time.sleep(2)
                    exit()
                else:
                    print("The hobo searches your pockets, but he becomes sad as he can't find anything.")
                    time.sleep(2)
                    print("GAME OVER!")
                    time.sleep(2)
                    exit()
            else:    
                time.sleep(2)
                print("You start doing pushups, the hobo thinks you are crazy so he leaves.")
                time.sleep(2)
                break
        break
    elif choice9 == "4":
        while True:
            if choice8 == "4":
                time.sleep(2)
                print("Are you out of your mind?! You have a freaking dart in your eye, and you wanna make a program? This is what I call passion.")
                time.sleep(2)
                print("Sorry {}, I won't let you do this. You are going home.".format(playername))
                break
            else:
                time.sleep(2)
                print("You write a program for the hobo in python. He gets rich from it but he doesn't give you anthing from his wealth.")
                time.sleep(2)
                break
        break
    else:
        time.sleep(2)
        print("Why did you entered '{}' ? Enter the number of the choosen option!\n".format(choice9))
print()
print("You arrive home at last. You can do the following things at home:")
while True:
    print()
    choice10 = input("[1] DO ASSIGNMENTS\n[2] THINK ABOUT LIFE\n[3] PLAY ON COMPUTER\n[4] CRY IN THE CORNER\n[5] PENGUIN\n")
    if choice10 == "1":
        time.sleep(2)
        print("You start doing your assignment...but you can't do it. Sad.")
        time.sleep(2)
    elif choice10 == "2":
        time.sleep(2)
        print("You are thinking of the meaning of life, and you discovered your life hasn't got any meaning. Sorry {}.".format(playername))
        time.sleep(2)
        while True:
            if choice3 == "1":
                while True:
                    if choice8 == "4":
                        time.sleep(2)
                        print("You not only have a damn dart in your eye, but you have a brand new lung cancer from the cigarette you accepted. I don't envy you.")
                        break
                    else:
                        print("While thinking, you are start to cough. You got a lung cancer from that cigarette you accepted. Your life is in ruins.")
                        time.sleep(2)
                        print("GAME OVER!")
                        print()
                        exit()
            else:
                break
    elif choice10 == "3":
        time.sleep(2)
        print("You start playing and time passes by. You didn't do your assignment on time. Imi is now sad.")
        time.sleep(2)
    elif choice10 == "4":
        time.sleep(2)
        print("{}! Quit acting like a pussy!".format(playername))
        time.sleep(2)
    elif choice10 == "5":
        time.sleep(2)
        print("Plot twist: {}, you are a penguin. You were a penguin all along. Accept the truth.".format(playername))
        time.sleep(2)
        break
    else:
        time.sleep(2)
        print("Why did you entered '{}' ? Enter the number of the choosen option!\n".format(choice10))
print()
print("But something is not right. Why are you a penguin?")
time.sleep(2)
print("Of course! This was just a dream!")
time.sleep(2)
print("You wake up. You are tired and of course miserable. {}, you should start going to Codecool, because you wil late!".format(playername))
time.sleep(2)
print()
input("Press ENTER to continue...")
print()
time.sleep(2)
print("YOU WON")
time.sleep(2)
print("Thanks for playing {}!".format(playername))
time.sleep(2)
print("All credit goes to Tibi and Zoli.")
time.sleep(2)
print(".")
time.sleep(2)
print(".")
time.sleep(2)
print(".")
time.sleep(2)
print("Penguin.")
print()
print()
exit()


        
        


    
        

