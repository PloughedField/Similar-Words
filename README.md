# Similar-Words
A small web service for printing similar words in the English language.

How To Use
  1. install python
  2. pip install -r /path/to/requirements.txt
  or 
  1.pip install fastapi
  2.pip install uvicorn
  3.pip install typing

Run 
  main.py


DB
  A DB of the English dictionary should be provided.
  The service expects the DB ("words_clean.txt" text file) to be in the local directory.

Algorithm
    1.Load data to internal DB.
    2.Read each word
    3.Assign a unique key - the word sorted by multiply prime numbers
    4.Save word to new db under the key prime number.
  When a word is requested
    1.Sort word to get key.
    2.Use key to get all words in group.
    3.Extract the word from the group.
  Return request.
    1.Big O calculation:
    2.Since db is implemented by a Golang hash map, Retrieval is O(1). 

