import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel # incoming data is valid 

app = FastAPI()

with open('model.pkl', 'rb') as f:
    pipeline = pickle.load(f)

class JobInput(BaseModel):
    region: str
    eco_activity: str
    city: str
    comp_size: str
    job_title: str
    exper: int
    comp_type: int

@app.post("/predict")
def predict_salary(job: JobInput):
    input_data = pd.DataFrame([job.dict()])
    predicted = pipeline.predict(input_data)[0]
    return {"predicted_salary": round(predicted, 2)}