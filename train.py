import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pickle

#loading the dataset
data=pd.read_csv("personality_dataset.csv")
data=pd.DataFrame(data)

#Encoding the data

Encoder=LabelEncoder()
data['Stage_fear']=Encoder.fit_transform(data['Stage_fear'])
data['Drained_after_socializing']=Encoder.fit_transform(data['Drained_after_socializing'])
data['Personality']=Encoder.fit_transform(data['Personality'])


#spliting the data into Two parts
x=data.iloc[:,:-1]
y=data['Personality']

#spliting the data into traning and testing

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#traning model                                                  
model=KNeighborsClassifier(n_neighbors=20,metric='euclidean')
                                                                                                                                
model.fit(x_train,y_train)                                       
                                                                 
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
