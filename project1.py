#!/usr/bin/python3

print("Which Lanturn Corp do you align with?")
color = ["red", "blue", "green", "yellow","orange", "indigo", "violet"]
ideology = ['Needs saving', 'Is terrifying and filled with evil','Is beautiful and filled with good']
perception = ['Reliable','What friends?', 'Protective', 'Supportive']
happiness = ['Good People', 'A good fight','Happiness is a lie', 'I can find joy in all things']
motivation = ['For my fellow Lanterns','For the safety of the galaxy', 'For victory', 'Because no one else will']
dislikes = ['Ignorance', 'Bullies', 'Arrogance', 'Selfishness']
corps = ['redrage', 'orangeavarice', 'yellowfear', 'greenwillpower', 'bluehope', 'indigocompassion', 'violetlove']
redrage = 0
orangeavarice = 0
yellowfear = 0
greenwillpower = 0
bluehope = 0
indigocompassion = 0
violetlove = 0

answer = input ("What is your favorite color? red, blue, green, yellow, orange, indigo, or violet\n")
if answer == 'red':
    redrage += 1
if answer == 'blue':
    bluehope += 1
if answer == 'green':
    greenwillpower += 1
if answer == 'yellow': 
    yellowfear += 1
if answer == 'orange':
    orangeavarice += 1
if answer == 'indigo':
    indigocompassion += 1
if answer == 'violet':
    violetlove += 1

answer = input ("The universe... Is beautiful and filled with good, Is terrifying and filled with evil, or Needs Saving\n")
if answer == 'Is beautiful and filled with good':
    violetlove += 1
    indigocompassion += 1
if answer == 'Is terrifying and filled with evil':
    redrage += 1
    yellowfear += 1
    orangeavarice =+ 1
if answer == 'Needs Saving':
    bluehope += 1
    greenwillpower += 1

answer = input ("What makes your happy? Good people, A good fight, Happiness is a lie, I can find joy in all things\n")
if answer == 'Good people':


