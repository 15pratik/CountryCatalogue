# Author : Pratik Padalia

import country

class CountryCatalogue(object, continentFile, dataFile):
    def __init__(self):
        self.cDictionary = [] #List
        self.countryCat = [] #List
        try:
            fileContinent = open(continentFile, "r")
        except IOError as err:
            # Error reading file. Quit
            print("Error, File not found!")
            quit()

        for line in fileContinent:
            # print(line)
            line = line.split(",")
            self.cDictionary[line[0]] = {line[1]}

        try:
            fileData = open(dataFile, "r")
        except IOError as err:
            # Error reading file. Quit
            print("Error, File not found!")
            quit()

        for line in fileData:
            # print(line)
            line = line.split("|")
            if cDictionary.has_key(line):
                addCountry = Country(currCountry[0], line[2], line[3], currCountry[1])
                self.countryCat.append(addCountry)

    def findCountry(name):
        for currCountry in self.countryCat:
            if currCountry.get_name() == name:
                return currCountry
        return NULL

    def setPopulationOfCountry(name, population):
        for currCountry in self.countryCat:
            if currCountry.get_name() == name:
                self.countryCat.remove(currCountry)
                currCountry.set_population(population)
                self.countryCat.append(currCountry)
                return True
        return False

    def setPopulationOfCountry(name, area):
        for currCountry in self.countryCat:
            if currCountry.get_name() == name:
                self.countryCat.remove(currCountry)
                currCountry.set_area(area)
                self.countryCat.append(currCountry)
                return True
        return False

    def addCountry(name, population, area, continent):
        if cDictionary.has_key(line):
            return False
        currCountry = Country(name, population, area, continent)
        self.cDictionary[name] = continent
        self.countryCat.append(currCountry)
        return True

    def deleteCountry(name):
        if cDictionary.has_key(line):
            for currCountry in self.countryCat:
                if currCountry.get_name == name:
                    self.countryCat.remove(currCountry)
                    break

    def printCountryCatalogue():
        for currCountry in self.countryCat:
            currCountry.__repr__()

    def getCountriesByContinent(continent):
        countries = []
        for currCountry in self.countryCat:
            if currCountry.get_continent() == continent:
                countries.append(currCountry)
        return countries

    def getCountriesByPopulation():
        sortedCountry = sorted(self.countryCat, key=lamda countryCat: countryCat.population, reverse=True)
        return [sortedCountry, sortedCountry.name]

    def getCountriesByArea():
        sortedCountry = sorted(self.countryCat, key=lamda countryCat: countryCat.area, reverse=True)
        return [sortedCountry, sortedCountry.name]

    def filterCountriesByPopDensity():
        sortedCountry = sorted(self.countryCat, key=lamda countryCat: countryCat.getPopDensity(), reverse=True)
        return [sortedCountry, sortedCountry.name]

    def saveCountryCatalogue(fileName):
        sortedCountry = sorted(self.countryCat, key=lamda countryCat: countryCat.name)
        