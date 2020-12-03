# Similar-Words
A small web service for printing similar words in the English language.

How To Use

    1. install python 3
    2. pip install -r requirements.txt

Run 

    main.py


DB
       
    "words_clean.txt" text file local directory.
    
NEW DB 
     
     "new_db.json"  text file local directory.
    
    
    

Algorithm

    1. Load data to internal DB.
    2. Read each word
    3. Assign a unique key - the word sorted by multiply prime numbers
    4. Save word to new db under the key prime number
    
  When a word is requested
  
    1. Sort word to get key.
    2. Use key to get all words in group.
    3. Extract the word from the group.
    
  Return request
  
    1. Big O calculation:
    2. Retrieve a list of words from DB in O1A unique key that doubles prime numbers from a hash table.

