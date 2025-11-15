import pandas as pd
import math
import string 
import json 
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class InputMessage(BaseModel):
  message: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def predict(message: str)->str:
  data = pd.read_csv('spam.csv')

  totalRows = len(data)

  spam = data[data['Category']=='spam']
  ham = data[data['Category']=='ham']

  lenSpam = len(spam)
  lenHam = len(ham)

  probSpam = lenSpam/totalRows
  probHam = lenHam/totalRows

  with open('hamdict.json','r') as f:
    hamdict = json.load(f)
    
  with open('spamdict.json','r') as f:
    spamdict = json.load(f)
    
  def remove_punctuation(text):
      translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
      return text.translate(translator).lower()
  
  a = sum(spamdict.values())
  b = sum(hamdict.values())

  spamFreqDict = spamdict.copy()
  hamFreqDict = hamdict.copy()

  spamdict = {i:spamdict[i]/a for i in spamdict}
  hamdict = {i:hamdict[i]/b for i in hamdict}
  vocab = set(list(spamdict.keys())+list(hamdict.keys()))
  v = len(vocab)

  t = message
  t = remove_punctuation(t)
  t = t.split()

  # take log to avoid very small numbers
  spamScore=math.log(probSpam)
  hamScore=math.log(probHam)

  for word in t:
    # perform laplace smoothing so that the words that are not in the given emails dont just make the probability 0 when multiplied.
    spamFreq = spamFreqDict.get(word,0)
    spamProb = (spamFreq+1)/(a+v)
    spamScore+=math.log(spamProb)
      
    hamFreq = hamFreqDict.get(word,0)
    hamProb = (hamFreq+1)/(b+v)
    hamScore+=math.log(hamProb)
    
  return 0 if spamScore>hamScore else 1

@app.post("/predict")
def output_prediction(input: InputMessage):
  result = predict(input.message)
  return {"prediction":result}
  