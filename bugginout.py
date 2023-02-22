#!/usr/bin/python3
# """Just a lil' warmup!"""

name= input("What is your name?\n>")
num= input("Pick a number between 1 and 3\n>")
num= int(num)
num= num - 1


adj_list= ["stupendous","splendiferous","magnificent"]
adj= adj_list[num]

# these prints are for debugging purposes, you may delete them when you're ready
print(name)
print(adj)

# FINAL PART OF CHALLENGE:
# USE THE name AND adj VARIABLES TO PRINT THE FOLLOWING:
# "Hello <name>! Have a <adj> Valentine's Day!
print("Hello, ", name,"! Have a ", adj, " Valentines's Day!", sep=(""))
print(f"Hello, {name}! Have a {adj} Valentine's Day!")
