# Semantic similarity
A program that calculates and displays the semantic similarity between a given sentence and a dictionary potentially related sentences
<br/>
### Pre-requisites
- install spacy library - [Link](https://spacy.io/usage)
- install the english md model (en_core_web_md) - [Link](https://spacy.io/usage#quickstart)
- install the english sm model (en_core_web_sm) - [Link](https://spacy.io/usage#quickstart) 
<br/>
### Running the program
Download the files in the repo on your machine, open the semantic.py file with your preferred IDE.

You can change between small model and the medium model by modifying the nlp variable's loading option:
    
- to load the small model, change <u>__load()__</u> to <u>__load('en_core_web_sm')__</u>
- to load the medium model, change <u>__load()__</u> to <u>__load('en_core_web_sm')__</u>

You can change the "sentence_to_compare" variable to any other text you want to compare.

You can also alter (change, add, remove) the "sentences" dictionary to your preference to generate different results