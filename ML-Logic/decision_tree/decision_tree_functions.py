import pandas as pd
import numpy as np
from pathlib import Path
from joblib import load

script_dir = Path(__file__).resolve().parent

# Load 1 model per job!?
filename = str(script_dir)+'/software_engineer_clf.joblib'
clf_se_load = load(filename)
#

X_train = pd.read_csv(str(script_dir)+'/columns_1.csv')

def predict(new_job_skills,jobname):
  df_prediction_input = pd.DataFrame(0, index=np.arange(1),columns=X_train.columns)
  predicted = pd.DataFrame()

  for skill in new_job_skills:
    if skill in df_prediction_input.columns:
      df_prediction_input.loc[:, skill] = 1

  if jobname.lower() == "software engineer":
    predicted = clf_se_load.predict_proba(df_prediction_input)

  return pd.DataFrame(predicted, columns=['not_software_engineer', 'is_software_engineer'])

def getMostWantedSkills(jobname):

  most_features_frame = pd.DataFrame()
  if jobname.lower() == "software engineer":
    most_features_frame = pd.DataFrame(
      data=clf_se_load.feature_importances_,
      columns=["importance"],
      index=X_train.columns,
      ).sort_values(by=["importance"], ascending=False)

  top_5_feature = most_features_frame.index[:6]
  top_5_feature_list = [i for i in top_5_feature]

  return top_5_feature_list


#print(predict(['program', 'develop', 'software', 'java', 'c++', 'node.js', 'murder']))
