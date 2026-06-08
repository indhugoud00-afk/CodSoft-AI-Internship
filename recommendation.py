import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# loading dataset
movies = pd.read_csv("movies.csv")

# converting genres into numerical format
vectorizer = CountVectorizer()

genre_matrix = vectorizer.fit_transform(movies["Genre"])

# calculating similarity between movies
similarity = cosine_similarity(genre_matrix)


def recommend_movie(movie_name):

    movie_name = movie_name.strip()

    if movie_name not in movies["Movie"].values:
        print("\nMovie not found in dataset.")
        return

    movie_index = movies[movies["Movie"] == movie_name].index[0]

    similarity_scores = list(enumerate(similarity[movie_index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Movies:")
    print("-" * 25)

    recommendation_count = 0

    for movie in similarity_scores[1:]:

        index = movie[0]

        print(
            f"{recommendation_count + 1}. "
            f"{movies.iloc[index]['Movie']} "
            f"({movies.iloc[index]['Genre']})"
        )

        recommendation_count += 1

        if recommendation_count == 5:
            break


print("=" * 50)
print("      MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nAvailable Movies:\n")

for movie in movies["Movie"]:
    print("-", movie)

while True:

    user_movie = input("\nEnter a movie name (or type exit): ")

    if user_movie.lower() == "exit":
        print("Thank you for using the system.")
        break

    recommend_movie(user_movie)