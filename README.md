# Practicum 1 - Question Answering Project
This is the repo for the Question Answering project developed by the following students as part of the 1st year practicum

 - Divya Parvatala (divyaparvatala@msitprogram.net)
 - Sri Rama Karthikeya Lanka (karthiklanka19@msitprogram.net)
 - Leela Venkat Sai Anaparthi (karthiklanka19@msitprogram.net)
 - Prathima Avula (prathima.avula@msitprogram.net)
 - Makireddy Avinash Reddy (prathima.avula@msitprogram.net)
 - Sai Venkata Srinath Erramilli (srinath.esv@msitprogram.net)
 - Nikhil Chowdary Linga (nikhillinga670@msitprogram.net)
 - Vishwaja Meddela (nikhillinga670@msitprogram.net)

# Components of the system

## Question Generation

Given a document (for example the text of a document from Wikipedia), the module should generate a set of questions relevant to that document. The goal is to generate questions that are fluent and reasonable. That is, they should be grammatically correct and in idomatic English, and they should also be answerable based on the information in the document.

The question generation program must have the following command line interface

```python3
python question_generation.py article.txt num_questions
```
where `article.txt` is a path to an arbitrary plain text file (the article) and `num_questions` is an integer which represents the number of questions to be generated. The program should output to STDOUT a sequence of questions which each question printed on a newline.

## Question Answering

Given a plain text document and a set of questions, the module should return an answer for each question. The goal is to produce answers that are fluent, correct and concise. That is the answers should be in idiomatic / grammatically correct English, they should be correct according to the document and they should not contain any extra words.

The question answering program must have the following command line interface

```python3
python question_answering.py article.txt questions.txt
```
where `article.txt` is a path to an arbitrary plain text file (the article) and `questions.txt` is a path to an arbitrary file of questions (one question per line with no extraneous material). The output (to STDOUT) should contain a sequence of answers with each answer terminated by a newline character.
