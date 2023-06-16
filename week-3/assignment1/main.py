import pandas as pd
import datetime
import yfinance as yf

# Allow the full width of the dataframe to be displayed
pd.options.mode.chained_assignment = None
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', None)

def getStock(stkInput, dayInput):
    dt = datetime.date.today()
    dtPast = dt - datetime.timedelta(days=dayInput)

    # Call Yahoo finance to get stock data for the stock provided
    dfStock = yf.download(stkInput, start=dtPast, end=dt)
    # df = dfStock.iloc[:, 3:6]
    df = dfStock[['Close', 'Volume']]
    # % Volume change and fill NaN with 0
    df['Volume % Change'] = df['Volume'].pct_change().fillna(0)
    # %Close change and fill NaN with 0
    df['Close % Change'] = df['Close'].pct_change().fillna(0)
    # overall %change for Close and round to 3 decimal places
    overallCloseChange = round((df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0], 3)
    # overall %change for Volume and round to 3 decimal places
    overallVolumeChange = round((df['Volume'].iloc[-1] - df['Volume'].iloc[0]) / df['Volume'].iloc[0], 3)
    print(f'Daily Percent Change - {dtPast} to {dt} * {stkInput} *')
    print('******************************************************')
    print(df)
    print('\n------------------------------------------------------')
    print(f'Summary of Cumulative Change for {stkInput}')
    print('\n------------------------------------------------------')
    print(f'% Volume Change: {overallVolumeChange}')
    print(f'% Close Change: {overallCloseChange}')

def stockReportMenu():
    print('------------------------------------------------------')
    print('Stock Report Menu Options')
    print('------------------------------------------------------')
    print('1. Report changes for a stock')
    print('2. Quit')

def stockReport():
    stockReportMenu() 
    response = int(input('Enter your choice: '))
    if response == 1:
        stock = input('Please enter the stock symbol: ').upper()
        days = int(input('Please enter the number of days for the analysis: '))
        getStock(stock, days)
        print('Do you want to run another report?')
        reportAgain = input('Enter Y for yes or N for no: ').upper()
        if reportAgain == 'Y':
            stockReport()
        elif reportAgain == 'N':
            print('Goodbye!')
        else:
            print('Invalid choice. Please try again.')
            stockReport()
    elif response == 2:
        print('Goodbye!')
    else:
        print('Invalid choice. Please try again.')
        stockReport()

stockReport()