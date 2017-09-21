import pandas as pd
import graphlab

ratings_base = pd.read_csv('ratings.csv', sep=',', encoding='latin-1')
ratings_base.shape
train_data = graphlab.SFrame(ratings_base)
popularity_model = graphlab.popularity_recommender.create(train_data, user_id='userId', item_id='movieId', target='rating')
#Get recommendations for first 5 users and print them
#users = range(1,6) specifies user ID of first 5 users
#k=5 specifies top 5 recommendations to be given
popularity_recomm = popularity_model.recommend(users=range(1,6) , k=5)
# popularity_recomm.print_rows(num_rows=25)
print ratings_base.groupby(by='movieId')['rating'].mean().sort_values(ascending=False).head(20)
