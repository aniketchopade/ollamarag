# Document Retrieval and Response Generation

This program reads a text file containing a history of the United States, stores each line as a document in a Weaviate vector embedding database, and allows the user to query the database with a prompt. The program retrieves the most relevant document and generates a response based on the retrieved document and the user's prompt.

## Setup Instructions

### 1. Create a Python Virtual Environment

First, create a Python virtual environment named `ollamarag`:

```sh
python -m venv ollamarag
```

Activate the virtual environment:

- On Windows:
  ```sh
  .\ollamarag\Scripts\activate
  ```
- On macOS/Linux:
  ```sh
  source ollamarag/bin/activate
  ```

### 2. Install Dependencies

Install the required Python packages:

```sh
pip install weaviate-client ollama
```

### 3. Install Docker Desktop

To set up the Weaviate database, you need to have Docker Desktop installed. You can download and install Docker Desktop from [here](https://www.docker.com/products/docker-desktop).

After installing Docker Desktop, run the following command to start a Weaviate instance:

```sh
docker run -d -p 8080:8080 semitechnologies/weaviate:latest
```

### 4. Run the Program

Ensure that the text file `A-Short-History-of-the-United-States.txt` is in the same directory as the script. Then, run the script:

```sh
python main.py
```

## High-Level Description

1. **Read Documents**: The program reads a text file and stores each non-empty line as a document.
2. **Connect to Weaviate**: It connects to a local Weaviate instance.
3. **Create Collection**: If a collection named "docs" does not exist, it creates one with a property "text".
4. **Store Documents**: Each document is stored in the Weaviate database with its corresponding vector embedding.
5. **User Prompt**: The user is prompted to enter a query.
6. **Retrieve Document**: The program retrieves the most relevant document from the database based on the user's query.
7. **Generate Response**: It generates a response combining the retrieved document and the user's query using the `ollama` model.
8. **Output Response**: The generated response is printed to the console.

```