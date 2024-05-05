# CareerCannon

## Description of Project
The goal of the project is to use machine learning techniques to help users plot their job trajectory as well as recommend relevant jobs using datasets obtained from the open web.

## Required Libraries
We recommend avoiding compiling the libraries yourself using pip and use Anaconda instead. 
On Production servers we recommend using miniconda.

- python                    3.12.3  
- streamlit                 1.32.0
- numpy                     1.26.4
- pandas                    2.2.1
- joblib                    1.2.0
- gensim                    4.3.2 
- scikit-learn              1.3.0
- scipy                     1.12.0

## How to run
### 1. Install dependencies. We recommend installing dependencies using conda rather than pip to avoid compiling everything from scratch.

### 2. Download raw data and place them in the /data folder:
       linkedin_job_postings.csv - https://drive.google.com/file/d/16YFG4mViI6VbKCya3DFxaS3kWnZQSsTF/view?usp=drive_link
       job_skills.csv - https://drive.google.com/file/d/1Tu2pGznuz6DQks4etPnO1iRg7au2dQLn/view?usp=drive_link
       
### 4. Run through all the jupyter notebooks to generate the models in ML-Logic.
Require the following files:
1. Raw data. The /data folder should look like this
<img width="376" alt="image" src="https://github.com/weelye/Project_01/assets/168352720/82288451-f1fa-4d79-8ad2-7fef4804b982">

2. Decision Tree data from notebooks. The /decision_tree folder should look like this
<img width="374" alt="image" src="https://github.com/weelye/Project_01/assets/168352720/be819fcf-3e25-4620-af03-bd51a9bceb47">

3. Word2vec data from notebooks. The /word2vec folder should look like this
<img width="473" alt="image" src="https://github.com/weelye/Project_01/assets/168352720/8281a8be-0f5b-48c5-a4fe-22c977a43452">

### 5. Change directory to the main project folder (/Project_01) and run "run_webapp.sh" to start. 
- We recommend running the application using a process manager such as Node.js PM2 or supervisord.
