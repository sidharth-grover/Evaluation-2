import pandas as pd
from pymongo import MongoClient

#client = MongoClient('localhost',27012)
#db = client['sidharth']
#collection = db['impatient']

df = pd.read_csv('temp.csv')

#df_dict = df.to_dict("records")
#collection.insert_many(df_dict)


#Q3
print('Q3')
q2 = df[(pd.to_datetime(df["Certification Date"],format = 'mixed' ) > pd.to_datetime('10-01-2011')) & (df["Ownership Type"] == 'Non-profit')]
print(q2[:5])

#Q4
print('Q4  providers belonging to BIRMINGHAM and Ownership Type= PROFIT')
q4 = df[(df["City/Town"] == 'BIRMINGHAM') & (df["Ownership Type"] == 'For profit')]
print(q4[:5])

#Q5
print('Q5 providers with ZIP codes in the range 85000-90000')
q5 = df[(df["ZIP Code"] >= 85000) & (df["ZIP Code"] <= 90000)]
print(q5[:5])


#Q6
print('Q6')
profit = df[df["Ownership Type"] == 'For profit'].shape[0]
non_profit = df[df["Ownership Type"] == 'Non-profit'].shape[0]
print('Number of profit providers:  ' , profit )
print('Number of non- profit providers:  ' , non_profit )


