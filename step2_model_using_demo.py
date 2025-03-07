# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:58:00 2024

@author: ShowerLee
"""

from transformers import BertTokenizer, BertForSequenceClassification, pipeline
# tested in transformers==4.18.0 
import transformers
transformers.__version__


if __name__ == "__main__":

    bert = BertForSequenceClassification.from_pretrained('./bert-base-chinese-uncertainty',num_labels=2)
    tokenizer = BertTokenizer.from_pretrained('./vocab.txt')
    nlp = pipeline("text-classification", model=bert, tokenizer=tokenizer)

    results = nlp(['牛顿研究发现物体所受到的外力等于动量对时间的一阶导数。',
                   '现有研究表明物体所受到的外力等于动量对时间的一阶导数。'])
