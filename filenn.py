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




if __name__ == "__main__":
    main()