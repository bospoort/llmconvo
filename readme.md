# Introduction

This project provides an API to start a conversation between two roles on a given topic using FastAPI. The conversation is generated using a language model.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- Requests

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/llmconvo.git
    cd llmconvo
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Server

Start the server with the following command:

```bash
uvicorn llmconvo:app --host 0.0.0.0 --port 8000 --reload --log-level debug
```

Send a message:

```
curl -X 'POST'   'http://localhost:8000/start_conversation'   -H 'Content-Type: application/json'   -d '{
  "topic": "Artificial Intelligence",
  "role1": "Researcher",
  "role2": "Skeptic",
  "messages": 5
}'
```

curl -X POST 'http://localhost:8000/start_conversation' -H 'Content-Type: application/json' -d '{"topic": "Artificial Intelligence", "role1": "Researcher", "role2": "Skeptic", "messages": 5}'


curl -X POST 'http://localhost:11434/api/generate' -H 'Content-Type: application/json' -d '{"model": "deepseek-r1:1.5b", "prompt": "Why is the sky blue?", "stream": false, "options": {"num_thread": 8, "num_ctx": 2024}}'