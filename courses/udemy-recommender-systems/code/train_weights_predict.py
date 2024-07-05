import pandas as pd
import numpy as np


df = pd.read_csv("../ml-20m/ratings.csv")
print(df.shape)
df.head()

# procesamiento de los datos
N_users = 100
N_movies = 500

# keep users most have scored movies
users_to_keep = df["userId"].value_counts().iloc[:N_users]
users_to_keep = users_to_keep.index

# keep movies most scored
movies_to_keep = df["movieId"].value_counts().iloc[:N_movies]
movies_to_keep = movies_to_keep.index

# filter dataset
df = df[df["userId"].isin(users_to_keep) & df["movieId"].isin(movies_to_keep)]
df = df.drop(columns=["timestamp"])
print(f"Dimension del dataframe despues de filtrar el top de users y movies: {df.shape}")
df.head()

del users_to_keep, movies_to_keep

# ==================================================
# compute users similarity
# ==================================================
users = df["userId"].unique()
movies = df["movieId"].unique()

# 
def predict(data: pd.DataFrame, user_x: int, movie: int, k: int):

    avg_rating_x = data.query("userId==@user_x")["rating"].mean()

    weights_dev = {
        user_y: compute_weights_xy(
            data, user_x, user_y
        ) for user_y in users if user_x != user_y
    }
    w_users = {user_y:weights_dev[user_y]["w_xy"] for user_y in weights_dev.keys()}
    w_users = sorted(w_users.items(), reverse=True, key=lambda x: x[1])
    w_users = [(user_y, w) for user_y, w in w_users if w>0]
    w_users = [(user_y, w) for user_y, w in w_users if movie in weights_dev[user_y]["dev_y"].keys()]    
    
    if len(w_users) > k:
        w_neigh = w_users[:k]
    else:
        w_neigh = w_users

    if len(w_neigh) > (k/2):
        w_neigh = dict(w_neigh)
        numerator = np.sum([weights_dev[y]["dev_y"][movie] * w for y, w in w_neigh.items()])
        denominator = np.sum(np.abs(list(w_neigh.values())))
        if denominator==0:
            prediction = avg_rating_x
        else:
            dev_hat = numerator / denominator
            prediction = avg_rating_x + dev_hat
    else:
        prediction = avg_rating_x
    
    prediction = min(5, prediction)
    prediction = max(.5, prediction)
    
    return prediction


def compute_weights_xy(df: pd.DataFrame, user_x: int, user_y: int):
    
    results = {}
    min_common_movies = 5
    
    movies_x = df.query("userId==@user_x").drop(columns=["userId"])
    movies_x["dev"] = movies_x["rating"] - movies_x["rating"].mean()

    movies_y = df.query("userId==@user_y").drop(columns=["userId"])
    movies_y["dev"] = movies_y["rating"] - movies_y["rating"].mean()

    common_movies = (
        movies_x.merge(movies_y, on=["movieId"], how="inner")
    )
    if common_movies.shape[0] >= min_common_movies:
        # los pesos seran la similitud del coseno
        num = common_movies["dev_x"].values @ common_movies["dev_y"]
        den = (
            np.sqrt(common_movies["dev_x"].values @ common_movies["dev_x"]) * 
            np.sqrt(common_movies["dev_y"].values @ common_movies["dev_y"])
        )
        results["w_xy"] = num / den
        
        if results["w_xy"] > 0:
            results["dev_y"] = {int(m): round(r, 4) for m, r in common_movies[["movieId", "dev_y"]].values}
        else:
            results["w_xy"] = 0
    else:
        results["w_xy"] = 0

    return results

# ejecutar predicciones
predictions = [
    predict(
        data=df, 
        user_x=user_x, 
        movie=movie, 
        k=10
    ) for user_x, movie in df[["userId", "movieId"]].values
]
