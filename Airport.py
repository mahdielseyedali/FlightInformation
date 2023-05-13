# Desc: The three python files (Flight.py, Airport.py, and Airline.py) are used track flight codes, airports, origins and destinations.

class Airport:
    # Constructor for Airport class
    def __init__(self,code,city,country,continent):
        self._code = code
        self._city = city
        self._country = country
        self._continent = continent

    # return a string representation of the object
    def __repr__(self):
        return f"{self._code} ({self._city}, {self._country})"
    
    # get the airport code, city, country and continent
    def getCode(self):
        return self._code
    
    def getCity(self):
        return self._city
    
    def getCountry(self):
        return self._country
    
    def getContinent(self):
        return self._continent
    
    # set the airport code, city, country and continent
    def setCity(self,city):
        self._city = city

    def setCountry(self,country):
        self._country = country

    def setContinent(self,continent):
        self._continent = continent