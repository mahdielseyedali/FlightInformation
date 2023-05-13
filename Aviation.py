# Desc: The three python files (Flight.py, Airport.py, and Airline.py) are used track flight codes, airports, origins and destinations.

from Flight import *
from Airport import *
import os

class Aviation:

    # Constructor for Aviation class
    def __init__(self):
        self._allAirports = []
        self._allFlights = {}
        self._allCountries = {}

    # 3 getter methods and 3 setter methods
    def getAllAirports(self):
        return self._allAirports

    def getAllFlights(self):
        return self._allFlights

    def getAllCountries(self):
        return self._allCountries
    
    def setAllAirports(self, airports):
        self._allAirports = airports

    def setAllFlights(self, flights):
        self._allFlights = flights

    def setAllCountries(self, countries):
        self._allCountries = countries
    
    # Can read and return data from the data files
    def loadData(self, airportFile, flightFile, countriesFile):
        # Load countries
        try:
            with open(countriesFile, 'r', encoding='utf8') as f:
                for line in f:
                    country, continent = [x.strip() for x in line.split(',')]
                    self._allCountries[country] = continent
        except:
            return False

        # Load airports
        try:
            with open(airportFile, 'r', encoding='utf8') as f:
                for line in f:
                    code,  country, city = [x.strip() for x in line.split(',')]
                    airport = Airport(code, city, country, self._allCountries[country])
                    self._allAirports.append(airport)

        except:
            return False

        # Load flights
        try:

            with open(flightFile, 'r', encoding='utf8') as f:
                for line in f:
                    flightNum, origCode, destCode = [x.strip() for x in line.split(',')]
                    flight = Flight(flightNum, self.getAirportByCode(origCode), self.getAirportByCode(destCode))
                    self._allFlights[flightNum] = flight
        
            # Fix self._allFlights
            all_flights = {}
            for flight_num, flight_obj in self._allFlights.items():
                all_flights[flight_num] = [flight_obj]

            self._allFlights = all_flights
          

        except:
            return False
    
        return True
    
    def getAirportByCode(self, code):
        for airport in self._allAirports:
            if airport.getCode() == code:
                return airport
        return -1

    # The following find methods will find flights, airports, and countries specified by the user
    def findAllCityFlights(self, city):
        flights = []
        for flight_list in self._allFlights.values():
            for flight in flight_list:
                if flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city:
                    flights.append(flight)
        return flights

    
    def findFlightByNo(self, flightNo):
        flight= []
        for flight_list in self._allFlights.values():
            for flight in flight_list:
                if flight.getFlightNumber() == flightNo:
                    return flight
        return -1
    
    
    def findAllCountryFlights(self, country):
        flights = []
        for flight_list in self._allFlights.values():
            for flight in flight_list:
                origin_airport = flight.getOrigin()
                destination_airport = flight.getDestination()
                if origin_airport.getCountry() == country or destination_airport.getCountry() == country:
                    flights.append(flight)
        return flights

    
    def findFlightBetween(self, origin_airport, destination_airport):
        all_flights = self._allFlights.values()
        connection_flights = set()
        flight2 = []
        for flightlist in all_flights:
            for flight in flightlist:
                if flight.getOrigin() == origin_airport and flight.getDestination() == destination_airport:
                    return f"Direct Flight({flight._flightNo}): {flight._origAirport._code} to {flight._destAirport._code}"
                else:
                    #print("flight origin:", flight.getOrigin(), "flight destination:", flight.getDestination(), "origin_airport:", origin_airport, "destination_airport:", destination_airport)
                    if flight.getOrigin() == origin_airport and flight.getDestination() != destination_airport:
                        for flight2 in all_flights:  
                            #print(flight2)                     
                            if isinstance(flight2, Flight) and flight2.getOrigin() == flight.getDestination() and flight2.getDestination() == destination_airport:
                                connection_flights.add((flight, flight2))
            if connection_flights:
                # Format connection flights as a string
                return "Connecting Flights:\n" + "\n".join([f"Flight {i+1}: {f1._origAirport._code} to {f1._destAirport._code} ({f1._flightNo}), {f2._origAirport._code} to {f2._destAirport._code} ({f2._flightNo})" for i, (f1, f2) in enumerate(connection_flights)])
        
        return -1


    def findReturnFlight(self, firstFlight):
        for flight_list in self._allFlights.values():
            for flight in flight_list:
                if flight.getOrigin() == firstFlight.getDestination() and flight.getDestination() == firstFlight.getOrigin():
                    return flight
        return -1
    
    def findFlightsAcross(self, ocean):
        flights = set()
        redzone = ["Asia", "Australia"]
        greenzone = ["South America", "North America"] 
        bluezone = ["Europe", "Africa"]
        
        for flightlist in self._allFlights.values():
            for flight in flightlist:
                sameZone = False
                if flight.getOrigin().getContinent() != flight.getDestination().getContinent():
                            
                    if flight.getOrigin().getContinent() in redzone and flight.getDestination().getContinent()  in redzone: 
                        sameZone = True
                                
                    if flight.getOrigin().getContinent() in greenzone and flight.getDestination().getContinent()  in greenzone:
                        sameZone = True
                    
                    if flight.getOrigin().getContinent() in bluezone and flight.getDestination().getContinent()  in bluezone:
                        sameZone = True 
                    
                    if sameZone == False:                        
                        if ocean == "Atlantic":                        
                            if (flight.getOrigin().getContinent() in greenzone or flight.getOrigin().getContinent() in bluezone) and (flight.getDestination().getContinent() in greenzone or flight.getDestination().getContinent() in bluezone):
                                flights.add(flight.getFlightNumber())          
                                
                        elif ocean == "Pacific":
                            if (flight.getOrigin().getContinent() in redzone or flight.getOrigin().getContinent() in greenzone) and (flight.getDestination().getContinent() in redzone or flight.getDestination().getContinent() in greenzone):
                                flights.add(flight.getFlightNumber())
        return flights