class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        finalstring = []
        kelvin = celsius + 273.15
        Farenheit = (celsius * 1.80) + 32.00
        finalstring.append(kelvin)
        finalstring.append(Farenheit)
        return finalstring
