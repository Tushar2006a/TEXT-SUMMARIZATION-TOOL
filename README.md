# TEXT-SUMMARIZATION-TOOL
*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: TUSHAR SUHAGPURE 

*INTER ID*: CT06DR1876

*DOMAIN*: ARTIFICIAL INTELLIGENCE

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

##(Internship Task 1 description)

1. Introduction

This project is created as part of my AI internship. In Task 1, I had to build a Text Summarization Tool using a pretrained NLP model. The goal was to take a long paragraph as input and generate a short and meaningful summary. The main focus of the task was to learn how modern AI models understand natural language and how we can use them directly without training them from scratch.

I completed this task on a MacBook Air, and this README explains all the tools, setup, platforms, and technologies I used to successfully build the project.

2. Task Overview

The internship task requiredment:

Using a pretrained HuggingFace summarization model

Writing Python code that loads the model

Taking input text from the user

Setting max_length, min_length, and do_sample parameters

Showing both original text and summary

Making the program run locally on pc

Following clean, structured coding practices

The purpose was to understand NLP pipelines, Transformer models, and basic AI development workflow.

3. Tools & Libraries I Used:

Programming Language:

Python 3.14 
Python is the most popular language for AI development.

Libraries
1. Transformers (HuggingFace)

Used to load powerful NLP models with a single line:

pipeline("summarization")


Transformers library is widely used in real AI companies.

2. SentencePiece

Tokenizer used for models like T5 and BART.

3. PyTorch

Backend used by Transformers.

4. Platform Used
Device:

MacBook Air (macOS)
I performed the entire task on my Mac system.

Terminal:

I used the built-in macOS Terminal for:

Installing libraries

Running Python files

Debugging code

Code Editor:

Visual Studio Code (VS Code)
VS Code is lightweight, fast, and perfect for AI scripting.
I used it to write and save Python files like:

text_summarizer.py

5. Installation Steps:
   
1. Install pip3

Already built into macOS Python versions.

2. Install Transformers
   
"pip3 install transformers"
(direct write in terminal)

4. Install SentencePiece
   
pip3 install sentencepiece
(direct write in terminal)

6. Install PyTorch

its installed automatically when you run the program if you want you can download ownself 

6. How My Code Works

I import the summarization model pipeline:

from transformers import pipeline

Load the summarizer model:

summarizer = pipeline("summarization")


Ask the user to enter text in terminal:

text = input("Enter your paragraph:\n\n")


Generate summary:

summary = summarizer(text, max_length=60, min_length=20, do_sample=False)


Print summarized result to user.

This makes the project very easy and user-friendly.

7. Applications of This Project

This summarizer can be used for:

News article summarization

Student study material

PDF content summaries

Notes compression

Blog summaries

Research paper summarization

AI chatbot backend

Assistive writing tools

It is lightweight and works perfectly on macOS without GPU.

8. Learning Outcome

From this task, I learned:

basics of python

How pretrained NLP models work

How to use HuggingFace pipelines

How summarization algorithms shorten long content

How to install and manage Python libraries on macOS

How to run Python scripts using Terminal

How AI models load, tokenize, and generate outputs

This task strengthened my understanding of core NLP concepts and real-world AI development on Mac systems.

#OUTPUT
<img width="1440" height="900" alt="Image" src="https://github.com/user-attachments/assets/df3822ed-5857-4bee-83e6-b5f3fc9c0705" />
