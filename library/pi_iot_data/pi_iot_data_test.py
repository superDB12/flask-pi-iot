# Test the data code

import unittest
import pi_iot_data as pid


class test_pi_iot_data(unittest.TestCase):

    def setUp(self):
        pass

    # test adding list items
    def test_add_reading(self):
        print("starting ADD readings test")
        # create instance of data object
        aPid = pid.pi_iot_data()

        # call data handler object and pass test data
        # (serialnumber, timestamp, x, y, z)
        aPid.add_reading('12356', '180603 105800', 2.0, 20.0, 2.0)

        # get number of entries
        n = aPid.get_number_readings()
        self.assertTrue(n == 1)

        aPid.add_reading('121212', '180603 114500', 3.0, 30.0, 3.0)

        # get number of entries
        n = aPid.get_number_readings()
        self.assertTrue(n == 2)

    # getting some readings
    def test_get_readings(self):
        print("starting GET readings test")
        # create instance of data object
        aPid = pid.pi_iot_data()

        # add readings to the instance
        aPid.add_reading('12356', '180603 105800', 2.0, 20.0, 2.0)
        aPid.add_reading('121212', '180603 114500', 3.0, 30.0, 3.0)

        # get number of entries
        n = aPid.get_number_readings()
        self.assertTrue(n == 2)


        # get readings
        gRead = aPid.get_readings()
        print(gRead)

        # test if the data is a list
        self.assertTrue(isinstance(gRead, list))


if __name__ == '__main__':
    print("starting tests")
    unittest.main()
