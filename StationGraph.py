import csv

class Station:
    def __init__(self, ID, latitude, longitude, name):
        self.ID = ID
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.name = name
        self.neighbours = []
        
    def AddNeighbour(self, neighbourID, line, time):
        neighbour = [neighbourID, line, int(time)]
        self.neighbours.append(neighbour)

    def GetID(self):
        return str(self.ID)
    
    def GetArrayForGraph(self):
        entry = []
        entry.append(self.name)
        entry.append([self.latitude, self.longitude])
        for neighbour in self.neighbours:
            entry.append(neighbour)
        return entry

def getGraph():
    #This is the dictonary of all the stations
    stations = {}
    with open("london.stations.csv", "r") as StationFile:
        for row in csv.reader(StationFile):
            if row[0] == "id":
                print("skipping label line in station file")
                continue
     
            currentStation = Station(row[0], row[1], row[2], row[3])
            stations[currentStation.GetID()] = currentStation

    with open("london.connections.csv", "r") as ConnectionFile:
        for row in csv.reader(ConnectionFile):
            if row[0] == "station1":
                print("skipping label line in connection file")
                continue
            #The first station in the connection
            station1ID = row[0]
            #The second station in the connection
            station2ID = row[1]
            line = row[2]
            time = row[3]
            station1 = stations[station1ID]
            station1.AddNeighbour(station2ID, line, time)
            station2 = stations[station2ID]
            station2.AddNeighbour(station1ID, line, time)
            
    graph = {}
    # go through all stations and build the graph
    for stationKey in stations:
        currentStation = stations[stationKey]
        graph[currentStation.GetID()] = currentStation.GetArrayForGraph()

    return graph