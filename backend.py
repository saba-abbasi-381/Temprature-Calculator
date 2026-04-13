class TemperatureConverter:
    def __init__(self, temp):
        self.temp = temp

    def celsius_to_fahrenheit(self):
        fahrenheit = (self.temp * 9/5) + 32
        return fahrenheit
    
    def fahrenheit_to_celsius(self):
        celsius = (self.temp - 32) * 5/9
        return celsius
   

