import numpy as np
import pandas as pd



import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

# The following csv file consists of details about 911 calls in a particular county downloaded from kaggle
df = pd.read_csv("911.csv")

print(df.info())

print(df.head())


# This gives the zip codes of top 5 places where most of the calls have been placed
print(df['zip'].value_counts().head(5))


# Top 5 townships for 911 calls
print(df['twp'].value_counts().head(5))


# Total no of different reasons for 911 calls
print(df['title'].nunique())


#  To create a new column in the dataframe. Parse through 'title' column in df. If found 'EMS' or 'FIRE' or 'TRAFFIC' the reason will be
# the relevant one.


def parseString(reason):
    if 'ems:' in reason.lower().split():
        return 'EMS'
    elif 'fire:' in reason.lower().split():
        return 'FIRE'
    elif 'traffic:' in reason.lower().split():
        return 'TRAFFIC'
    else:
        return np.nan

df['Reason'] = df['title'].apply(lambda x: parseString(x))


print(df['Reason'])


# See the total number of occurrences per value
print(df['Reason'].value_counts())




# Countplot 911 calls using seaborn

sns.countplot(x='Reason',data=df,palette='viridis')
plt.show()


# 'timeStamp' column has been changed from string to date and time
df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# Creating various columns and splitting the timeStamp column

df['Hour'] = df['timeStamp'].apply(lambda time:time.hour)
df['Month'] = df['timeStamp'].apply(lambda time:time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time:time.dayofweek)


# Since the values of column 'Day of Week' are from 0-6. We need to map them to Mon-tue

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

df['Day of Week'] = df['Day of Week'].map(dmap)



# Plotting the extacted data. Where the x-axis is 'Day of Week' and for each day its corresponding number of FIRE, EMS and TRAFFIC has been plotted
sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


# The same for 'Month'

sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


byMonth = df.groupby('Month').count()


byMonth['twp'].plot()
plt.show()

sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())
plt.show()


df['Date'] = df['timeStamp'].apply(lambda time: time.date())


df.groupby('Date').count()['twp'].plot()
plt.tight_layout()
plt.show()


df[df['Reason']=='TRAFFIC'].groupby('Date').count()['twp'].plot()
plt.title('TRAFFIC')
plt.tight_layout()
plt.show()


df[df['Reason']=='FIRE'].groupby('Date').count()['twp'].plot()
plt.title('FIRE')
plt.tight_layout()
plt.show()


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()
plt.show()
