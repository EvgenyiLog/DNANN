import os
import sys
import numpy as np
import pandas  as pd
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style 
#import xlsxWriter 
import cv2

from LOCSFile import LOCSFile
from BCLFile   import BCLFile
import os.path
import gemmi
from cifreaderq import cifreader
from sklearn.decomposition import FastICA,PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import BaggingClassifier
import dtaidistance
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import Lasso,Ridge

 




import warnings
import csv
def main():
    warnings.simplefilter("ignore")
    warnings.filterwarnings("default", category=FutureWarning)
    'source_dir path sourse'
    #source__dir = "F:/Program Files/Sar/pythondif/s_1_1101.locs"
    #source__dir=os.path.abspath("C:/files/")
    source__dir="C:/Users/evgen/Downloads/DNATOOOLS/files/"
    #print(source__dir)
    #pathsave="F:/Program Files/Sar/pythondif/result.xlsx"
    
    ainten=[]
    cinten=[]
    ginten=[]
    tinten=[]
   


    for (dirpath, dirnames, filename) in os.walk(source__dir):
        #print(dirnames)
        #print(filename)
        #print(dirpath)
        for i,filename in enumerate(sorted(filename)):
            filename=os.path.join(dirpath, filename)
            #print(filename)
            
           
            
            if filename.endswith(".cif"):
                intenA,intenC,intenT,intenG,k=cifreader(filename)
                #print(intenA.shape)
                ainten.append(np.asarray(intenA,dtype=float))
                cinten.append(np.asarray(intenC,dtype=float))
                tinten.append(np.asarray(intenT,dtype=float))
                ginten.append(np.asarray(intenG,dtype=float))


    number=np.arange(1,len(ginten)+1)
    #print(number)
              
    x=PrettyTable()
    x.add_column('number',number)
    x.add_column('A',ainten)
    x.add_column('G',ginten)
    x.add_column('C',cinten)
    x.add_column('T',tinten)
    x.align = "c"
    print(x)

    

    
    x=np.column_stack((ainten,ginten,cinten,tinten))
    print(x.shape)
    df = pd.DataFrame(x,
                  columns=['intensitivityA','intensitivityG','intensitivityC','intensitivityT'])
    boxplot = df.boxplot(column=['intensitivityA','intensitivityG','intensitivityC','intensitivityT'])
    plt.figure('Violinplot',figsize=(15,7))   
    sns.violinplot(data=df)
    plt.grid(True)
    plt.tick_params(labelsize =20,#  Размер подписи
                    color = 'k')   #  Цвет 
    

    plt.figure('Boxplot',figsize=(15,7))    
    sns.boxplot(df)
    plt.grid(True)
    plt.tick_params(labelsize =20,#  Размер подписи
                    color = 'k')   #  Цвет делений
    

    #plt.figure('Histplot',figsize=(15,7))  
    #sns.histplot(df)
    #plt.grid(True)
    #plt.tick_params(labelsize =20,#  Размер подписи
                    #color = 'k')   #  Цвет делений
        
    plt.show()




if __name__ == "__main__":
    main()