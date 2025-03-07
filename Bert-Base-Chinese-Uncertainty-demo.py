# -*- coding: utf-8 -*-
# Note: the following code is for demonstration purpose. Please use GPU for fast inference on large scale dataset.

from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import transformers
transformers.__version__


if __name__ == "__main__":

    bert = BertForSequenceClassification.from_pretrained('./bert-base-chinese-uncertainty',num_labels=2)
    tokenizer = BertTokenizer.from_pretrained('google-bert/bert-base-chinese')
    nlp = pipeline("text-classification", model=bert, tokenizer=tokenizer)
    results = nlp(['牛顿研究发现物体所受到的外力等于动量对时间的一阶导数。',
                   '现有研究表明物体所受到的外力等于动量对时间的一阶导数。'])
    results
