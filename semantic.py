# importing required libraries
import spacy

#loading the md english model 
nlp = spacy.load('en_core_web_md')

# declaring the sentence to compare and a dict of sentences to compare with
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

# declaring the model of the sentence for comparison
model_sentence = nlp(sentence_to_compare)

# looping through the dict of sentences,
# calculating the similarity of each sentence to the sentence_to_compare and
# displaying the similarity
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
"""Output:
where did my dog go -  0.630065230699739
Hello, there is my car -  0.8033180111627156
I've lost my car in my car -  0.6787541571030323
I'd like my boat back -  0.5624940517078084
I will name my dog Diana -  0.6491444739190607

the highest similarity is with the second sentence, "Hello, there is my car"
    - this is because the sentence_to_compare we ask why the cat is on the car and
    in the sentence we point at the car's location
    
the lowest similarity is with the 4th sentence, "I'd like my boat back"
    - this is because the sentence hasn't got a clear link to the sentence_to_compare
    we would likely look into the sentence for either our car or our cat which is not the case here but
    the sentence is pointing towards another object that we posses, the boat
the similarities results for the first, 3rd and 5th are quite close to each other
    - 1st and 5th are about dogs; dogs and cats are both pets
    - one of the objects in the 3rd sentence is 'car' which appears twice (as the object lost and its location) which
    is also the location of the lost cat in the the sentence_to_compare
"""