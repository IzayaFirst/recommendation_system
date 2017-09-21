import pandas as pd
import mongoclient
import graphlab
import json

client = mongoclient.getConnection()
MRating = client['miletrav-development'].MRating
data = MRating.find().sort([('userId', 1),('movieId', 1)])
ratings_base =  pd.DataFrame(list(data))
ratings_base = ratings_base.drop('_id', 1)
train_data = graphlab.SFrame(ratings_base)
item_sim_model = graphlab.item_similarity_recommender.create(train_data, user_id='userId', item_id='movieId', target='rating', similarity_type='cosine')
item_sim_recomm = item_sim_model.recommend(k=20)
result = []
for sc in item_sim_recomm:
    ddt = json.dumps(sc, ensure_ascii=False)
    ddt = json.loads(ddt)
    mongoclient.saveMovieRecommender(ddt, client )

