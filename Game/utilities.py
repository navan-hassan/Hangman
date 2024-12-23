import requests
import random

REQUEST_URL = 'https://www.randomlists.com/data/vocabulary-words.json'
WORD_POOL = []


def get_random_word():
    global WORD_POOL
    if len(WORD_POOL) == 0:
        response = requests.get(REQUEST_URL).json()
        WORD_POOL = [entry['name'] for entry in response['data']]

    word = random.choice(WORD_POOL)
    WORD_POOL.remove(word)
    return word.upper()
