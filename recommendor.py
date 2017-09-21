import pandas as pd
import numpy as np
from sklearn import cross_validation as cv
from sklearn.metrics.pairwise import pairwise_distances

## read data from csv
header = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('ratings.csv', sep=',', names=header)

## print total user
n_users = df.user_id.unique().shape[0]
n_items = df.item_id.unique().shape[0]
print('Number of users = ' + str(n_users) + ' | Number of movies = ' + str(n_items))

train_data, test_data = cv.train_test_split(df, test_size=0.25)

train_data_matrix = np.zeros((n_users, n_items))

user_similarity = pairwise_distances(train_data_matrix, metric='cosine')
item_similarity = pairwise_distances(train_data_matrix.T, metric='cosine')

print(item_similarity)