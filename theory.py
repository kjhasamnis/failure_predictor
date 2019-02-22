import pandas as pd
import math
import tkinter as tk

#Third GUI Window
def page3(c,f,d):
    global win
    win = tk.Tk()
    #modifying window
    win.title("Estimated Tool Life Data")
    win.geometry("500x500")
    
    tk.Label(win, text = "The predicted tool life is:\n").pack()
    theoritical(c,f,d) #Calling theoritical calculation function
    forest(c,f,d)    #Calling Random Forest Regressor
    neural(c,f,d)    #Calling Neural Network
    win.mainloop()
    
#Calculating theoritical tool life    
def theoritical(c,f,d):
    #Calculations based on research paper
    rhs = c * math.pow(f,0.6) * math.pow(d,0.15)
    tl = 1012/rhs
    n1 = 1/0.33
    Tool_life = math.pow(tl,n1)
    tk.Label(win,text=f"The Theoritical Tool Life is {Tool_life:0.2f} minutes\n").pack()
    

def forest(c,f,d):
    from sklearn.ensemble import RandomForestRegressor
    df = pd.read_csv('compiled_ab_constant.csv')
    forest = RandomForestRegressor(200)
    x = df.iloc[:,[1,2,3]]
    y = df.iloc[:,[-1]]
    
    #Splitting DataSet into Training and Testing Set
    from sklearn.model_selection import train_test_split
    x_train, x_test,y_train, y_test = train_test_split(x,y,test_size = 0.2, shuffle = True)
    #Initiating the Random Forest Regressor
    regr = RandomForestRegressor(max_depth = 5, random_state=0)
    regr.fit(x_train,y_train)
#    print(regr.feature_importances_)
    #Predicting Output Values
    pred = regr.predict([[c,f,d]])
    tk.Label(win, text = f"The tool life found out by the Random Forest Regressor is {pred[0]:0.2f} minutes\n").pack()
    #tk.Label(win, text = f"The tool life found out by the Artificial Neural Network is is {pred[0] - 3.274:0.2f} minutes\n").pack()

def neural(c,f,d):
    import pandas as pd
    df = pd.read_csv('compiled_ab_constant.csv')
    
    #****Use this code if using google collabaratory
    """
    from google.colab import files
    uploaded = files.upload()
    import io
    df = pd.read_csv(io.StringIO(uploaded['compiled_ab_constant.csv'].decode('utf-8')))
    df.head()
    """
    #Importing Libraries
    import numpy as np
    import pandas as pd
    
    #Creating Matrix of Features(inputs) and Matrix of Target Variables(outputs)
    x = df.iloc[:,[1,2,3]].values
    y = df.iloc[:,-1].values
    
    #Importing sklearn for train_test_split
    from sklearn.model_selection import train_test_split
    
    #Splitting DataSet into Training and Testing Set
    x_train, x_test,y_train, y_test = train_test_split(x,y,test_size = 0.2, shuffle = True)
    
    #Scaling Data so than no variable dominates other
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    
    #Creating Neural Network
    import keras
    from keras.models import Sequential #Sequential to initialize NN
    from keras.layers.core import Dense #Dense to add Hidden Layers
    
    #Initializing the Neural Network
    model = Sequential() #naming the model
    
    #Adding input layer
    #init: initialization....uniform to randomly generate weights
    #activation fuction: relu
    model.add(Dense(80, activation = 'relu',input_dim = 3))
    
    #Adding Hidden Layers
    model.add(Dense(40,activation ='relu'))
    model.add(Dense(40,activation ='relu'))
    model.add(Dense(20,activation ='relu'))
    model.add(Dense(10,activation ='relu'))
    model.add(Dense(10,activation ='relu'))
    
    #Adding Output Layer
    model.add(Dense(1,activation ='relu'))
    
    #Compiling Neural Network
    #Optimization Algorithm: Stochastic Gradient Descent, ADAM
    #Loss function: sparse_categorical_crossentropy/ binary_crossentropy if o/p is binary
    #mean_sqaured_error
    #RMSprop
    model.compile(optimizer = 'RMSprop', loss='mean_squared_error', metrics=['accuracy'])
    
    #Training our model
    #Fitting before training
    #Batch size: Iterations after which weight changes
    #Epoch: Total number of iterations
    model.fit(x_train,y_train,batch_size = 30,nb_epoch = 100)

    #Predicting the output 
    y_pred = model.predict(x_train)
    y_op = model.predict(np.array([[c,f,d]]))
    print(f"The tool life obtained by the Artificial Neural Network is {y_op[0,0]:.2f} minutes ")
    
    
