class Temperature:
    def __init__(self, kelvin=None, celsius=None,farenheit=None):
        values = [x for x in [kelvin, celsius, farenheit]if x]
        if len(values)<1:
            raise ValueError('Need arguement')
        if len(values)>1:
            raise ValueError('Only one arguement')
        if celsius is not None:
            self.kelvin = celsius + 273.15
        elif farenheit is not None:
            self.kelvin = (farenheit - 32) * 5/9 + 273.15
        else:
            self.kelvin=kelvin
            
        if  self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative')
    def __str__(self):
        return f'Temperature ={self.kelvin} Kelvins'