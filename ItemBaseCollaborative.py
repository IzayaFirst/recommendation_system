import pandas as pd
import graphlab

ratings_base = pd.read_csv('ratings.csv', sep=',', encoding='latin-1')
print ratings_base
#train_data = graphlab.SFrame(ratings_base)

#item_sim_model = graphlab.item_similarity_recommender.create(train_data, user_id='userId', item_id='movieId', target='rating', similarity_type='cosine')
#item_sim_recomm = item_sim_model.recommend(k=100)
#item_sim_recomm.print_rows(num_rows=10000)