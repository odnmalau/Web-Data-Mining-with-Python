


import string
import numpy as np

class document_clustering(object):
    

    def __init__(self, file_dict, word_list, k):
        self.file_dict = file_dict
        self.word_list = word_list
        self.k = k

    def tokenize_document(self, document):
        

        terms = document.lower().split()
        return [term.strip(string.punctuation) for term in terms]

    def create_word_listing(self):
        

        
        
        self.listing_dict_ = {}

        for id in self.file_dict:
            temp_word_list = []
            f = open(self.file_dict[id], 'r')
            document = f.read()
            terms = self.tokenize_document(document)
            for term in self.word_list:
                temp_word_list.append(terms.count(term.lower()))
            self.listing_dict_[id] = temp_word_list

        print('Word listing of each document')
        for id in self.listing_dict_:
            print('%d\t%s' % (id, self.listing_dict_[id]))

    def create_document_matrix(self):
        

        self.distance_matrix_ = []
        for id1 in self.file_dict:
            temp_list = []
            for id2 in self.file_dict:
                dist = 0
                for term1, term2 in zip(self.listing_dict_[id1], self.listing_dict_[id2]):
                    dist += abs(term1 - term2)
                temp_list.append(dist)
            self.distance_matrix_.append(temp_list)

        print('\nDistance Matrix')
        for i in self.distance_matrix_:
            print(i)

    def find_centroid(self, feature):
        

        distances = []
        for centroid in self.centroids_:
            dist = 0
            for term1, term2 in zip(self.centroids_[centroid], feature):
                dist += abs(term1 - term2)
            distances.append(dist)

        return np.argmin(distances)

    def kmeans_clustering(self):
        

        self.centroids_ = {}

        
        
        for i in range(self.k):
            self.centroids_[i] = self.listing_dict_[i + 1]

        for i in range(500):
            self.classes_ = {}
            self.features_ = {}

            for i in range(self.k):
                self.classes_[i] = [i+1]
                self.features_[i] = [self.centroids_[i]]

            for id in self.listing_dict_:
                if id > self.k:
                    classification = self.find_centroid(self.listing_dict_[id])
                    self.classes_[classification].append(id)
                    self.features_[classification].append(self.listing_dict_[id])

            previous = dict(self.centroids_)

            
            for i in self.features_:
                self.centroids_[i] = np.average(self.features_[i], axis = 0)

            isOptimal = True

            for centroid in self.centroids_:
                original_centroid = np.array(previous[centroid])
                curr_centroid = self.centroids_[centroid]

                if np.sum(original_centroid - curr_centroid) != 0:
                    isOptimal = False

            
            if isOptimal:
                break

    def print_clusters(self):
        

        print('\nFinal Clusters')
        for i in self.classes_:
            print('%d:-->%s' % (i+1, self.classes_[i]))



file_dict = {1: 'documents/doc1.txt',
             2: 'documents/doc2.txt',
             3: 'documents/doc3.txt',
             4: 'documents/doc4.txt',
             5: 'documents/doc5.txt',
             6: 'documents/doc6.txt',
             7: 'documents/doc7.txt',
             8: 'documents/doc8.txt',
             9: 'documents/doc9.txt'}

word_list = ['Automotive', 'Car', 'motorcycles', 'self-drive', 'IoT', 'hire' ,'Dhoni']


document_cluster = document_clustering(file_dict = file_dict, word_list = word_list, k = 4)
document_cluster.create_word_listing()
document_cluster.create_document_matrix()
document_cluster.kmeans_clustering()
document_cluster.print_clusters()
