# This is a simple game based on teaching and getting commands from a bot
# I attempted to use functional programming to implement this :)

import webbrowser
import sys
import re

# Introduction
print("Hello, I am a basic AI robot!")
print("I am able to execute commands and also learn new ones")
print("For a list of known commands, type !help.")
print("To exit the program, type !exit.")

# Getting user input and processing it


def get_input(func, c_list):
    user_com = input("Please enter a command: \n")
    valid = re.match(r'!(.*)', user_com)
    if valid:
        user_com = user_com[1:]
        if user_com == "exit":
            print("Bye!")
            sys.exit()
        elif user_com == "help":
            print("Known commands:")
            for x in com_list:
                print("!" + x)
        elif user_com == "search":
            webbrowser.open('http://google.com')
        func(user_com, c_list)
    else:
        print("Invalid command format!")


def process(user_com, c_list):
    com = user_com
    if com in c_list:
        print(c_list[com])
    else:
        c_list[com] = input("How should I do that?")


com_list = {
    "greet": "Hello, my friend!",
    "sing": "Do re mi fa sol la si do...\ndo si la sol fa mi re do!",
    "exit": "Exit the program",
    "search": "Open a web page"
}

while True:
    get_input(process, com_list)
