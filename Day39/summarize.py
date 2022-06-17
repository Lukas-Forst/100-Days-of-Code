from collections import Counter
import re
import requests
from bs4 import BeautifulSoup
import bs4
import nltk
from nltk.corpus import stopwords

def main():
    #speech = []
    """
    r = requests.get("https://www.ruhr-uni-bochum.de/gna/Quellensammlung/10/10_mlkihaveadream_1963.htm")
    soup = BeautifulSoup(r.text, 'html.parser')
    body = soup.body
    #for text in body.find_all("p", class_="QuellenText"):
    #    speech.append(text.text)
    #speech_n = ''.join(speech)
    test_speech = [element.text for element in body.find_all("p", class_="QuellenText")]
    """
    url = 'http://www.analytictech.com/mb021/mlk.htm'
    page = requests.get(url)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    p_elems = [element.text for element in soup.find_all('p')]
    speech_n = ''.join(p_elems)
    #print(soup.body)
    #print(len(speech))
    speech_n = speech_n.replace(')mowing', 'knowing')
    speech_n = re.sub('\s+', ' ', speech_n)
    speech_edit = re.sub('[^a-zA-Z]', ' ', speech_n)
    speech_edit = re.sub('\s+', ' ', speech_edit)
    while True:
        max_words = input("Enter max words per sentence for summary: ")
        num_sents = input("Enter number of sentences for summary: ")
        if max_words.isdigit() and num_sents.isdigit():
            break
        else:
            print("\nInput must be in whole numbers.\n")

    speech_edit_no_stop = remove_stop_words(speech_edit)
    word_freq = get_word_freq(speech_edit_no_stop)

    sent_scores = score_sentences(speech_n, word_freq, max_words)
    #print(nltk.sent_tokenize(speech_n))
    counts = Counter(sent_scores)
    summary = counts.most_common(int(num_sents))
    print("\nSUMMARY:")
    print(speech_n)
    #print(summary, sent_scores, counts)
    for i in summary:
        print(i[0])


def remove_stop_words(speech_edit):
    """Remove stop words from string and return string."""
    stop_words = set(stopwords.words('english'))
    speech_edit_no_stop = ''
    for word in nltk.word_tokenize(speech_edit):
        if word.lower() not in stop_words:
            speech_edit_no_stop += word + ' '
    return speech_edit_no_stop

def get_word_freq(speech_edit_no_stop):
    """Return a dictionary of word frequency in a string."""
    word_freq = nltk.FreqDist(nltk.word_tokenize(speech_edit_no_stop.lower()))
    return word_freq

def score_sentences(speech, word_freq, max_words):
    """Return dictionary of sentence scores based on word frequency."""
    sent_scores = dict()
    print(max_words)
    sentences = nltk.sent_tokenize(speech)
    for sent in sentences:
        sent_scores[sent] = 0
        words = nltk.word_tokenize(sent.lower())
        sent_word_count = len(words)
        #print(words, sent_word_count)
        if sent_word_count <= int(max_words):
            for word in words:
                if word in word_freq.keys():
                    sent_scores[sent] += word_freq[word]
            sent_scores[sent] = sent_scores[sent] / sent_word_count
        #print(sent_scores)
    return sent_scores

if __name__ == "__main__":
    main()