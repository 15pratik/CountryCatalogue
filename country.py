class Country(object):
    def __init__(self, name, population, area, continent):
        self.name = name
        self.population = population
        self.area = area
        self.continent = continent
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_population(self):
        return self.population

    def set_population(self, population):
        self.population = population

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area

    def get_continent(self):
        return self.continent

    def set_continent(self, name):
        self.continent = continent

    def getPopDensity(self):
        return round(self.population/self.area, 2)

    def __repr__(self):
        return '%s (pop: %d, size: %f) in %s' % (self.name, self.population, self.area, self.continent)
