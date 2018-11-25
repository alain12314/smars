"""
S-code Parser
"""

import SMARS_Library as sl
from SMARS_Library import SmarsRobot
from SMARS_Library import leg
import time

def readLine(line):

    sm = SmarsRobot()
    sm.setName("Quaddy")
    sm.type = "Quad"

    if line[0] == 's101': # Move Forward
        sm.walkForward(100)
    if line[0] == 's102': # Move Backward
        sm.walkBackward(100)
    if line[0] == 's103': # Turn left
        sm.turnLeft()
    if line[0] == 's104': # Turn right
        sm.turnRight()

# Main
keywords = ""
while keywords[0] <> "quit":

    key = raw_input("# ")
    keywords = key.split()
    
    for items in keywords:
        print items

    readLine(keywords)
