import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Restaurant

def combined_features(row):
    return row['address']+" "+row['city'] + " " +row['alcohol']+" " +row['smoking_area']+" "+row['dresscode']+" "+row['price']+" "+row['ambience']+" "+row['area']+" "+row['other_services']

def get_id_from_index(df, index):
    return df[df.index == index]["id"].values[0]


def get_index_from_id(df, id):
    return df[df.id == id].index.values[0]


def get_recommendation_for_restaurant(restaurant_id):
    df = pd.DataFrame(list(Restaurant.objects.all().values()))
    features = ['address', 'city','alcohol', 'smoking_area', 'dresscode', 'price','ambience','area','other_services']
    for feature in features:
        df[feature] = df[feature].fillna('')

    df["combined_features"] = df.apply(combined_features, axis=1)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])    
    cosine_sim = cosine_similarity(count_matrix)
    id = get_index_from_id(df, restaurant_id)

    similar_restaurants = list(enumerate(cosine_sim[id]))

    sorted_similar_restaurants = sorted(
        similar_restaurants, key=lambda x: x[1], reverse=True)

    i = 0
    restaurant_ids = []
    for restaurant in sorted_similar_restaurants:
        i = i + 1
        restaurant_ids.append(get_id_from_index(df, restaurant[0]))

        if i > 15:
            break

    return restaurant_ids

