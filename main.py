documents = []
with open('A-Short-History-of-the-United-States.txt', 'r') as file:
    documents = [line.strip() for line in file if line.strip()]

import weaviate

client = weaviate.connect_to_local()

import weaviate.classes as wvc
from weaviate.classes.config import Property, DataType

# Check if the collection exists
if not client.collections.exists("docs"):
    # Create a new data collection
    collection = client.collections.create(
        name = "docs", # Name of the data collection
        properties=[
            Property(name="text", data_type=DataType.TEXT), # Name and data type of the property
        ],
    )
else:
    collection = client.collections.get("docs")

import ollama

# Store each document in a vector embedding database
with collection.batch.dynamic() as batch:
  for i, d in enumerate(documents):
    # Generate embeddings
    response = ollama.embeddings(model = "all-minilm", prompt = d)
    #print(response)
    # Add data object with text and embedding
    batch.add_object(
        properties = {"text" : d},
        vector = response["embedding"],
    )


# Prompt the user for input
user_prompt = input("Enter your prompt: ")

# Generate an embedding for the user prompt and retrieve the most relevant doc
response = ollama.embeddings(
  model = "all-minilm",
  prompt = user_prompt,
)

results = collection.query.near_vector(near_vector = response["embedding"],
                                       limit = 1)

data = results.objects[0].properties['text']
# print(data)

prompt_template = f"Using this data: {data}. Respond to this prompt: {user_prompt}"

# Generate a response combining the prompt and data we retrieved in step 2
output = ollama.generate(
  model = "llama2",
  prompt = prompt_template,
)

print(output['response'])

client.close()