import gensim
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

# Load pre-trained Word2Vec model and stuff
#model = gensim.models.Word2Vec.load("word2vec_jobs.model")
#job_vectors = np.load("job_vectors.npy")
#df_filtered = pd.read_csv('job_positions.csv')
script_dir = Path(__file__).resolve().parent
model = gensim.models.Word2Vec.load(str(script_dir) + "/word2vec_jobs.model")
job_vectors = np.load(str(script_dir) + "/job_vectors.npy")
df_filtered = pd.read_csv(str(script_dir) + '/job_positions.csv')


def document_vector(word_list):
    # remove out-of-vocabulary words
    doc = [word for word in word_list if word in model.wv.key_to_index]
    if len(doc) == 0:
        return np.zeros(model.vector_size)
    return np.mean(model.wv[doc], axis=0)

def getTop5Jobs(new_job_skills):
    new_job_vector = document_vector(new_job_skills)
    similarities = cosine_similarity([new_job_vector], job_vectors).flatten()

    # Get the top 5 similar jobs indices and scores
    top_indices = similarities.argsort()[-5:][::-1]
    top_similar_jobs = df_filtered.iloc[top_indices]
    top_confidence_scores = similarities[top_indices]

    print(type(top_confidence_scores))

    # Display the results
    results = pd.DataFrame({
      'Job': top_similar_jobs['search_position'],
      'Score': top_confidence_scores
    })
    return results


getTop5Jobs(['program', 'develop', 'software', 'java', 'c++'])
