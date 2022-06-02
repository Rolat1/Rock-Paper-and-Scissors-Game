import random

options= ['R','P', 'S']

def selection():
    global user_option, cpu_option
    user_option= input('Pick an option between "R" for Rock, "P" for Paper or "S" for Scissors: ')
    while(user_option not in options):
        print("Error: Invalid input")
        user_option= input('Pick an option between "R" for Rock, "P" for Paper or "S" for Scissors: ')

    cpu_option= random.choice(options)
    options_dic= {'R':'Rock', 'P':'Paper', 'S':'Scissors'}

    print('Player (%s): CPU (%s)' %(options_dic.get(user_option), options_dic.get(cpu_option)) )

selection()
while(user_option == cpu_option):
    print ("No winner, Try again")
    selection()

if ((user_option=='S' and cpu_option=='R') or (user_option=='R' and cpu_option=='P') or (user_option=='P' and cpu_option=='S') ):
    print("You lose")

else:
    print("You won")
