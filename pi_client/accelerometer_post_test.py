#Test the accelerometer code

import unittest
import accelerometer_post as ap


class test_accelerometer_post(unittest.TestCase):

    def setUp(self):
        return

    #test the host name list
    def test_get_ServerList(self):
        l = ap.get_ServerList()
        self.assertTrue(len(l)>0)

    def test_servers(self):
        ap.test_servers()




if __name__ == '__main__':
    unittest.main()



