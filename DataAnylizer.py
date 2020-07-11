import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb 
class Information:
    def __init__(self, data):
        self.data=data
    
    
    def printInfo(self):
        print('The first 5 elements of the data')
        print(self.data.head(5))
        print()
        print("Nb Columns: ", self.data.shape[1])
        print("Nb Records: ", self.data.shape[0])
        print("Nb records null:", self.data.isnull().sum().sum())
        print()
        print("Nb records null by columns:")
        print(self.data.isnull().sum())
    
    def printDesc(self):
        print(self.data.describe())
    
    def printDescCol(self, colName):
        print(self.data[colName].describe())

class PreProcessing:
    def __init__(self, data):
        self.data=data
    
    #Delete the columns that contains NaN, inplace is we want to update data
    def delNAbyCol(self, inplace):
        return self.data.dropna(axis=1, inplace=inplace)
    
    def delNAbyRow(self, inplace):
        return self.data.dropna(axis=0, inplace=inplace)
    
    # fill the NaN data with using 'strategy by row
    def fillnaStrategyRow(self, strategy):
        if strategy == 'linear':
            return self.data.interpolate(method='linear', axis=0) 
        return self.data.fillna(method=strategy, axis=0)
    
     # fill the NaN data with using 'strategy by columns
    def fillnaStrategyCol(self, strategy):
        if strategy == 'linear':
            return self.data.interpolate(method='linear', axis=1) 
        return self.data.fillna(method=strategy, axis=1)

class Visulizer:
    def __init__(self, data, bins):
        self.data=data
        self.bins = bins
    
    
    def drawHist(self, colName):
        if self.bins == None:
            plt.hist(data=self.data, x=colName)
        else:
            plt.hist(data=self.data, x=colName, bins=self.bins)
