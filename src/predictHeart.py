import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

mydata = pd.read_csv("../CSV/heart.csv")
mydata.head()

# 2. prepare the input variable x, and target output y
z,t = mydata.drop(['target','age', 'trestbps', 'chol', 'fbs', 'thalach', 'thal','sex'],axis=1), mydata['target']
z_train,z_test,t_train,t_test = train_test_split(z,t,test_size = 0.3,random_state = 1)

model = LogisticRegression()
rfe = RFE(model, 7)
fit = rfe.fit(z_train, t_train)
#print("Num Features: %s" % (fit.n_features_))
#print("Selected Features: %s" % (fit.support_))
#print("Feature Ranking: %s" % (fit.ranking_))

def kneighbor_heart(entry):
    knn = KNeighborsClassifier(n_neighbors = 3)
    prediction = knn.predict(entry)
  #  print('KNN for HeartDisease accuracy is: ',knn.score(z_test,t_test)) # accuracy
    return prediction 
    
def naivebayes_heart(entry):
    nb = GaussianNB()
    nb.fit(z_train,t_train)
    prediction_nb= nb.predict(entry)
   # print('For HeartDisease NB accuracy is: ',nb.score(z_test,t_test)) # accuracy
    return prediction_nb


def svc_heart(entry):
    svm = SVC()
    svm.fit(z_train, t_train)
    prediction_svm=svm.predict(entry)
  #  print(' SVM accuracy is: ',svm.score(z_test,t_test)) # accuracy
    return prediction_svm

 
def randomforest_heart(entry):
    clf_rf_2 = RandomForestClassifier()      
    clr_rf_2 = clf_rf_2.fit(z_train,t_train)
    prediction_clf_rf_2=clf_rf_2.predict(entry)
 #   print('For HeartDisease RandomForest accuracy is: ',clf_rf_2.score(z_test, t_test))
    return prediction_clf_rf_2
              
def decisiontree_heart(entry):                
    dtree = DecisionTreeClassifier()
    dtree.fit(z_train,t_train)
    prediction_dt = dtree.predict(entry)
   # print('For HeartDisease Decision tree accuracy is: ',dtree.score(z_test,t_test)) # accuracy
    return prediction_dt