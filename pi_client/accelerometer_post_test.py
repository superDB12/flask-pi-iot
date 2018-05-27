#Test the accelerometer code

import unittest
import accelerometer_post as ap


class test_accelerometer_post(unittest.TestCase):

    def setUp(self):
        return

    #test the host name list
    def test_get_ServerList(self):
        l = ap.get_ServerList()
        self.assertTrue(type(l) == type(list()))
        self.assertTrue(len(l) > 0)

    def test_servers(self):
        l = ap.get_valid_servers()
        self.assertTrue(len(l) > 0)




if __name__ == '__main__':
    unittest.main()



