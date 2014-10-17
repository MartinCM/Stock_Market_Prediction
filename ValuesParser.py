class ValuesParser:
    def __init__(self):
        self.data = []
    def getValues(inputSeries, name):
        order = -1
        if name == "date":
            order = 0
        elif name == "open":
            order = 1
        elif name == "close":
            order = 2
        elif name == "high":
            order = 3
        elif name == "low":
            order = 4
        elif name == "volume":
            order = 5
        if order == -1:
            raise SystemExit
            
        values = [0 for i in range(len(inputSeries))]
        for i in range(0, len(inputSeries)):
            values[i] = inputSeries[i][order]
            
        return values
    def getQuotes(dates, openValues, closeValues, highValues, lowValues, volumeValues):
        quotes = [[0 for i in range(0, 6)] for j in range(0, len(openValues)) ]
        for i in range(0, len(openValues)):
            quotes [i][0] = dates[i]
            quotes [i][1] = openValues[i]
            quotes [i][2] = closeValues[i]
            quotes [i][3] = highValues[i]
            quotes [i][4] = lowValues[i]
            quotes [i][5] = volumeValues[i]
        return quotes