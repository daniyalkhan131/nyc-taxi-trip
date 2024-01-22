from joblib import load
import numpy as np
model_path = "models/model.joblib"
model = load(model_path)

f=np.array([1]*15).reshape(-1,15)
prediction = model.predict(f)

print(f"prediction={prediction}")