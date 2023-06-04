# Excercise 1
list = [1.3, 2.6, 8.9, 11.5, 14.8]
print(f"The array length is {str(len(list))}.")

for index in range(len(list)):
    print(f"index {index}: {list[index]}")

print("Here is the list again")

for item in list:
    print(item)

# Excercise 2
def showFruitList(fruitList):
    print("\n***DISPLAYING ARRAY CONTENTS***")
    for i in range(len(fruitList)):
        print(fruitList[i])
# Create array
fruit = ["apple"]

# Add items to array
fruit.append("pears")
fruit.insert(0, "plums")

# Sort array
fruit.sort()

# Show array contents
showFruitList(fruit)

# Excercise 3
moreFruits = ["bananas", "dates", "peaches"]
fruit.extend(moreFruits)
showFruitList(fruit)

# Excercise 4
import pandas as pd

dataset = {
    'firstName': ['Jonny', 'Holly', 'Nira'],
    'lastName': ['Sraub', 'Conway', 'Arora'],
    'grade':[85,95,91]

}

df = pd.DataFrame(dataset, columns=['firstName', 'lastName', 'grade'])
print(df)

# Excercise 5
import pandas as pd

dataset = {'Market': ['S&P500', 'Dow', 'Nikkei'],
           'Last': [2932.05, 26485.01, 21087.16]
           }

df = pd.DataFrame(dataset, columns=['Market', 'Last'])

change = [-21.51, -98.41, -453.83]
df['Change'] = change

percentageChange = [-0.73, -0.37, -2.11]
df['percentageChange'] = percentageChange

print(df)

# Excercise 6
for i in range(len(df)):
    print(df.loc[i]['Last'])

# Excercise 7
firstRow = df.loc[0]
print(firstRow)

# Excercise 8
# Market               S&P500
# Last                2932.05
# Change               -21.51
# percentageChange      -0.73

# Excercise 9

dataset = {'Market': ['S&P500', 'Dow', 'Nikkei'],
            'Last': [2932.05, 26485.01, 21087.16]
            }

df1 = pd.DataFrame(dataset, columns=['Market', 'Last'])

dataset2 = {'Market': ['Hang Seng', 'DAX'],
            'Last': [26918.58, 11872.44]}

df2 = pd.DataFrame(dataset2, columns=['Market', 'Last'])

dataset3 = {'Market':['FTSE100'],
            'Last':[7407.06]}

df3 = pd.DataFrame(dataset3, columns=['Market', 'Last'])

df = pd.concat([df1, df2, df3]).reset_index(drop=True)

print(df)   

# Excercise 10
dataset = {'Market': ['S&P500', 'Dow'],
            'Last': [2932.05, 26485.01]
        }
df1 = pd.DataFrame(dataset, columns=['Market', 'Last'])

stockDictionary = {'Market': ['Nikkei'],
                    'Last': [21087.16]}
df2 = pd.DataFrame(stockDictionary, columns=['Market', 'Last'])

stockDictionary2 = {'Market': ['DAX'],
                    'Last': [11872.44]
                    }
df3 = pd.DataFrame(stockDictionary2, columns=['Market', 'Last'])

df = pd.concat([df1, df2, df3]).reset_index(drop=True)

# Excercise 11
# 5 is the default number of rows to display
df.head()
df.tail()

# Excercise 12
import pandas as pd

path = 'datasets/bodyfat.txt'
df = pd.read_csv(path, skiprows=1, 
                 sep='\t',
                 names=['Density', 'BodyFat', 'Age', 'Weight', 'Height', 'Neck', 'Chest', 'Abdomen', 'Hip', 'Thigh', 'Knee', 'Ankle', 'Biceps', 'Forearm', 'Wrist']
                 )
# Show all columns
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)

# Show first 2 rows
print(df.head(2))

# Show last 2 rows
print(df.tail(2))

# Data types of each column
print(df.dtypes)

# Statistical summary of each column
print(df.describe().round(2))

# Excercise 13
df2 = df[['Height', 'Weight', 'BodyFat']]

print(df2.head(2))