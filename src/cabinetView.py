from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import Tk
from tkinter import ttk
from tkinter import Menu
import tkinter.messagebox
import predictDiabetes
import predictHeart
import pandas as pd
fields = ('Pregnancies','Glucose','Blood pressure', 'Body mass index', 'Diabetes pedigree function')
fields2 = ('Chest pain type', 'Resting electrocardiographic', 'Exercise induced angina', 'Depression induced', 'Slope of the peak exercise', 'Nr. of major vessels')
fields3 = ('radius_mean','perimeter_mean','aera_mean','concavity_mean','radius_worst','perimeter_worst','area_worst','concave_points_worst')
def predict_heart_disease(entries, tab2):
    new_df = [];
    for entry in entries:
       if(entry[0]=='Depression induced'):
           new_df.append(float(entry[1].get()))
       else:
           new_df.append(int(entry[1].get()))
    test1=pd.DataFrame([new_df])
    if predictHeart.svc_heart(test1) == 1 :  
         label_4 = Label(tab2, text="Heart disease was detected", width=30,fg='brown', font=("comis sans ms", 11,"bold"))
         label_4.place(x=100,y=490)
    else: 
         label_4 = Label(tab2, text="Heart disease was not detected", width=30,fg='brown', font=("comis sans ms", 11,"bold"))
         label_4.place(x=100,y=490)
      
          
                      
def predict_diabet(entries,tab1):
    new_df = [];
    for entry in entries:
       if(entry[0]=='BMI' or entry[0]=='DiabetesPedigreeFunction'):
           new_df.append(float(entry[1].get()))
       else:
           new_df.append(int(entry[1].get()))
    test1=pd.DataFrame([new_df])
    print(test1)
    if predictDiabetes.naivebayes(test1) == 1 :  
         label_4 = Label(tab1, text="Diabetes was detected", width=20,fg='brown', font=("comis sans ms", 12,"bold"))
         label_4.place(x=140,y=450)
    else: 
         label_4 = Label(tab1, text="Diabetes was not detected", width=20,fg='brown', font=("comis sans ms", 12,"bold"))
         label_4.place(x=140,y=450)
   
def makeform(tab1, fields):
   entries = []
   pos_x_label = 80
   pos_y_label = 150
   pos_x_input = 260
   pos_y_input = 152
   for field in fields:
      nr=+1
      label_1 = Label(tab1, text=field ,width=20,font=("bold", 10))
      label_1.place(x=pos_x_label,y=pos_y_label)
      entry_1 = Entry(tab1)
      entry_1.place(x=pos_x_input,y=pos_y_input)
      pos_y_input += 50
      pos_y_label += 50
      entries.append((field, entry_1))
   return entries

def makeform2(tab2, fields2):
   entries = []
   pos_x_label = 80
   pos_y_label = 150
   pos_x_input = 260
   pos_y_input = 152
   for field in fields2:
      label = Label(tab2, text=field ,width=20,font=("bold", 10))
      label.place(x=pos_x_label,y=pos_y_label)
      entry = Entry(tab2)
      entry.place(x=pos_x_input,y=pos_y_input)
      pos_y_input += 50
      pos_y_label += 50
      entries.append((field, entry))
   return entries

def makeform3(tab3, fields3):
   entries = []
   pos_x_label = 80
   pos_y_label = 120
   pos_x_input = 260
   pos_y_input = 122
   for field in fields3:
      label = Label(tab3, text=field ,width=20,font=("bold", 10))
      label.place(x=pos_x_label,y=pos_y_label)
      entry = Entry(tab3)
      entry.place(x=pos_x_input,y=pos_y_input)
      pos_y_input += 50
      pos_y_label += 50
      entries.append((field, entry))
   return entries

def ext_1():
    exit()

    
def startCabinet():
    root = Tk()
    root.geometry('500x550')
    root.title("MedHelper")              # Add a title 
    tabControl = ttk.Notebook(root)          # Create Tab Control
    tab1 = ttk.Frame(tabControl)            # Create a tab 
    tabControl.add(tab1, text='Diabetes')      # Add the tab
    tabControl.pack(expand=1, fill="both")  # Pack to make visible
    tab2 = ttk.Frame(tabControl)            # Create a tab 
    tabControl.add(tab2, text='Heart Disease')      # Add the tab
    tab3 = ttk.Frame(tabControl)            # Create a tab 
    tabControl.add(tab3, text='Breast Cancer')      # Add the tab
    ents_diabetes = makeform(tab1, fields)
    ents_heart = makeform2(tab2, fields2)
    ents_cancer = makeform3(tab3,fields3)
    tab1.bind('<Return>', (lambda event, e=ents_diabetes: predict_diabet(e)))   
    tab2.bind('<Return>', (lambda event, e=ents_heart: predict_heart_disease(e))) 
    label_0 = Label(root, text="MedHelper",relief="solid",width=20,fg='brown', font=("comis sans ms", 19,"bold"))
    label_0.place(x=100,y=50)
    label_2 = Label(tab1, text="Diabetes Prediction",relief="solid", width=20,fg='brown', font=("comis sans ms", 12,"bold"))
    label_2.place(x=150,y=70)
    label_3 = Label(tab2, text="Heart Disease Prediction",relief="solid", width=20,fg='brown', font=("comis sans ms", 12,"bold"))
    label_3.place(x=150,y=70)
    label_4 = Label(tab3, text="Breast Cancer Prediction",relief="solid", width=20,fg='brown', font=("comis sans ms", 12,"bold"))
    label_4.place(x=150,y=70)
    menu = Menu(root)
    root.config(menu=menu)
    button_predict_diab=Button(tab1, text='Predict',width=30,bg='brown',fg='white',command=lambda e=ents_diabetes:predict_diabet(e,tab1)).place(x=130,y=420)
    button_predict_heart=Button(tab2, text='Predict',width=30,bg='brown',fg='white',command=lambda e=ents_heart:predict_heart_disease(e,tab2)).place(x=130,y=460)
    Button(tab3, text='Predict',width=30,bg='brown',fg='white').place(x=130,y=500)
    tabControl.pack(expand=1, fill="both") 
    root.mainloop()