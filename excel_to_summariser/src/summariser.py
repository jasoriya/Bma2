# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:02:33 2018

@author: Shreyans
"""

from excel_parser import excel_preprocessor
from gensim.summarization import summarize

text = excel_preprocessor()
text_summarized = summarize(text, ratio = 0.01)