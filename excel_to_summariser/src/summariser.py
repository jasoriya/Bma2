# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 10:02:33 2018

@author: Shreyans
"""

from excel_parser import excel_preprocessor
from gensim.summarization import summarize
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser


def summarizer(algo):
    text = excel_preprocessor()
    if algo is 'gensimTextRank':
        text_summarized = summarize(text, word_count=5000)
        return text_summarized
    elif algo is 'sumyTextRank':
        parser = PlaintextParser(text, Tokenizer('english'))
        stemmer = Stemmer('english')
        text_summarizer = TextRankSummarizer(stemmer)
        text_summarizer.stop_words = get_stop_words('english')
        summarized = text_summarizer(parser.document, 25)
        sent = []
        for sentence in summarized:
            sent.append(str(sentence))
        text_summarized = "\n\n".join(sent)
        return text_summarized
    else:
        msg = "Accepted Inputs are: \n1. gensimTextRank\n2. sumyTextRank"
        print(msg)
        
if __name__ == "__main__":
    text = summarizer('gensimTextRank')
    text = text.replace("\n", "\n\n")
    with open("../output.txt", "w") as f:
        f.writelines(text)
   
