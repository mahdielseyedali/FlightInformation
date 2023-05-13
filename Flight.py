# Desc: The three python files (Flight.py, Airport.py, and Airline.py) are used track flight codes, airports, origins and destinations.

import re
from Airport import *

# Flight class
class Flight:
    # Constructor for Flight class
    def __init__(self,flightNo,origAirport,destAirport):
        if not isinstance(origAirport,Airport) or not isinstance(destAirport,Airport):
           raise TypeError("The origin and destination must be Airport objects")
        if not isinstance(flightNo,str) or not re.match("^[A-Z]{3}[0-9]{3}$", flightNo):
            raise TypeError("The flight number format is incorrect")
        self._flightNo = flightNo
        self._origAirport = origAirport
        self._destAirport = destAirport
    # Return a string representation of the object
    def __repr__(self):
        if self.isDomesticFlight():
            flight_type = "domestic"
        else:
            flight_type = "international"
        return f"Flight({self._flightNo}): {self._origAirport._city} -> {self._destAirport._city} [{flight_type}]"
    
    # Compare two flights
    def __eq__(self,other):
        
        if isinstance(other,Flight):
            if self._origAirport == other._origAirport or self._destAirport == other._destAirport:
                return True
            else:
                return False    

    # Get the flight number, origin, destination and flight type
    def getFlightNumber(self):
        return self._flightNo
    
    def getOrigin(self):
        return self._origAirport
    
    def getDestination(self):
        return self._destAirport
    
    # Set the flight number, origin, destination and flight type
    def isDomesticFlight(self):
        return self._origAirport._country == self._destAirport._country

    def setOrigin(self,origin):
        self._origAirport = origin

    def setDestination(self,destination):
        self._destAirport = destination