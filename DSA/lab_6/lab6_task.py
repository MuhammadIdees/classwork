import pandas as pd
import numpy as np
Diabetes=pd.read_csv('F:/8sem/DSA/lab_6/data.csv')
table1=np.mean(Diabetes,0)# finds out mean based on columns
table2=np.std(Diabetes,0)# finds out std deviation based on columns
print(table1)
print(table2)

inputData=Diabetes.iloc[:,:8] #creates dataframes based on columns 1 through 8
outputData=Diabetes.iloc[:,8] #creates sequence based on column 9
print(inputData.head())
print(outputData.head())

from sklearn.linear_model import LogisticRegression
logit1=LogisticRegression()
logit1.fit(inputData,outputData)

print('Score',logit1.score(inputData,outputData)) #defines how well the algorithm has performed


####Model performance
####Classification rate 'by hand'
##Correctly classified
print('CORRECTLY CLASSIFIED',np.mean(logit1.predict(inputData)==outputData))
##True positive
trueInput=Diabetes.loc[Diabetes['Outcome']==1].iloc[:,:8]
trueOutput=Diabetes.loc[Diabetes['Outcome']==1].iloc[:,8]
##True positive rate
print('TRUE POSITVE RATE',np.mean(logit1.predict(trueInput)==trueOutput))
##True negative
falseInput=Diabetes.loc[Diabetes['Outcome']==0].iloc[:,:8]
falseOutput=Diabetes.loc[Diabetes['Outcome']==0].iloc[:,8]
##True negative rate
print('TRUE NEGATIVE RATE',np.mean(logit1.predict(falseInput)==falseOutput))

##Real vs predicted plot
import matplotlib.pyplot as plt
plt.figure()
plt.scatter(inputData.iloc[:,1],inputData.iloc[:,5],c=logit1.predict_proba(inputData)[:,1],alpha=0.4)
plt.xlabel('Glucose level ')
plt.ylabel('BMI ')
plt.show()

plt.figure()
plt.scatter(inputData.iloc[:,1],inputData.iloc[:,5],c=outputData,alpha=0.4)
plt.xlabel('Glucose level ')
plt.ylabel('BMI ')
plt.show()
