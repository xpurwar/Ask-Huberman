import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure
import os

# Best practice: store your credentials in environment variables
wcd_url = os.environ["WEAVIATE_URL"]
wcd_api_key = os.environ["WEAVIATE_API_KEY"]

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,                                    # Replace with your Weaviate Cloud URL
    auth_credentials=Auth.api_key(wcd_api_key),             # Replace with your Weaviate Cloud key
)

questions = client.collections.create(
    name="Question",
    vectorizer_config=Configure.Vectorizer.text2vec_weaviate(), # Configure the Weaviate Embeddings integration
    generative_config=Configure.Generative.cohere()             # Configure the Cohere generative AI integration
)

client.close() 