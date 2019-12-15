#Leg setup

# setup leg 1:

# from SMARS_Library import *
from smars_library.smars_library import SmarsRobot, Leg
import smars_library.smars_library

channel_number = 1
l1 = Leg(name="limb test", channel=channel_number,  leg_minangle=0, leg_maxangle=180, invert=False)
# l1.name = "left_leg_front"
# l1.channel = channel_number
# l1.leg_minAngle = 0
# l1.leg_maxAngle = 180
# l1.invert = False

def menu():
    """ display the main menu """
    print("Menu")
    print("----")
    print("")
    print("1) select channel")
    print("2) select angle")
    print("0) quit")
    print("")

channel_number = 0
def select_channel():
    global channel_number
    global l1
    print("Select Channel")
    print("--------------")
    print("")
    print("currently selected channel is:", channel_number)
    key = ""
    ch = 0
    #  need to make this loop exit once the channel number is selected and "q" pressed
    while key != "q":
        key = input("type channel number:, or q to return to the main menu")
        print(key)
        if key == "q":
            print("")
        else:
            ch = int(key)
            if ch >= 16:
                print("sorry that channel number is too high, needs to be between 0 and 15")
            else:
                channel_number = int(ch)
                l1.channel = channel_number
                l1.show()

angle = 0


def select_angle():
    """ change the current angle """
    global angle
    print("Select Angle")
    print("------------")
    print("")
    print("current angle is:", angle)

    # l1.setAngle(angle)
    key = ""
    while key != "q":
        key = input("Type angle to set servo to, or press q to exit")
        print(key)
        if key == "q":
            print("")
        else:
            # if raw_input ==
            # angle = angle + 10
            angle = int(key)
            l1.setangle(angle)
            print("current angle:", angle)

menu_key = ""
# show Menu until quit
while menu_key != "0":
    menu()
    print("current channel is:", l1.channel)
    print("current angle is:", angle)
    menu_key = input("enter number ")

    if menu_key == "1":
        select_channel()
    if menu_key == "2":
        select_angle()
    if menu_key == "0":
        print("Good bye!")
