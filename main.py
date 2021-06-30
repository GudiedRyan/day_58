import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

#counts all the entries
df.count()


# Max posts total
df.groupby('TAG').sum()

#Max months using
df.groupby('TAG').count()

#Grab a single entry:
df['DATE'][1]

#Convert the date column into datetime objects from strings
df.DATE = pd.to_datetime(df.DATE)
df.head()

# Pivot Example
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')

# Real Pivot
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')


# Fill NaN values with a 0
reshaped_df.fillna(0, inplace=True)

# Plotting popularity of Java over time
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)


# Rolling average graph

roll_df = reshaped_df.rolling(window=6).mean()
 
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)
 
plt.legend(fontsize=16)