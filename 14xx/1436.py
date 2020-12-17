class Solution(object):
    def destCity(self, paths):
        cityFrom = set()
        cityTo = set()
        for path in paths: 
            cityFrom.add(path[0])
            cityTo.add(path[1])
        for city in cityTo:
            if city not in cityFrom:
                return city