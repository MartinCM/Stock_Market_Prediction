from numpy import linalg

class AutoRegression:
    def __init__(self):
        self.data = []
    def calculateARCoefficients(inputSeries, order):
        length = len(inputSeries)      
        coef = [0 for i in range(order)]
        mat = [[0 for i in range(order)] for j in range(order) ]
        
        for i in range(order-1, length-1):
            for j in range(order):
                coef[j] += inputSeries[i+1]*inputSeries[i-j]
                for k in range(order):
                    mat[j][k] += inputSeries[i-j]*inputSeries[i-k]
        
        for i in range(0, order):
            coef[i] /= (length - order)
            for j in range(i, order):
                mat[i][j] /= (length - order)
                mat[j][i] = mat [i][j]
                
        return linalg.solve(mat, coef)             
    def calculateEstimation(inputSeries, arCoefficients):
        estimation = [0 for i in range(len(inputSeries))]
        
        for i in range(len(arCoefficients), len(inputSeries)):
            est = 0
            for j in range(0, len(arCoefficients)):
                est += arCoefficients[j]*inputSeries[i-(j+1)]
            estimation[i] = est
        return estimation