from random import choice
starting = "enter from the choices"
prompt = "Do you want to play more? (y/n)"
values = ["rock", "paper", "scissor"]

def check_response(response):
    if response not in values:
        again = True
    else:
        again = False
    return again 

def check_condition(response):
    if response == 'rock' and value == 'scissor' or response == 'scissor' and value == 'paper' or response == 'paper' and value == 'rock':
        print("I chose ",value," You won!")
    else:
        print("I chose",value," ,I won!")

def main_fun():
    while True:
        global value
        value = choice(values)
        response = input('Enter rock, paper or scissor?\n:> ').lower()
        result = check_response(response)
        if result:
            print(starting)
            continue
        else:
            check_condition(response)

        if try_again(prompt):
            continue
        else:
            break

def try_again(prompt):
    while True:
        print(prompt)
        response = input(":> ").lower().strip()
        if response not in ('y', 'n'):
            continue
        else:
            if response == 'y':
                ret_value = True
            else:
                ret_value = False
            break

    return ret_value


main_fun()