import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 10))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lbf = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = x_pred*lbf.slope + lbf.intercept
    plt.plot(x_pred, y_pred)

    # Create second line of best fit
    df2 = df.loc[(df['Year'] >= 2000)]
    lbf2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(2000, 2051)])
    print(x_pred)
    y_pred = x_pred*lbf2.slope + lbf2.intercept
    plt.plot(x_pred, y_pred, 'r')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
