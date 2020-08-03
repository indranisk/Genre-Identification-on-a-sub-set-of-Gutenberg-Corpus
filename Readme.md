# NLP Feature Extractor for Books

## Extracts features from books and compares them to the features of other books to get a set of similar books

### Set of features include :
* sentiment analysis from the beginning of a book
* sentiment analysis from the ending of a book 
* sentences count
* average sentence length
* flesch reading score
* word count
* Proper noun count

### Packages required :
* textblob
* textstat
* bs4
* re 
* csv
* os
* pandas
* sklearn

## USAGE

### 1. Feature Extractor
##### Entry point : `feature_extractor.py`
##### Inputs : a folder called "books" containing all the required books in html format
##### Output : a csv file containing features from all books called 'features.csv'

*To generate a new features file, rename the old file or move it to another directory before running the script*

### 2. Similar books picker 

##### ---- TO BE IMPLEMENTED ---- 


## Features dataset discription

* BOOK_ID   - Book id
* Senti_S1  - Sentiment of the 1st 1/3 of the book's beginning
* Senti_S2  - Sentiment of the 2nd 1/3 of the book's beginning
* Senti_S3  - Sentiment of the 3rd 1/3 of the book's beginning
* Senti_E1  - Sentiment of the 1st 1/3 of the book's ending
* Senti_E2  - Sentiment of the 2nd 1/3 of the book's ending
* Senti_E3  - Sentiment of the 3rd 1/3 of the book's ending
* S_count   - Sentences count
* Avg_S_len - Average Sentence length
* Flesch    - Flesch reading score
* W_count   - Word count
* Noun_Cnt  - Proper noun count
