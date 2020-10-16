from collections import Counter
from responses import responses, blank_spot
from user_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
import spacy

word2vec = spacy.load("en_core_web_md")

exit_commands = ("quit", "goodbye", "exit", "no")

class ChatBot:
    
    #define .make_exit()
    def make_exit(self, user_message):
        for command in exit_commands:
            if command in user_message:
                print("Ok, have a good day!")
                return True
            
            
    #define .chat()
    def chat(self):
        # write a welcoming prompt for a user question
        user_message = input("Hello there! How can I help you? ")
        while not self.make_exit(user_message):
            user_message = self.respond(user_message)


    #define .find_intent_match()
    def find_intent_match(self, responses, user_message):
        # create a Bag-of-Words model
        bow_user_message = Counter(preprocess(user_message))
        processed_responses = [Counter(preprocess(response)) for response in responses]
        # select the response that best matches the intent of the user message
        similarity_list = [compare_overlap(item, bow_user_message) for item in processed_responses]
        # select the index of the highest similarity score
        response_index = similarity_list.index(max(similarity_list))
        return responses[response_index]
    
    
    #define .find_entities()
    def find_entities(self, user_message):
        tagged_user_message = pos_tag(preprocess(user_message))
        message_nouns = extract_nouns(tagged_user_message)
        # fit a word2vec model on our candidate entities
        tokens = word2vec(" ".join(message_nouns))
        category = word2vec(blank_spot)
        word2vec_result = compute_similarity(tokens, category)
        # select the entity with the highest similarity score
        word2vec_result.sort(key=lambda x: x[2])
        if len(word2vec_result) > 0:
            return word2vec_result[-1][0]
        else:
            return blank_spot

    
    # define .respond()
    def respond(self, user_message):
        best_response = self.find_intent_match(responses, user_message)
        entity = self.find_entities(user_message)
        print(best_response.format(entity))
        #print(best_response)
        input_message = input("Would you like something else? ")
        return input_message



#initialize ChatBot instance below:
chatbot_one = ChatBot()

#call .chat() method below:
chatbot_one.chat()