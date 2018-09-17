import SMARS_Library
from SMARS_Library import SmarsRobot
import time

sm = SmarsRobot()

#  Telling sm to Sit

print "SMARS QUAD TEST PROGRAM"
sm.type = "quad"

for n in sm.legs:
    print n.name
    n.down()
    time.sleep(1)
    key = raw_input("Press any key to sit down")

sm.leg_reset()

key = raw_input("Press any key to sit down")
sm.sit()

key = raw_input("Press any key to stand")
sm.stand()
