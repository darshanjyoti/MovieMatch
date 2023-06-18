This is a movie recommender system aim to provide personalized recommendations to users based on their favourite movie and pereferences. It is a content-based movie recommender system that utilizes cosine similarity and the bag-of-words algorithm. The system is built using the Python libraries pandas and numpy for data processing and streamlit for visualization and website creation.
The workflow of the content-based movie recommender system can be summarized as follows:
-Load and preprocess the movie dataset using pandas.
-Extract features from movie titles and descriptions using the bag-of-words algorithm.
-Calculate the cosine similarity between each pair of movies based on their feature vectors.
-For a given movie, retrieve the top-k most similar movies based on their cosine similarity scores.
-Present the recommendations to the user through a user-friendly interface created using streamlit.
