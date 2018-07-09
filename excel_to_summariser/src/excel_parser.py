# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 21:47:15 2018

@author: Shreyans
"""

import glob, os
import pandas as pd
import numpy as np
import re

runDir = r"C:\Users\Shreyans\Documents\GitHub\Summarisation_SEC\excel_to_summariser\src"

if os.getcwd() != runDir:
    os.chdir(runDir)

def read_excel_file():
    """
    Refer: https://stackoverflow.com/a/21138287/5830794
    """
    files = glob.glob(r"../res/*.xlsx")
    df = pd.DataFrame()
    for each in files:
        sheets = pd.ExcelFile(each).sheet_names
    
        for sheet in sheets:
            df = df.append(pd.read_excel(each, sheet, header = None))
            df = df.append(pd.DataFrame(data= [[None]*len(df.columns)], columns=df.columns))
    return df

def excel_preprocessor():
    ten_q = read_excel_file()
    ten_q.fillna("", inplace=True)
    ten_q = ten_q.astype(str)
    
    dfToTextList = []
    for num in range(len(ten_q)):
        dfToTextList.append(", ".join(ten_q.iloc[num]).rstrip(", ").lstrip(", ").replace(' ,',''))
        
    ten_q_text = "\n".join(dfToTextList)
    return ten_q_text