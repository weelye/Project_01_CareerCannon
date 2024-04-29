import pandas as pd
import numpy as np
from pathlib import Path
from joblib import load

script_dir = Path(__file__).resolve().parent
filename = str(script_dir)+'/software_engineer_clf.joblib'
clf_load = load(filename)
X_train = pd.read_csv(str(script_dir)+'/columns_1.csv')

def predict(new_job_skills):
  df_prediction_input = pd.DataFrame(0, index=np.arange(1),columns=X_train.columns)

  for skill in new_job_skills:
    if skill in df_prediction_input.columns:
      df_prediction_input.loc[:, skill] = 1

  predicted = clf_load.predict_proba(df_prediction_input)
  return pd.DataFrame(predicted, columns=['not_software_engineer', 'is_software_engineer'])



#print(predict(['program', 'develop', 'software', 'java', 'c++', 'node.js', 'murder']))
