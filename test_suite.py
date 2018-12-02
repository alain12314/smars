import unittest
from SMARS_Library import leg
import SMARS_Library as sl
from SMARS_Library import set_servo_pulse

class setServoPulseTestCase(unittest.TestCase):
    """ tests setServoPulse """

    def test_setServoPulseChannelLessThan15(self):
        for channel in range(0,16):
            self.assertTrue(set_servo_pulse(channel,10))

    def test_setServoPulseIsNumberBetween0And4096(self):
        self.assertTrue(set_servo_pulse(0,0))
        self.assertTrue(set_servo_pulse(0,4096))
        self.assertTrue(set_servo_pulse(0,2000))
        self.assertFalse(set_servo_pulse(0,4097))

    def test_setAngle(self):
        legTest = leg()
        self.assertTrue(legTest.setAngle(0))
        self.assertTrue(legTest.setAngle(180))
        self.assertFalse(legTest.setAngle(181))

if __name__ == '__main__':
    unittest.main()
