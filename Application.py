from matplotlib.finance import quotes_historical_yahoo_ohlc
from AutoRegression import AutoRegression
from CandleStickChart import CandleStickChart
from ValuesParser import ValuesParser

class Application: 
    def __init__(self):
        company = "GOOG"
        startDate = (1992, 1, 1)
        endDate = (2014, 10, 17)
        
        # First chart data
        quotes = quotes_historical_yahoo_ohlc(company, startDate, endDate)
        if len(quotes) == 0:
            raise SystemExit
        
        # Second chart data
        dates = ValuesParser.getValues(quotes, "date")
        openValues = ValuesParser.getValues(quotes, "open")
        closeValues = ValuesParser.getValues(quotes, "close")
        highValues = ValuesParser.getValues(quotes, "high")
        lowValues = ValuesParser.getValues(quotes, "low")
        volumeValues = ValuesParser.getValues(quotes, "volume")
        
        predictedOpenValues = AutoRegression.calculateEstimation(openValues, AutoRegression.calculateARCoefficients(openValues, 5))
        predictedCloseValues = AutoRegression.calculateEstimation(openValues, AutoRegression.calculateARCoefficients(closeValues, 5))
        predictedHighValues = AutoRegression.calculateEstimation(openValues, AutoRegression.calculateARCoefficients(highValues, 5))
        predictedLowValues = AutoRegression.calculateEstimation(openValues, AutoRegression.calculateARCoefficients(lowValues, 5))
        predictedVolumeValues = AutoRegression.calculateEstimation(openValues, AutoRegression.calculateARCoefficients(volumeValues, 5))
        
        predictedQuotes = ValuesParser.getQuotes(dates, predictedOpenValues, predictedCloseValues, predictedHighValues, predictedLowValues, predictedVolumeValues)
        
        """ L'algorithme utilisant les 5 premières valeurs pour en déduire les 5 suivantes,
         les 5 premières valeurs des prévisions sont fatalement nulles. Pour ne pas avoir
         le même résultat que le screenshot du mail, (l'échelle changeante à cause des valeurs nulles)
         j'ai copié les premières valeurs pour avoir une meilleure lisibilité """
        predictedQuotes[0:5] = quotes[0:5]
        
        # Charts
        CandleStickChart("Cotations", quotes)
        CandleStickChart("Prévisions", predictedQuotes)
        
Application()