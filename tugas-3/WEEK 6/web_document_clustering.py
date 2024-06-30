


import string
import pandas as pd
import math
import matplotlib.pyplot as plt
import requests
import re
from bs4 import BeautifulSoup
from bs4.element import Comment
from nltk.stem import PorterStemmer


def visible_text(element):
    if element.parent.name in ['style', 'title', 'script', 'head', '[document]', 'class', 'a', 'li']:
        return False
    elif isinstance(element, Comment):
        return False
    elif re.match(r"[\s\r\n]+",str(element)): 
        return False
    elif re.match(r"www.", str(element)):
        return False
    return True

class document_clustering(object):
    
    
    def __init__(self, file_dict, word_list):
        self.file_dict = file_dict
        self.word_list = word_list
        
    def tokenize_document(self, document):
        
        ps = PorterStemmer()
        terms = []
        for i in document:
            temp = i.lower().replace('vehicle', 'car').replace('automobile', 'car').split()
            for j in temp:
                terms.append(j)
        return [ps.stem(term.strip(string.punctuation)) for term in terms]
    
    def create_word_listing(self):
        
        
        
        self.listing_dict_ = {}
        
        for id in self.file_dict:
            temp_word_list = []
            response = requests.get(self.file_dict[id])
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.find_all(text = True)
            text = list(filter(visible_text, text))
            terms = self.tokenize_document(text)
            for term in self.word_list[:500]:
                temp_word_list.append(terms.count(term.lower()))
            self.listing_dict_[id] = temp_word_list
        
        print('Word listing of each document')
        for id in self.listing_dict_:
            print('%d:  %s' % (id, self.listing_dict_[id]))
            
    def create_document_matrix(self):
        
        self.labels_ = ['web%d' % (id) for id in self.file_dict]
        main_list = []
        for id1 in self.file_dict:
            temp_list = []
            for id2 in self.file_dict:
                dist = 0
                for term1, term2 in zip(self.listing_dict_[id1], self.listing_dict_[id2]):
                    dist += (term1-term2)**2
                temp_list.append(round(math.sqrt(dist), 4))
            main_list.append(temp_list)
            
        self.distance_matrix_ = pd.DataFrame(main_list, index = self.labels_, columns = self.labels_)
        print('\nDistance Matrix')
        print(self.distance_matrix_)
    
    def cluster(self):
        
        from scipy.cluster.hierarchy import linkage
        row_cluster = linkage(self.distance_matrix_.values,
                              method = 'complete',
                              metric = 'euclidean')
        from scipy.cluster.hierarchy import dendrogram
        dn = dendrogram(row_cluster, labels = self.labels_)
        plt.ylabel('Euclidean Distance')
        plt.xticks(rotation = 90, fontsize = 7)
        plt.savefig('dendrogram2.png', dpi = 300)
        plt.show()
                
    

file_dict = {1: 'https://www.zigwheels.com/newcars/Tesla',
             2: 'https://www.financialexpress.com/auto/car-news/mahindra-to-launch-indias-first-electric-suv-in-2019-all-new-e-verito-sedan-on-cards/1266853/',
             3: 'https://en.wikipedia.org/wiki/Toyota_Prius',
             4: 'https://economictimes.indiatimes.com/industry/auto/auto-news/government-plans-new-policy-to-promote-electric-vehicles/articleshow/65237123.cms',
             5: 'https://indianexpress.com/article/india/india-news-india/demonetisation-hits-electric-vehicles-industry-society-of-manufacturers-of-electric-vehicles-4395104/',
             6: 'https://www.livemint.com/Politics/ySbMKTIC4MINsz1btccBJO/How-demonetisation-affected-the-Indian-economy-in-10-charts.html',
             7: 'https://www.hrblock.in/blog/impact-gst-automobile-industry-2/',
             8: 'https://inc42.com/buzz/electric-vehicles-this-week-centre-reduces-gst-on-lithium-ion-batteries-hyundai-to-launch-electric-suv-in-india-and-more/',
             9: 'https://www.youthkiawaaz.com/2017/12/impact-of-demonetisation-on-the-indian-economy/',
             10: 'https://indianexpress.com/article/india/demonetisation-effects-cash-crisis-mobile-wallets-internet-banking-4406005/',
             11: 'https://www.news18.com/news/business/how-gst-will-curb-tax-evasion-1446035.html',
             12: 'https://economictimes.indiatimes.com/small-biz/policy-trends/is-gst-helping-the-indian-economy-for-the-better/articleshow/65319874.cms'}

word_list = ['Tesla', 'Electric', 'Car', 'pollution', 'de-monetisation', 'GST' ,'black money']


document_cluster = document_clustering(file_dict = file_dict, word_list = word_list)
document_cluster.create_word_listing()
document_cluster.create_document_matrix()
document_cluster.cluster()