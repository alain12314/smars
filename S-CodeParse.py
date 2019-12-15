"""
S-code Parser
"""

from smars_library.smars_library import SmarsRobot, Leg
import smars_library.smars_library as sl
import time

def readLine(line):

    sm = SmarsRobot()
    sm.setname("Quaddy")
    sm.type = "Quad"

    if line[0] == 's101': # Move Forward
        sm.walkforward(100)
    if line[0] == 's102': # Move Backward
        sm.walkbackward(100)
    if line[0] == 's103': # Turn left
        sm.turnleft()
    if line[0] == 's104': # Turn right
        sm.turnright()
    if line[0] == 's155': # Stand Up
        sm.stand()
    if line[0] == 's156': # Sit down
        sm.sit()
    if line[0] == 's157': # Clap
        print("line count: ", len(line))
        if len(line) <= 1:
            clap_count = 3
        else:
            clap_count = int(line[1]) # convert str to int
        sm.clap(clap_count)
    if line[0] == 's158': # Wiggle
        print("line count:", len(line))
        if len(line) <= 1:
            wiggle_count = 3
        else:
            wiggle_count = int(line[1]) # convert str to int
        sm.wiggle(wiggle_count)
# Main
keywords = ""
while keywords != "quit":

    key = input("# ")
    keywords = key.split()

    for items in keywords:
        print(items)

    readLine(keywords)
