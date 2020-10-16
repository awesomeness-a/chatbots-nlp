# Chatbots with Python and NLP
This repository contains a few chatbots built using `Python` and `NLP`.

## Alienbot
_Rule-based_ chatbots use __regular expression__ patterns to match user input to human-like responses that simulate a conversation with a real person.
Their responses are entirely predefined and returned to the user according to a series of rules.
This includes __decision trees__ that have a clear set of possible outputs defined for each step in the dialog.\
__Alienbot__ is a closed domain, rule-based chatbot that simulates a real conversation with a human.


## Cyborg Cantina 
_Retrieval-based_ chatbots' responses are pulled from an existing corpus of dialogs. ML models, such as __statistical NLP models__ and sometimes __supervised NN__,
are used to interpret the user input and determine the most fitting response to retrieve.\
Like rule-based models, retrieval-based models rely on predefined responses, but they have the additional ability to self-learn and improve their selection of response over time.\
__Cyborg Cantina__ a retrieval-based chatbot system for a restaurant serving Mexican cuisine. It's built with a combination of __tf-idf__ scoring, __word embedding__ models, 
and a set of use-defined functions in order to answer any number of questions from a restaurant diner.

## Twitter Generative Chatbot
_Generative chatbots_ are capable of formulating their own original responses based on user input, rather than relying on existing text. 
This involves the use of __deep learning__, such as LSTM-based __seq2seq models__, to train the chatbots to be able to make decisions about what is an appropriate response 
to return.\
In this project, we create a generative chatbot using a stream of tweets on a particular topic.
