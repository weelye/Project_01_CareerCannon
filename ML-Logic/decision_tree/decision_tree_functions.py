import pandas as pd
import numpy as np
import glob, os
from pathlib import Path
from joblib import load

script_dir = str(Path(__file__).resolve().parent)
clf_dict = dict()

X_train = pd.read_csv(str(script_dir)+'/columns_1.csv')
X_train_2 = pd.read_csv(str(script_dir)+'/columns_2.csv')

for file in glob.glob(script_dir+"/*.joblib"):
  clf_name = Path(file).stem
  clf_dict[clf_name] = load(file)

def getSanitizedJobName(jobname):
  return jobname.lower().replace(" ", "_") + "_clf"

def getSkillsColumns(jobname):
  if jobname.lower() == "software engineer":
    return X_train.columns
  return X_train_2.columns

def predict(new_job_skills,jobname):
  cols = getSkillsColumns(jobname)
  df_prediction_input = pd.DataFrame(0, index=np.arange(1),columns=cols)

  predicted = pd.DataFrame()
  for skill in new_job_skills:
    if skill in df_prediction_input.columns:
      df_prediction_input.loc[:, skill] = 1

  predicted = clf_dict[getSanitizedJobName(jobname)].predict_proba(df_prediction_input)

  return pd.DataFrame(predicted, columns=['no', 'yes'])

def getMostWantedSkills(jobname):
  most_features_frame = pd.DataFrame(
      data=clf_dict[getSanitizedJobName(jobname)].feature_importances_,
      columns=["importance"],
      index=getSkillsColumns(jobname),
      ).sort_values(by=["importance"], ascending=False)
  top_5_feature = most_features_frame.index[:6]
  top_5_feature_list = [i for i in top_5_feature]

  return top_5_feature_list


#print(predict(['program', 'develop', 'software', 'java', 'c++', 'node.js', 'murder'],"software engineer"))
