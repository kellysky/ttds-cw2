import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import requests
from bs4 import BeautifulSoup
ps=PorterStemmer()

def page_title(link):
    print(link)
    strs=' '
    try:
        link=re.sub('[^a-zA-Z0-9://.]','',link)
        print(link)
        res = requests.get(link)
        #res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')
        if soup.title is None:
            strs=' '
        else:
            print(soup.title.text)
            strs=soup.title.text
    except Exception as e:
        print('utf8_transfer error',strs,e)
    return strs



def preprecoss(path, filename):
    terms = []
    temp_terms = []
    stopwords=[]

    #read the stopwords file
    with open('englishST.txt') as f:
        line=f.readline()
        while line:
            line=line.split()
            stopwords.append(line[0])
            line=f.readline()

    # read the file and remove the link and lower the character
    with open(path + filename, 'r', encoding="Windows-1252",errors='ignore') as f:
        line = f.readline()
        while line:
            line = line.split('\t')
            line=line[1].split()
            for i in range(0,len(line)):
                if line[i].startswith('http') == False:
                    item = line[i].lower()
                    item = re.sub('[^a-zA-Z0-9#]+', '', item)
                    #if item not in stopwords:
                    #     item=ps.stem(item)
                    if item not in temp_terms:
                        if item not in ' ' or item not in '  ':
                            temp_terms.append(item)
                            #convert duplicated words with #
                            if item.startswith('#') == True:
                                item = re.sub('[^a-zA-Z0-9]+', '', item)
                                if item not in ' ' or item not in '':
                                    if item not in temp_terms:
                                       temp_terms.append(item)
                # else:
                #     #extract page title from the link
                #     link_title=line[i]
                #     title=page_title(link_title)
                #     title=title.split()
                #     for item in title:
                #         if item.startswith('http') == False:
                #             item = item.lower()
                #             item = re.sub('[^a-zA-Z0-9#]+', '', item)
                #             # if item not in stopwords:
                #             #   item=ps.stem(item)
                #             if item not in temp_terms:
                #                 if item not in ' ' or item not in '  ':
                #                     temp_terms.append(item)
            line = f.readline()
    terms = temp_terms

    # give a corrispoding id for terms and write it into file
    with open('../classfication_results/feats.dic3', 'w', encoding='utf-8') as f:
        for i in range(len(terms)):
            f.write(str(i + 1) + ' ' + terms[i])
            f.write('\n')


preprecoss('../tweetsclassification/', 'Tweets.14cat.train')
