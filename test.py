# This is the SMARS Library test program
# it can be used to test each of the SMARS Library functions
#
# Written by Kevin McAleer
# September 2018

import SMARS_Library as sl
from SMARS_Library import SmarsRobot
from SMARS_Library import leg
import time

# create an instance of the Smars Robot class
sm = SmarsRobot()

# set the robot type to 'quad'
sm.type = "quad"

def continous_test(object):
    # print "channel number", channel_num

    while True:
        a = object.leg_minAngle
        b = object.leg_maxAngle
        while a <= object.leg_maxAngle:
            object.setAngle(a)
            print "angle:", a, "Channel:", object.channel, "name: ", object.name
            time.sleep(0.1)
            a = a + 1
        while b >= object.leg_minAngle:
            object.setAngle(b)
            print "angle:", b
            time.sleep(0.1)
            b = b - 1

def continous_feet_test():
    key = ""
    while key != "q":
        print "Continuous feet test"
        print "-------------------"
        print ""
        print "Select a foot to test:"
        print "1) Front Left Foot"
        print "2) Front Right Foot"
        print "3) Back Left Foot"
        print "4) Back Right Foot"
        print "q) Return to main menu"

        key = raw_input("Type 1-4 or q to return to main menu")
        if key == "1":
            # sm.legs[sl.left_foot_front].setAngle(sm.legs[sl.left_foot_front].leg_minAngle)
            continous_test(sm.feet[sl.left_foot_front])
        if key == "2":
            continous_test(sm.feet[sl.right_foot_front])
        if key == "3":
            continous_test(sm.feet[sl.left_foot_back])
        if key == "4":
            continous_test(sm.feet[sl.right_foot_back])


def continous_leg_test():
    print "Continuous leg test"
    print "-------------------"
    print ""
    print "Select a leg to test:"
    print "1) Front Left leg"
    print "2) Front Right leg"
    print "3) Back Left leg"
    print "4) Back Right leg"
    print "q) Return to main menu"

    key = raw_input("Type 1-4 or q to return to main menu")
    if key == "1":
        # sm.legs[sl.left_foot_front].setAngle(sm.legs[sl.left_foot_front].leg_minAngle)
        continous_test(sm.feet[sl.left_leg_front])
    if key == "2":
        continous_test(sm.feet[sl.right_leg_front])
    if key == "3":
        continous_test(sm.feet[sl.left_leg_back])
    if key == "4":
        continous_test(sm.feet[sl.right_leg_back])

def continuous_check():
    key = ""
    while key != "q":
        print "Continous servo check"
        print "---------------------"
        print ""
        print "Select a feet or limbs:"
        print "l) - select legs"
        print "f) - select feet"
        print "q) - return to main menu"

        key = raw_input("Type 'l', 'f' or 'q' ")
        if key == "q":
            print ""
        if key == "l":
            continous_leg_test()
        if key == "f":
            continous_feet_test()

def check_legs():
    # Check each leg

    key = ""
    print "Checking each leg - it should rotate to its full extent"
    key = raw_input("press a key to continue")

    print "front left leg"
    sm.legs[sl.left_leg_front].up()
    print sm.legs[sl.left_leg_front].name
    key = raw_input("press a key to continue")

    print "front right leg"
    sm.legs[sl.right_leg_front].up()
    print sm.legs[sl.right_leg_front].name
    key = raw_input("press a key to continue")

    print "back left leg"
    sm.legs[sl.left_leg_back].up()
    print sm.legs[sl.left_leg_back].name
    key = raw_input("press a key to continue")

    print "back right leg"
    sm.legs[sl.right_leg_back].up()
    print sm.legs[sl.right_leg_back].name
    key = raw_input("press a key to continue")

    print "Now moving each let to its default position."
    sm.legs[sl.left_leg_front].setDefault()
    sm.legs[sl.right_leg_front].setDefault()
    sm.legs[sl.left_leg_back].setDefault()
    sm.legs[sl.right_leg_back].setDefault()

    print "now moving each leg to its down position"

def check_feet():
    print "Checking each foot - each foot should rise up."
    key = raw_input("press a key to continue")

    print "front left foot"
    sm.feet[sl.left_foot_front].up()
    key = raw_input("press a key to continue")

    print "front right foot"
    sm.feet[sl.right_foot_front].up()
    key = raw_input("press a key to continue")

    print "back left foot"
    sm.feet[sl.left_foot_back].up()
    key = raw_input("press a key to continue")

    print "back right foot"
    sm.feet[sl.right_foot_back].up()
    key = raw_input("press a key to continue")

    print "Now moving each let to its default position."
    sm.feet[sl.left_foot_front].setDefault()
    sm.feet[sl.right_foot_front].setDefault()
    sm.feet[sl.left_foot_back].setDefault()
    sm.feet[sl.right_foot_back].setDefault()

# set the input choice to nothing
key = ""

# Display the main menu
while key != "q":
    print "SMARS QUAD TEST PROGRAM"
    print "-----------------------"
    print ""
    print "1) Set all limbs and feet to their default position"
    print "2) Set all feet to stand position"
    print "3) Set all feet to sit position"
    print "4) Check each limb is set correctly"
    print "5) continous servo check"

    key = raw_input("type an option, or type 'q' to quit ")
    if key == "1":
        for n in sm.legs:
            print n.name
            n.setDefault()
        for n in sm.feet:
            print n.name
            n.setDefault()
    if key == "2":
        for n in sm.feet:
            n.up()
    if key == "3":
        for n in sm.feet:
            n.down()
    if key == "4":
        check_legs()
        check_feet()
    if key == "5":
        continuous_check()

    if key == "q":
        print "Good bye!"
