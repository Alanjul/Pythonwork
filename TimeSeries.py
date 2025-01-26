"""Time series is asequence of values known as observations
associated with points in time
Examples include daily closing stock prices
temperature readings
change of position of plane in flight, annual crop yields, quartely
company profits
Simple linear regression make predictions using time series
we use observation ordered by year
multivariate time series looks at existing time series to make patterns
helping data analyst understand data
like looking for seasonality in data
Time series forecasting uses past data to predict future"""
#we gonna use univariate time series to make observation
#we will use simple linear regression  to make predictions
#by finding linear relationship between month and average temperature
#we will use independent and dependent variable
#month will be independent and temp will be dependent
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#converting the temperature to celcius
c = lambda f: 5/9*(f-32)

#tuple to display Fahrenheit temperature to their corresponding celsius temp
temp = [(f, c(f)) for f in range(0,101, 10)]
print(temp, ' ')
Fa = lambda ca: (9/5 *ca)+32
temp1 = [(ca, Fa(ca)) for ca in range(0,40, 5) ]
print(temp1, ' ')
temp_df = pd.DataFrame(temp, columns=['Fahrenheit', 'Celsius'])
temps_df = pd.DataFrame(temp1, columns=['Celsius', 'Fahrenheit'])
print("Tables showing degrees in Celsius converted to Fahrenheit")
print(temps_df)
axes = temps_df.plot(x='Celsius', y='Fahrenheit', style='-')