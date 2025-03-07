# Bert-base-Chinese-Uncertainty

This repository contains the implementation of a fine-tuned model based on Google's [Bert-Base-Chinese model]([https://huggingface.co/google-bert/bert-base-chinese]) to perform uncertainty classification on Chinese sentences. The fine-tuned model is trained to classify sentences as either "certain" or "uncertain." 

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Examples](#examples)
- [Model](#model)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

In many documents, identifying uncertain statements is crucial for decision-making. This project focuses on fine-tuning the pre-trained FinBERT model to classify sentences based on their uncertainty. The task involves distinguishing between "certain" and "uncertain" sentences, where certain sentences express confidence and uncertain sentences leave room for ambiguity.

### Examples:

**Uncertain sentence:**
> "The company *may* achieve higher revenues next quarter."
> "这家公司*可能*在下个季度获得更高的收入。"

**Certain sentence:**
> "The company achieved higher revenues last quarter."
> "这家公司在上个季度获得了更高的收入。"

## Dataset

The training data for this project is sourced from the [Chinese Hedges and their Scope Corpus](https://github.com/DUT-NLP/CHScope). Specifically, the model has been fine-tuned using annotated data from Chinese version of following Corpus:

- **BioScope** (Vincze et al., 2008)
- **WikiWeasel** (Farkas et al., 2010)

Both of these datasets contain annotations that help identify uncertain language in various contexts.

## Model

You can access our model at [Huggingface](https://huggingface.co/Zhenyu-Zane/Bert-Base-Chinese-Uncertainty). The model is built on top of Google's [Bert-Base-Chinese model](https://huggingface.co/google-bert/bert-base-chinese), which is specifically optimized for Chinese language. We have further fine-tuned it to classify sentences as either certain or uncertain, using BioScope and WikiWeasel for training.

## Usage

For usage examples, please refer to the [`Bert-Base-Chinese-Uncertainty-demo.py`](./Bert-Base-Chinese-Uncertainty-demo.py) file, which demonstrates how to use the fine-tuned model for uncertainty classification.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you find a bug or have a feature request.
