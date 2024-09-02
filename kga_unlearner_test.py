# -*- coding: utf-8 -*-
"""kga_unlearner_test

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aEEmhM5qteocbMlES28Mbkthv9rK600L
"""

!pip install accelerate -U
!pip install transformers[torch]

import torch
import re
import copy
import os
import accelerate
from transformers import BertTokenizer, BertForMaskedLM
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

import os
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
import sys
sys.path.append('/content/gdrive/My Drive/')

"""1. Fine tune a bert-base-uncased bert model Ad on data D"""

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
# Load your short story data and tokenize it
with open("/content/gdrive/My Drive/articles_data_D.txt", "r") as f:
    text = f.read()

#Cleaning the training Data##############
# 1. Convert to lowercase
text=text.lower()
#2. Remove html tags
def remove_html_tags(text):
  pattern=re.compile('<.*?>')
  return pattern.sub(r'',text)
text=remove_html_tags(text)
#.3. remove urls

def remove_url(text):
  pattern=re.compile(r'https?://\s+www\.\s+')
  return pattern.sub(r'',text)
text=remove_url(text)
#. 4. Remove punctuation
import string,time
string.punctuation
exclude=string.punctuation

def remove_punc(text):
  for char in exclude:
    text=text.replace(char,'')
  return text
text=remove_punc(text)
# Write the modified text to a file
with open("output.txt", "w") as file:
    file.write(text)
print(type(text))
# Tokenize the text
tokenized_text = tokenizer.tokenize(text)
# Add special tokens
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)

# Create a PyTorch dataset
dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="output.txt",
    block_size=128,
)

# Data collator for language modeling
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./bert_finetuned_on_D",
    overwrite_output_dir=True,
    num_train_epochs=2,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./bert_finetuned_on_D")

"""#2. Here we finetune bert-base-uncased bert model An on Data Dn"""

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
# Load your short story data and tokenize it
with open("/content/gdrive/My Drive/new_data_Dn.txt", "r") as f:
    text = f.read()

#Cleaning the training Data##############
# 1. Convert to lowercase
text=text.lower()
#2. Remove html tags
def remove_html_tags(text):
  pattern=re.compile('<.*?>')
  return pattern.sub(r'',text)
text=remove_html_tags(text)
#.3. remove urls

def remove_url(text):
  pattern=re.compile(r'https?://\s+www\.\s+')
  return pattern.sub(r'',text)
text=remove_url(text)
#. 4. Remove punctuation
import string,time
string.punctuation
exclude=string.punctuation

def remove_punc(text):
  for char in exclude:
    text=text.replace(char,'')
  return text
text=remove_punc(text)
# Write the modified text to a file
with open("new_data_Dn_output.txt", "w") as file:
    file.write(text)
print(type(text))
# Tokenize the text
tokenized_text = tokenizer.tokenize(text)
# Add special tokens
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)

# Create a PyTorch dataset
dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="new_data_Dn_output.txt",
    block_size=128,
)

# Data collator for language modeling
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./bert_finetuned_on_Dn",
    overwrite_output_dir=True,
    num_train_epochs=2,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./bert_finetuned_on_Dn")

"""#3. Hee we finetune a bert-base-uncased model Ar on Dr, the remaining data"""

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
# Load your short story data and tokenize it
with open("/content/gdrive/My Drive/remaining_data_Dr.txt", "r") as f:
    text = f.read()

#Cleaning the training Data##############
# 1. Convert to lowercase
text=text.lower()
#2. Remove html tags
def remove_html_tags(text):
  pattern=re.compile('<.*?>')
  return pattern.sub(r'',text)
text=remove_html_tags(text)
#.3. remove urls

def remove_url(text):
  pattern=re.compile(r'https?://\s+www\.\s+')
  return pattern.sub(r'',text)
text=remove_url(text)
#. 4. Remove punctuation
import string,time
string.punctuation
exclude=string.punctuation

def remove_punc(text):
  for char in exclude:
    text=text.replace(char,'')
  return text
text=remove_punc(text)
# Write the modified text to a file
with open("remaining_data_Dr_output.txt", "w") as file:
    file.write(text)

print("___________________________________**********________________________\n")

# Tokenize the text
tokenized_text = tokenizer.tokenize(text)
# Add special tokens
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)

# Create a PyTorch dataset
dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="remaining_data_Dr_output.txt",
    block_size=128,
)
# print(text2)
# num_samples_to_view = 5
# for i in range(num_samples_to_view):
#     sample = dataset[i]
#     print(f"Sample {i + 1}: {sample}")

# Data collator for language modeling
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./bert_finetuned_on_Dr",
    overwrite_output_dir=True,
    num_train_epochs=2,
    per_device_train_batch_size=2,
    save_steps=10_000,
    save_total_limit=2,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./bert_finetuned_on_Dr")

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')
# Load your short story data and tokenize it
with open("/content/gdrive/My Drive/to_be_forgotten_Df.txt", "r") as f:
    text = f.read()

#Cleaning the training Data##############
# 1. Convert to lowercase
text=text.lower()
#2. Remove html tags
def remove_html_tags(text):
  pattern=re.compile('<.*?>')
  return pattern.sub(r'',text)
text=remove_html_tags(text)
#.3. remove urls

def remove_url(text):
  pattern=re.compile(r'https?://\s+www\.\s+')
  return pattern.sub(r'',text)
text=remove_url(text)
#. 4. Remove punctuation
import string,time
string.punctuation
exclude=string.punctuation

def remove_punc(text):
  for char in exclude:
    text=text.replace(char,'')
  return text
text=remove_punc(text)
# Write the modified text to a file
with open("to_be_forgotten_Df_output.txt", "w") as file:
    file.write(text)

# Tokenize the text
tokenized_text = tokenizer.tokenize(text)
# Add special tokens
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)

# Create a PyTorch dataset
dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="/content/to_be_forgotten_Df_output.txt",
    block_size=128,
)

# Data collator for language modeling
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./bert_finetuned_on_Df",
    overwrite_output_dir=True,
    num_train_epochs=2,
    per_device_train_batch_size=8,
    save_steps=10_000,
    save_total_limit=2,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./bert_finetuned_on_Df")

trainer.save_model("/content/gdrive/My Drive/bert_finetuned_on_D")

trainer.save_model("/content/gdrive/My Drive/bert_finetuned_on_Dn")

trainer.save_model("/content/gdrive/My Drive/bert_finetuned_on_Dr")

D_model_path = "/content/gdrive/My Drive/bert_finetuned_on_D"
bert_finetuned_on_D = BertForMaskedLM.from_pretrained(D_model_path)
Dn_model_path = "/content/gdrive/My Drive/bert_finetuned_on_Dn"
bert_finetuned_on_Dn = BertForMaskedLM.from_pretrained(Dn_model_path)
Df_model_path = "/content/gdrive/My Drive/bert_finetuned_on_Df"
bert_finetuned_on_Df = BertForMaskedLM.from_pretrained(Df_model_path)
Dr_model_path = "/content/gdrive/My Drive/bert_finetuned_on_Dr"
bert_finetuned_on_Dr = BertForMaskedLM.from_pretrained(Dr_model_path)

out_put_unlearned_model=copy.deepcopy(bert_finetuned_on_D)

from transformers import BertTokenizer, TFBertForMaskedLM
import torch.nn.functional as F
# Load the pre-trained tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
#Asian markets started 2015 on an upswing in limited trading on Friday, with mainland Chinese stocks surging in Hong Kong on speculation Beijing may ease monetary policy to boost slowing growth
# Use the model for inference
input_text = "Asian markets started 2015 on an upswing in limited trading on Friday, with mainland [MASK] stocks surging in Hong Kong "
input_ids = tokenizer.tokenize(input_text)
print(input_ids)
masked_index = input_ids.index( '[MASK]' )
print(masked_index)

# Convert the tokenized text to a tensor of token ids
indexed_tokens = tokenizer.convert_tokens_to_ids(input_ids)
tokens_tensor = torch.tensor([indexed_tokens])
print(tokens_tensor)
#indexed_tokens
with torch.no_grad():
    outputs_1 = bert_finetuned_on_D(tokens_tensor)
    predictions_1 = outputs_1[0][0, masked_index].topk(3)
# Logits tensor contain the raw predictions
logits_1 = outputs_1.logits

#Applying softmax to get probabilities The resulting tensor,
#probabilities, contains the probabilities for each token in the
#vocabulary at each position in the input sequence.
probabilities_1 = F.softmax(logits_1, dim=-1)
#print("Probability",max(probabilities_1))

with torch.no_grad():
    outputs_2 = bert_finetuned_on_Dr(tokens_tensor)
    predictions_2 = outputs_2[0][0, masked_index].topk(3)
# Logits tensor contain the raw predictions
logits_2 = outputs_2.logits
probabilities_2 = F.softmax(logits_2, dim=-1)

loss_remain = F.kl_div(input=logits_1, target=logits_2, log_target=True, reduction='batchmean')
print("Kl divergence::::\n")
print(loss_remain)
#In the specific case of BERT and other language models,
#logits represent the scores assigned to each token in the model's vocabulary
#The resulting tensor, probabilities, contains the probabilities for each token in the vocabulary at each position in the input sequence.
