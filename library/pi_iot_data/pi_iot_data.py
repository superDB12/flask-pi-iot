#A class to store data from the acccelerometer


class piIotData():


    def __init__(self):
        self._readings = []

    def add_reading(self, serialNumber, timeStamp, x, y, z):
        self._readings.append([serialNumber, timeStamp, x, y, z])


    def get_number_readings(self):
        n = len(self._readings)
        return n

    def get_readings(self):
        return self._readings
