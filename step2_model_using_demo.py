# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:58:00 2024

@author: ShowerLee
"""

import os
os.chdir(r"D:\notebook\论文\中文模糊限制语")
import re
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
# tested in transformers==4.18.0 
import transformers
transformers.__version__


if __name__ == "__main__":
    df = pd.DataFrame()
    test_sentence = ['牛顿研究发现物体所受到的外力等于动量对时间的一阶导数。',
                     '现有研究表明物体所受到的外力等于动量对时间的一阶导数。']
    # bert-base-chinese
    bert = BertForSequenceClassification.from_pretrained('./模型/bert-base-chinese-uncertainty',num_labels=2)
    tokenizer = BertTokenizer.from_pretrained('google-bert/bert-base-chinese')
    nlp = pipeline("text-classification", model=bert, tokenizer=tokenizer)
    results = nlp(test_sentence)
    df['bert-base-chinese'] = [1 if res['label'] == 'LABEL_1' else 0 for res in results]
    # chinese-bert-wwm-ext
    bert = BertForSequenceClassification.from_pretrained('./模型/chinese-bert-wwm-ext-uncertainty',num_labels=2)
    tokenizer = BertTokenizer.from_pretrained('hfl/chinese-bert-wwm-ext')
    nlp = pipeline("text-classification", model=bert, tokenizer=tokenizer)
    results = nlp(test_sentence)
    df['chinese-bert-wwm-ext'] = [1 if res['label'] == 'LABEL_1' else 0 for res in results]