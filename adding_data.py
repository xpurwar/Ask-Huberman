import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure
import os
import glob 

wcd_url = os.environ["WEAVIATE_URL"]
wcd_api_key = os.environ["WEAVIATE_API_KEY"]

# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_api_key),
)

questions = client.collections.get("Question")

# Read all text files from the folder where transcripts are stored
transcript_files = glob.glob("transcripts/*.txt")  # Change path if needed

for file_path in transcript_files:
    with open(file_path, "r", encoding="utf-8") as file:
        transcript_text = file.read()
    
    file_name = os.path.basename(file_path).replace(".txt", "")  # Use file name as title

    # Insert the transcript into Weaviate
    questions.data.insert(
        properties={
            "title": file_name,  # Title of the video
            "content": transcript_text,  # Full transcript
        }
    )
    print(f"Uploaded: {file_name}")

# Close the Weaviate connection
client.close()
print("All transcripts uploaded successfully!")