# This is a smart chatbot program.

# Import the libraries

from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)


# get the article
article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521?cjdata=MXxOfDB8WXww&cjevent=6431664eba9111f083e900dc0a82b82c&cm_mmc=CJ-_-100357191-_-5250933-_-Evergreen+Link+for+Mayo+Clinic+Diet&utm_source=cj&utm_content=100357191&utm_capaign=3-months')
article.download()
article.parse()
article.nlp()
corpus = article.text

# print the article text



# Tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text) # A list of sentences

# A function to return a random greeting response to a users greeting
def greeting_response(text):
    text = text.lower()

# Bots greeting response
    bot_greetings = ['Hello', 'Hi', 'Hey']
# Users greeting
    user_greetings = ['Hi', 'hi', 'hi hello', 'Hello', 'hello', 'hey', 'Hey', 'hows it going', 'Hows it going', 'Hows it going?', 'hows it going?', 'how are you', 'How are you', 'How are you doing?', 'how are you doing?']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
        # Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index


# Create bots response
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm= CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+ ' '+sentence_list[index[i]]
            response = response_flag = 1
            j=j+1
        if j > 2:
            break

    if response_flag == 0:
        bot_response = bot_response + ' ' + 'I apologize, I dont understand.'

    sentence_list.remove(user_input)
    return bot_response

# Start the chat
print('Sarah Bot: I am Sarah Bot. I will answer your queries about Chronic Kidney Disease. If you want to exit type bye.')

exit_list = ['exit', 'see you later', 'bye', 'Bye', 'quit', 'break']

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Sarah Bot: Chat with you later!')
        break
    else:
        if greeting_response(user_input) != None:
            print('Sarah Bot: ' + greeting_response(user_input))
        else:
            print('Sarah Bot: ' +bot_response(user_input))