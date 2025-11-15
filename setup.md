# Project Setup Guide

## Prerequisites

Ensure the following are installed on your system:

* Python 3.8 or above
* pip
* Git

## 1. Clone the Repository

```
git clone <your-repo-url>
cd <project-folder>
```

## 2. Create and Activate a Virtual Environment

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### Linux or macOS

```
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```
pip install fastapi uvicorn pandas
```

If a requirements.txt file exists:

```
pip install -r requirements.txt
```

## 4. Dataset Preparation

Place the dataset file named `spam.csv` inside the backend folder.

Required columns:

* Category
* Message

## 5. Preprocessing and JSON Generation

If your version of the project already includes the generated JSON files (`spam_freq.json` and `ham_freq.json`), skip this step.

If not, run the preprocessing script to create them:

```
python main.py --build-json
```

This script should:

* Load spam.csv
* Process the dataset
* Generate spam_freq.json and ham_freq.json

After creation, the backend will use these files for predictions.

## 6. Run the Backend Server

```
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

## 7. Run the Frontend

You can open `index.html` directly in your browser or serve it from a simple local server.

### Option A: Open index.html directly

Double-click the file.

### Option B: Use Python HTTP server

```
cd frontend
python -m http.server 5500
```

Open:

```
http://localhost:5500
```

## 8. Sending a Test Request

Using curl:

```
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Congratulations, you won a prize\"}"
```

Response example:

```
{"prediction": 0}
```

## Notes

* Make sure the JSON and CSV filenames match those referenced in main.py
