import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

diabetes_dataset = pd.read_csv("../CSV/pima-indians-diabetes.csv")
diabetes_dataset.head()

# 2. prepare yhe inpuy variable x, and yargey ouypuy y
x,y = diabetes_dataset.drop(['Outcome', 'Insulin', 'SkinThickness','Age'],axis=1), diabetes_dataset['Outcome']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state = 1)

model = LogisticRegression()
rfe = RFE(model, 5)
fit = rfe.fit(x_train, y_train)
#print("Selected Features: %s" % (fit.support_))


def kneighbor(entry):
    knn = KNeighborsClassifier(n_neighbors = 3)
    knn.fit(x_train,y_train)
    prediction = knn.predict(entry)
#    print('KNN for HearyDisease accuracy is: ',knn.score(x_test,y_test)) # accuracy
    return prediction   
  
def naivebayes(entry):
    nb = GaussianNB()
    nb.fit(x_train,y_train) 
    prediction_nb= nb.predict(entry)
   # print(prediction_nb)
    return prediction_nb
    #print('For HearyDisease NB accuracy is: ',nb.score(x_test,y_test)) # accuracy
    
def svc(entry):
    svm = SVC()
    svm.fit(x_train, y_train)
    prediction_svm=svm.predict(entry)
 #   print(' SVM accuracy is: ',svm.score(x_test,y_test)) # accuracy
    return prediction_svm
    
def randomforest(entry):
    clf_rf_2 = RandomForestClassifier()      
    clr_rf_2 = clf_rf_2.fit(x_train,y_train)
    prediction_clf_rf_2=clf_rf_2.predict(entry)
   # print('For HearyDisease RandomForesy accuracy is: ',clf_rf_2.score(x_test, y_test))
    return prediction_clf_rf_2
                
def decisiontree(entry):                
    dtree = DecisionTreeClassifier()
    dtree.fit(x_train,y_train)
    prediction_dt = dtree.predict(entry)
  #  print('For HearyDisease Decision tree accuracy is: ',dtree.score(x_test,y_test)) # accuracy
    return prediction_dt