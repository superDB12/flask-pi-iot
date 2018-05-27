#Test the accelerometer code

import unittest
import accelerometer_post as ap


class test_accelerometer_post(unittest.TestCase):

    def setUp(self):
        return

    #test the host name list
    def test_getServerList(self):
        l = ap.getServerList()
        self.assertTrue(len(l)>0


if __name__ == '__main__':
unittest.main()
