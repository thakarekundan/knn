import pandas as pd
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import  numpy as np
dataframe = pd.read_csv('african_crises.csv')
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv('dataset-all-categorical.csv')
lbl = LabelEncoder()
df =df.apply(lbl.fit_transform)



dataframe.columns = ['country','year','systemic_crisis','exch_usd','gdp_weighted_default','inflation_annual_cpi','independence','currency_crises','inflation_crises','banking_crisis']


dataframe.country.replace(('Algeria','Angola','Central African Republic','Ivory Coast','Egypt','Kenya','Mauritius','Morocco','Nigeria','South Africa','Tunisia','Zambia','Zimbabwe'),(1,2,3,4,5,6,7,8,9,10,11,12,13), inplace=True)



dataframe.banking_crisis.replace(('no_crisis','crisis'),(1,0), inplace=True)



dataset = dataframe.values


X = dataset[:,:9]
Y = np.asarray(dataset[:,9], dtype="S9")

# Split Data to train and Test
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.2)


# create model
knn = KNeighborsClassifier()

knn.fit(X_Train, Y_Train)
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', metric_params=None, n_jobs=1, n_neighbors=5, p=2, weights='uniform')

predictions = knn.predict(X_Test)

score = accuracy_score(Y_Test, predictions)
score=score*100

print("|| library accuracy_score -: "+"{:.2f}".format(score),"% ||")


