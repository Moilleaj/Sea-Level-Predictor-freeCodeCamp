import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  fig,ax=plt.subplots(figsize=(8,5))
  ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
  res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  x1=np.arange(df['Year'].min(),2051,1)
  ax.plot(x1, res1.intercept + res1.slope * x1)

    # Create second line of best fit
  df_new = df.copy
  df_new = df[df['Year'] >= 2000]
  res2 = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])
  x2=np.arange(2000,2051,1)
  ax.plot(x2, res2.intercept + res2.slope * x2)

    # Add labels and title
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
  ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()