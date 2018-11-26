"""
S-code Parser
"""

import SMARS_Library as sl
from SMARS_Library import SmarsRobot
from SMARS_Library import leg
import time

sm = SmarsRobot()
sm.setName("Quaddy")
sm.type = "Quad"

def readLine(self, line):
    if line[1] == 's101': # Move Forward
        sm.walkForward(100)
    if line[1] == 's102': # Move Backward
        sm.walkBackward(100)
    if line[1] == 's103': # Turn left
        sm.turnLeft()
    if line[1] == 's104': # Turn right
        sm.turnRight()
    
