import pandas as pd

class CountryChallenge:
    def __init__(self,csvUrl):
        self.dataframeComplete = pd.read_csv(csvUrl)
        self.dataframe = self.dataframeComplete[['LOCATION','Country', 'INDICATOR', 'Indicator', 'INEQUALITY', 'Inequality','Value']]
        self.indicatorsAvailable = self.dataframe['INDICATOR'].unique()
    
    def validateParams(self,param):
        isValid = True
        if param not in self.indicatorsAvailable:
            isValid = False
        return isValid
    
    def getAllCountries(self):
        indicator = self.indicatorsAvailable[0]
        return self.dataframe[ (self.dataframe['INDICATOR'] == indicator) & (self.dataframe['INEQUALITY'] == 'TOT') ]
    
    
    def filter(self,indicator,value):
        return self.dataframe[ (self.dataframe['INDICATOR'] == indicator) & (self.dataframe['INEQUALITY'] == 'TOT') & (self.dataframe['Value'] > float(value))]
    
    def isfloat(self,value):
      try:
        float(value)
        return True
      except ValueError:
        return False

