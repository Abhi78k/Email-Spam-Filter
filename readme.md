# Email Spam Filter using Naive Bayes

This project is a simple email spam classification system built using Python, FastAPI, and a custom implementation of the Naive Bayes algorithm. The model classifies text messages as spam or ham using word frequencies learned from the spam dataset.

[Dataset](https://www.kaggle.com/datasets/abdallahwagih/spam-emails) from kaggle.

The system includes both a backend API for prediction and a frontend interface for user interaction.

## Overview

Unlike some Naive Bayes implementations that parse the dataset on every request, this project preprocesses the dataset once and stores all word frequency counts in two JSON files located in the backend folder:

* spam_freq.json
* ham_freq.json

This reduces repeated computation and speeds up classification.

The backend loads these files during startup and uses them to compute probabilities efficiently.

## Features

* Naive Bayes classifier implemented manually without external ML libraries like scikit-learn
* Laplace smoothing to prevent zero probabilities
* Preprocessed word counts stored in JSON files for faster queries
* FastAPI backend exposing a prediction endpoint
* Simple frontend with a text input box for message testing
* Handles punctuation removal, tokenization, and case normalization
* Lightweight and easy to extend

## Setup

Refer to `setup.md` for clear instructions to setup the project

## Tech Stack

### Backend

* Python 3
* FastAPI
* pandas
* uvicorn

### Frontend

* HTML
* CSS
* JavaScript (Fetch API)

### Data and Storage

* spam.csv dataset from Kaggle
* JSON files for word-frequency storage

## Dataset

[Dataset](https://www.kaggle.com/datasets/abdallahwagih/spam-emails) from kaggle.
Required columns:

* Category (spam or ham)
* Message (text)

## How It Works

### Preprocessing

* Lowercasing
* Removing punctuation
* Splitting into tokens
* Counting word frequencies for spam and ham separately
* Creating two JSON files with all frequency counts

### Model Training

* Computes prior probabilities:

  * P(spam)
  * P(ham)
* Calculates conditional probabilities using Laplace smoothing.

### Classification

For a given message:

* Tokenize the text
* For each word, compute:

  * P(word | spam)
  * P(word | ham)
* Sum log probabilities
* Compare final scores to determine the predicted class

## Project Structure

```
backend/
  main.py
  spam_freq.json
  ham_freq.json
  spam.csv  

frontend/
  index.html
  script.js
  style.css

README.md
setup.md
```

## API Endpoint

### POST /predict

Request body:

```
{
  "message": "your text here"
}
```

Response:

```
{
  "prediction": 0 or 1
}
```

## License

This project is open-source and intended for learning and experimentation.
