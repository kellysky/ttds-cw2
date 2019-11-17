import re
import nltk
from nltk.stem import PorterStemmer
import sys
import preprocess

ps=PorterStemmer()

def words():
    stopwords=[]
    # read the stopwords file
    with open('englishST.txt') as f:
        line = f.readline()
        while line:
            line = line.split()
            stopwords.append(line[0])
            line = f.readline()
    return stopwords

#to featured the trainning data file
def featured_train(path,filename):

    topic_dic={'Autos & Vehicles':'1','Comedy':'2','Education':'3','Entertainment':'4','Film & Animation':'5'
,'Gaming':'6','Howto & Style':'7','Music':'8','News & Politics':'9','Nonprofits & Activism':'10','Pets & Animals':'11','Science & Technology':'12','Sports':'13',
'Travel & Events':'14'}

    id_doc={}
    text_list=[]
    stopwords=words()

    with open('../classfication_results/feats.dic3','r') as f:
        line=f.readline()
        while line:
            line=line.split()
            id_doc[line[1]]=line[0]
            line=f.readline()

    #print(id_doc['for'])
    with open(path+filename,'r',errors='ignore') as f:
        line=f.readline()
        while line:
            text=' '
            words_list=[]
            if line.strip() not in '':
                line=line.split('\t')
                line[2]=line[2].replace('\n','')
                id=line[0]
                topic=line[2]
                line=line[1].split()
                content=' '
                for i in range(1,len(line)-1):
                    if line[i].startswith('http')==False:
                        item=line[i].lower()
                        item=re.sub('[^a-zA-Z0-9#]+','',item)
                        #if item not in stopwords:
                         #    item = ps.stem(item)
                        if item not in '':
                            if item in id_doc.keys():
                                    words_list.append(int(id_doc[item]))
                    # else:
                    #     # extract page title from the link
                    #     link_title = line[i]
                    #     title = preprocess.page_title(link_title)
                    #     title = title.split()
                    #     for item in title:
                    #         if item.startswith('http') == False:
                    #             item = item.lower()
                    #             item = re.sub('[^a-zA-Z0-9#]+', '', item)
                    #             # if item not in stopwords:
                    #             #   item=ps.stem(item)
                    #             if item not in '':
                    #                 if item in id_doc.keys():
                    #                     words_list.append(int(id_doc[item]))
                words_list=list(set(words_list))
                words_list=sorted(words_list)

                #print(words_list)
                for item in words_list:
                        text=text+str(item)+':'+'1'+' '
                text=topic_dic[topic]+text+' '+'#'+id
                text_list.append(text)
            else:
                text=' '
            line=f.readline()

    #save the output file
    with open('../classfication_results/feats.train3','w',errors='ignore') as f:
        for item in text_list:
            f.write(item)
            f.write('\n')


#to featured the test data file
def featured_test(path,filename):
    topic_dic = {'Autos & Vehicles': '1', 'Comedy': '2', 'Education': '3', 'Entertainment': '4', 'Film & Animation': '5'
        , 'Gaming': '6', 'Howto & Style': '7', 'Music': '8', 'News & Politics': '9', 'Nonprofits & Activism': '10',
                 'Pets & Animals': '11', 'Science & Technology': '12', 'Sports': '13',
                 'Travel & Events': '14'}

    id_doc = {}
    text_list = []
    stopwords=words()

    with open('../classfication_results/feats.dic3', 'r') as f:
        line = f.readline()
        while line:
            line = line.split()
            print(line)
            id_doc[line[1]] = line[0]
            line = f.readline()

    # print(id_doc['for'])
    with open(path + filename, 'r', errors='ignore') as f:
        line = f.readline()
        while line:
            text = ' '
            words_list=[]
            if line.strip() not in '':
                line = line.split('\t')
                line[2] = line[2].replace('\n', '')
                id = line[0]
                topic = line[2]
                line = line[1].split()
                content = ' '
                for i in range(1, len(line) - 1):
                    if line[i].startswith('http') == False:
                        item = line[i].lower()
                        item = re.sub('[^a-zA-Z0-9#]+', '', item)
                        #if item not in stopwords:
                         #    item=ps.stem(item)
                        if item not in '':
                            if item in id_doc.keys():
                                    words_list.append(int(id_doc[item]))
                    # else:
                    #     # extract page title from the link
                    #     link_title = line[i]
                    #     title = preprocess.page_title(link_title)
                    #     title = title.split()
                    #     for item in title:
                    #         if item.startswith('http') == False:
                    #             item = item.lower()
                    #             item = re.sub('[^a-zA-Z0-9#]+', '', item)
                    #             # if item not in stopwords:
                    #             #   item=ps.stem(item)
                    #             if item not in '':
                    #                 if item in id_doc.keys():
                    #                     words_list.append(int(id_doc[item]))
                words_list=list(set(words_list))
                words_list=sorted(words_list)
                for item in words_list:
                    text = text + str(item) + ':' + '1' + ' '
                text = topic_dic[topic] + text + ' ' + '#' + id
                text_list.append(text)
            else:
                text = ' '
                #text_list.append(text)
            line = f.readline()

    # save the output file
    with open('../classfication_results/feats.test3', 'w', errors='ignore') as f:
        for item in text_list:
            f.write(item)
            f.write('\n')


featured_test('../tweetsclassification/','Tweets.14cat.test')

featured_train('../tweetsclassification/','Tweets.14cat.train')
