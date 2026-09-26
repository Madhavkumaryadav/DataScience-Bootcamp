# Data Science Bootcamp

A hands-on, notebook-based collection of Data Science and Machine Learning learning material — from Python fundamentals to deep learning, NLP, MLOps and deployment.

[![Stars](https://img.shields.io/github/stars/Madhavkumaryadav/DataScience-Bootcamp?style=flat-square)](https://github.com/Madhavkumaryadav/DataScience-Bootcamp/stargazers)
[![Forks](https://img.shields.io/github/forks/Madhavkumaryadav/DataScience-Bootcamp?style=flat-square)](https://github.com/Madhavkumaryadav/DataScience-Bootcamp/forks)
[![Issues](https://img.shields.io/github/issues/Madhavkumaryadav/DataScience-Bootcamp?style=flat-square)](https://github.com/Madhavkumaryadav/DataScience-Bootcamp/issues)
[![Last Commit](https://img.shields.io/github/last-commit/Madhavkumaryadav/DataScience-Bootcamp?style=flat-square)](https://github.com/Madhavkumaryadav/DataScience-Bootcamp/commits/main)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

---

## Table of Contents

- [Overview](#overview)
- [Learning Roadmap](#learning-roadmap)
- [Repository Structure](#repository-structure)
- [Topics Covered](#topics-covered)
- [Tools & Technologies](#tools--technologies)
- [Getting Started](#getting-started)
- [Running Notebooks](#running-notebooks)
- [Projects / Applications](#projects--applications)
- [Learning Path](#learning-path)
- [Practice](#practice)
- [Who Is This For?](#who-is-this-for)
- [How to Use This Repository](#how-to-use-this-repository)
- [Repository Notes](#repository-notes)
- [Contributing](#contributing)
- [Author](#author)
- [Repository Link](#repository-link)

---

## Overview

**Data Science Bootcamp** is a personal learning and practice repository. It is organized as a sequence of topic folders, and almost everything inside is a Jupyter notebook written while learning and practicing each concept.

The repository is built for people who prefer **reading and running code** over reading theory. Each folder focuses on one area: Python basics, data analysis with pandas/NumPy, visualization, feature engineering, machine learning algorithms, deep learning, NLP, experiment tracking with MLflow, containerization with Docker, MongoDB, and interactive apps with Streamlit.

The content follows a natural progression — **Python fundamentals → data analysis → feature engineering → machine learning → deep learning → NLP → MLOps and deployment** — so the folders can be studied roughly in the order they appear. Beyond notebooks, the repository also contains small runnable applications (Flask and Streamlit apps, Docker setups) and practice assignments with solutions.

> Note: this is a learning repository. Code and notebooks were written while studying, so naming is not always consistent and some files are exploratory (for example, `Untitled.ipynb` files).

---

## Learning Roadmap

```
Python Fundamentals
        ↓
Pandas / NumPy (Data Analysis)
        ↓
Data Visualization
        ↓
Feature Engineering
        ↓
Machine Learning  (Supervised + Unsupervised)
        ↓
Deep Learning (Artificial Neural Networks)
        ↓
NLP (Text Preprocessing → BOW / TF-IDF / Word2Vec)
        ↓
MLflow (Experiment Tracking)
        ↓
Docker (Containerization)
        ↓
MongoDB (Data Storage)  ·  Flask & Streamlit (Deployment)
```

Every stage above maps to a real folder in the repository.

---

## Repository Structure

```text
DataScience-Bootcamp/
├── Python_basic/                    # Core Python language concepts
│   ├── Logging/                     # logging module examples and scripts
│   ├── OOPs/                        # OOP pillars, magic methods, small projects
│   ├── m_thread_and_m_process/      # Threading and multiprocessing
│   ├── memory_management/           # Python memory management
│   └── pkg1/                        # Custom package / module import example
├── pandas/                          # pandas fundamentals + CSV/XLSX samples
├── Analysis_with_python/            # NumPy, pandas, Matplotlib, Seaborn, SQLite3
├── data_visualization/              # Matplotlib visualization examples
├── Feature_engineering/             # Encoding, missing values, imbalance, SMOTE
├── Machine_learning/
│   ├── Supervised_ML/               # Regression, classification, ensembles
│   └── Unsupervised_ML/             # Clustering, PCA, anomaly detection
├── Deep_Learning/                   # Activation functions + ANN project
│   └── ANN/Churn_prediction/        # Customer churn ANN (TensorFlow/Keras)
├── NLP/                             # Tokenization, BOW, TF-IDF, Word2Vec, spam classifier
├── MLflow/                          # MLflow experiment tracking example
├── Docker/                          # Hello World + Docker Compose Flask apps
├── MongoDB/                         # PyMongo connection and CRUD operations
├── Streamlit/                       # Streamlit apps (basic, widgets, Iris classifier)
├── Flase/                           # Flask basics (routes, templates, JSON responses)
├── Practice_set/                    # Assignments with solutions
├── .gitignore
└── .vscode/settings.json
```

### Directory descriptions

| Directory | What it contains |
| --- | --- |
| `Python_basic/` | Notebooks covering lists, tuples, sets, dictionaries, conditionals and loops, functions, lambda functions, iterators and decorators, exception handling, file handling, importing modules, and practice sets. |
| `Python_basic/Logging/` | Practical use of the `logging` module: log files, single and multiple loggers, reading log files, plus small scripts and a task with solution. |
| `Python_basic/OOPs/` | OOP pillars (classes and objects), magic/dunder methods, a file-handling project that logs errors, and a Tkinter-based desktop search script. |
| `Python_basic/m_thread_and_m_process/` | Threading and multiprocessing examples, including `concurrent.futures` pool executor usage. |
| `Python_basic/memory_management/` | Notebook on Python memory management. |
| `Python_basic/pkg1/` | Example of a custom Python package (`__init__.py`, `maths.py`). |
| `pandas/` | `Pandas_day_1.ipynb` with hands-on pandas operations, plus sample datasets (`aids.csv`, `call_center.xlsx`, `test.csv`) and exported results. |
| `Analysis_with_python/` | Separate notebooks for NumPy, pandas, Matplotlib, Seaborn and SQLite3, along with a sample `train.csv` and SQLite database files. |
| `data_visualization/` | Notebook showcasing plots built with Matplotlib and NumPy. |
| `Feature_engineering/` | Data encoding (One-Hot, Ordinal, Label), handling missing values, handling imbalanced datasets, the SMOTE technique, and a five-number summary notebook. |
| `Machine_learning/Supervised_ML/` | Linear regression (simple, multiple, polynomial, Ridge/Lasso/ElasticNet), logistic regression, decision trees (pre- and post-pruning), KNN, SVM, Naive Bayes, and `bagging_boosting/` with AdaBoost, Gradient Boosting, Random Forest and XGBoost notebooks. |
| `Machine_learning/Unsupervised_ML/` | DBSCAN, hierarchical clustering, K-Means, PCA implementation, and anomaly detection with Isolation Forest. |
| `Deep_Learning/` | `Activation Function.ipynb` plus `ANN/Churn_prediction/` — a full ANN workflow (EDA, encoding, scaling, model training with TensorBoard callbacks). |
| `NLP/` | Text preprocessing (tokenization, stemming, lemmatization, stopwords, POS tagging, NER), Bag of Words, TF-IDF, Word2Vec, and a spam mail classifier. |
| `MLflow/` | `model_train.py` using `mlflow.sklearn.autolog()` with a Random Forest on the built-in wine dataset, plus the generated `mlruns/` tracking artifacts. |
| `Docker/` | Two Docker exercises: a minimal Flask "Hello World" container and a Docker Compose setup running Flask with Redis. |
| `MongoDB/` | Notebooks connecting to MongoDB from Python with PyMongo and performing insert, query, filter, sort and delete operations. |
| `Streamlit/` | Three Streamlit scripts: a basics demo, a widgets/inputs demo, and an Iris species prediction app. |
| `Flase/` | Intro-level Flask scripts demonstrating routes, GET/POST handling, Jinja templates and JSON API responses, with an `templates/` folder of HTML pages. |
| `Practice_set/` | Question-and-solution notebook pairs for Python topics, NumPy/pandas, and OOP. |

---

## Topics Covered

| Topic | Description |
| --- | --- |
| Python | Core language: data types, loops, functions, lambda, iterators, decorators, exception handling, file handling, modules |
| OOP | Classes, objects, OOP pillars, magic methods, small OOP projects |
| Logging | Python `logging` module, loggers, log files, reading logs |
| Concurrency | Threading and multiprocessing |
| NumPy | Array creation and numerical operations |
| pandas | Series, DataFrames, data manipulation, I/O, data cleaning |
| Data Visualization | Matplotlib and Seaborn charts |
| SQLite3 | Creating databases, tables and running SQL queries from Python |
| Feature Engineering | Data encoding, missing value handling, imbalanced data, SMOTE, five-number summary |
| Supervised Learning | Linear, polynomial, Ridge/Lasso/ElasticNet, logistic regression, decision trees, KNN, SVM, Naive Bayes |
| Ensemble Learning | Bagging and boosting: Random Forest, AdaBoost, Gradient Boosting, XGBoost |
| Unsupervised Learning | K-Means, DBSCAN, hierarchical clustering, PCA, anomaly detection |
| Model Evaluation | Accuracy, confusion matrix, classification report, ROC-AUC, cross-validation, hyperparameter search |
| Deep Learning | Activation functions, Artificial Neural Networks |
| NLP | Tokenization, stemming, lemmatization, stopwords, POS tagging, NER, Bag of Words, TF-IDF, Word2Vec |
| MLflow | Experiment tracking and model logging |
| Docker | Writing Dockerfiles and using Docker Compose |
| MongoDB | Connecting Python to MongoDB and performing CRUD operations |
| Flask | Basic web routes, templates and JSON APIs |
| Streamlit | Building interactive data/ML apps |

---

## Tools & Technologies

All of the following appear in the repository's notebooks, scripts or dependency files.

**Programming & Environment**

- Python 3
- Jupyter Notebook
- `venv` / virtual environments

**Data Science & Visualization**

- NumPy
- pandas
- Matplotlib
- Seaborn
- Plotly Express (`plotly.express`)
- SciPy (`scipy.cluster.hierarchy`)
- SQLite3

**Machine Learning**

- scikit-learn (`sklearn`)
- XGBoost (`xgboost`)
- imbalanced-learn (`imblearn` — SMOTE)
- statsmodels
- ydata-profiling / pandas-profiling
- kneed
- joblib, pickle

**Deep Learning**

- TensorFlow
- Keras (via `tensorflow.keras`)
- TensorBoard

**NLP**

- NLTK
- Gensim (Word2Vec, `gensim.downloader`)

**MLOps, Storage & Deployment**

- MLflow
- Docker and Docker Compose
- Flask
- Redis
- Streamlit
- PyMongo (MongoDB)

**Python standard library used in examples:** `logging`, `pickle`, `multiprocessing`, `threading`, `concurrent.futures`, `tkinter`, `sqlite3`, `datetime`, `os`.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Madhavkumaryadav/DataScience-Bootcamp.git
cd DataScience-Bootcamp
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

There is **no root `requirements.txt`** in this repository. Dependency files exist only inside certain topics:

| Dependency file | Packages listed |
| --- | --- |
| `NLP/requirements.txt` | `nltk`, `pandas`, `numpy`, `scikit-learn` |
| `MLflow/requirements.txt` | `mlflow==2.5.0` |
| `Deep_Learning/ANN/Churn_prediction/requirements.txt` | `tensorflow`, `numpy`, `pandas`, `streamlit`, `scikit-learn`, `matplotlib`, `tensorboard` |
| `Docker/Hello_World/requirements.txt` | `Flask` |
| `Docker/docker_compose/requirements.txt` | `Flask==3.0.2`, `redis==5.0.1` |

Install the file for the topic you are working on, e.g.:

```bash
pip install -r NLP/requirements.txt
```

For topics without a requirements file (pandas, visualization, feature engineering, machine learning, MongoDB, Streamlit, Flask), install the libraries that the notebook or script actually imports, for example:

```bash
pip install jupyter numpy pandas matplotlib seaborn scikit-learn
```

```bash
# Only for the notebooks that use them
pip install xgboost imbalanced-learn statsmodels gensim pymongo plotly scipy kneed
```

### 4. Extra setup notes

- **MongoDB notebooks** expect a local MongoDB server. The notebooks connect to `mongodb://localhost:27017` (and `mongodb://127.0.0.1:27017`), so a running MongoDB instance is required.
- **Docker examples** require Docker installed locally.
- **`NLP/word2vec/word2vec_implement.ipynb`** downloads the large `word2vec-google-news-300` model via `gensim.downloader`, which needs an internet connection and takes a while.

---

## Running Notebooks

From the repository root, with your virtual environment activated:

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

Then navigate to the folder for the topic you want to study, for example:

- `Python_basic/python_basic.ipynb` — start here for Python basics
- `pandas/Pandas_day_1.ipynb` — pandas practice
- `Analysis_with_python/numpy.ipynb`, `Pandas.ipynb`, `Matplotlib.ipynb`, `Seaborn.ipynb`
- `Feature_engineering/Handling_missing_value.ipynb`
- `Machine_learning/Supervised_ML/Logistic_regression/logistic_regression_first.ipynb`
- `Deep_Learning/ANN/Churn_prediction/Explore_data.ipynb`
- `NLP/Tokenization/practice_tokenization.ipynb`

Run the cells from top to bottom. Some notebooks read local CSV files (for example the churn and NLP notebooks), so open them from their own folder so the relative file paths resolve.

> Tip: the repository also contains `.ipynb_checkpoints/` folders. Those are editor-generated backups — ignore them, and open the real notebooks instead.

---

## Projects / Applications

These are the application-style projects present in the repository.

### 1. Customer Churn Prediction (ANN)

- **Purpose:** Predict whether a bank customer will churn using an Artificial Neural Network.
- **Main technologies:** TensorFlow, Keras, scikit-learn, pandas, NumPy, Matplotlib, pickle, TensorBoard.
- **Folder:** `Deep_Learning/ANN/Churn_prediction/`
- **Details:** `Explore_data.ipynb` covers data exploration, label/one-hot encoding, train-test split, feature scaling, model building and training with `EarlyStopping` and `TensorBoard` callbacks. Trained artifacts are stored in the folder: `model.h5`, `scaler.pkl`, `one_hot_encoder.pkl`, `level_encoder_gender.pkl`, and TensorBoard logs under `logs/fit/`.
- **Dataset:** `Churn_Modelling.csv`
- **How to run:** install `Deep_Learning/ANN/Churn_prediction/requirements.txt` and run the notebook from inside that folder.

### 2. SMS / Email Spam Classifier

- **Purpose:** Classify SMS messages as spam or ham using different text-vectorization approaches.
- **Main technologies:** NLTK, Gensim (Word2Vec), scikit-learn, pandas.
- **Folder:** `NLP/Email_spam_classifier/`
- **Notebooks:** `BOW_to_implement.ipynb` (Bag of Words), `TF-IDF_using.ipynb` (TF-IDF), `Word2vec_spam_Mail_classifier.ipynb` (Word2Vec embeddings).
- **Dataset:** `SMSSpamCollection`

### 3. Product Review Classifier

- **Purpose:** A basic NLP project on a product review dataset.
- **Main technologies:** pandas, Matplotlib, Seaborn.
- **Folder:** `NLP/candle_review_classifier/`
- **Notebook:** `NLP_Project_for_basic.ipynb`
- **Dataset:** `amazon_product_reviews.csv`

### 4. Word2Vec Implementation

- **Purpose:** Explore word embeddings using Gensim, including loading a pretrained Google News model.
- **Folder:** `NLP/word2vec/`
- **Notebook:** `word2vec_implement.ipynb`

### 5. Streamlit Apps

- **Folder:** `Streamlit/`
- **`app.py`** — Streamlit basics: title, text, DataFrame display and a line chart.
- **`widgets.py`** — Text input, slider, selectbox and CSV file uploader.
- **`classification.py`** — Trains a Random Forest classifier on the Iris dataset and predicts the species from sidebar sliders.
- **How to run** (from the `Streamlit` folder):

  ```bash
  pip install streamlit pandas numpy scikit-learn
  streamlit run app.py
  ```

### 6. MLflow Experiment Tracking

- **Purpose:** Demonstrate MLflow autologging for a scikit-learn model.
- **Folder:** `MLflow/`
- **Script:** `model_train.py` — uses `mlflow.sklearn.autolog()`, trains a `RandomForestClassifier` on the built-in wine dataset, and logs params, metrics and the model.
- **How to run:**

  ```bash
  cd MLflow
  pip install -r requirements.txt
  python model_train.py
  mlflow ui
  ```

  The generated run artifacts are already committed under `MLflow/mlruns/`.

### 7. Docker — Hello World Flask App

- **Purpose:** Containerize a minimal Flask web app.
- **Folder:** `Docker/Hello_World/`
- **Files:** `app.py`, `Dockerfile`, `requirements.txt`
- **How to run:**

  ```bash
  cd Docker/Hello_World
  docker build -t hello-world-flask .
  docker run -p 5000:5000 hello-world-flask
  ```

### 8. Docker Compose — Flask + Redis

- **Purpose:** Run a multi-container application where a Flask app counts visits in Redis.
- **Folder:** `Docker/docker_compose/`
- **Files:** `app.py`, `Dockerfile`, `docker-compose.yml`, `requirements.txt`
- **How to run:**

  ```bash
  cd Docker/docker_compose
  docker compose up --build
  ```

  The Flask service is exposed on port `5000`.

### 9. Flask Basics

- **Folder:** `Flase/`
- **Files:** `first.py`, `main.py`, `getpost.py`, `jinja.py`, `api.py`, plus HTML templates and a `sample.json`.
- **How to run** (each script is standalone):

  ```bash
  cd Flase
  pip install Flask
  python main.py
  ```

### 10. Ridge Regression Deployment Project (Algerian Forest Fires)

- **Purpose:** A Flask web app that predicts the Fire Weather Index using a trained Ridge regression model and a saved scaler.
- **Folder:** `Machine_learning/Supervised_ML/Linear_regression_Pritacle/ridge_lasso_elasticnet/Project_1/`
- **Main technologies:** Flask, scikit-learn, pandas, NumPy, Gunicorn.
- **Files:** `application.py`, `models/ridge.pkl`, `models/scaler.pkl`, `templates/home.html`, `templates/error.html`, `requirements.txt`, `.ebextensions/python.config` (AWS Elastic Beanstalk config), and `notebooks/Cross_validation.ipynb`.
- **How to run:**

  ```bash
  cd Machine_learning/Supervised_ML/Linear_regression_Pritacle/ridge_lasso_elasticnet/Project_1
  pip install -r requirements.txt
  python application.py
  ```

> See [Repository Notes](#repository-notes) before relying on links inside this folder.

---

## Learning Path

A suggested order for working through the repository:

1. **Python fundamentals** — `Python_basic/` (data types, loops, functions, lambda, iterators & decorators, exception handling, file handling, modules).
2. **OOP, logging and concurrency** — `Python_basic/OOPs/`, `Python_basic/Logging/`, `Python_basic/m_thread_and_m_process/`.
3. **Practice the basics** — `Practice_set/` (questions and solutions).
4. **NumPy and pandas** — `Analysis_with_python/numpy.ipynb` and `pandas/Pandas_day_1.ipynb`.
5. **Visualization** — `Analysis_with_python/Matplotlib.ipynb`, `Seaborn.ipynb`, `data_visualization/`.
6. **SQL basics from Python** — `Analysis_with_python/sqllite3.ipynb`.
7. **Feature engineering** — `Feature_engineering/` (encoding, missing values, imbalanced data, SMOTE).
8. **Supervised machine learning** — `Machine_learning/Supervised_ML/` from linear regression through to SVM and Naive Bayes.
9. **Ensemble methods** — `Machine_learning/Supervised_ML/bagging_boosting/`.
10. **Unsupervised machine learning** — `Machine_learning/Unsupervised_ML/` (K-Means, DBSCAN, hierarchical clustering, PCA, anomaly detection).
11. **Deep learning** — `Deep_Learning/Activation Function.ipynb`, then `Deep_Learning/ANN/Churn_prediction/`.
12. **NLP** — `NLP/Tokenization/` → `NLP/Bag_of_word/` → `NLP/TF-IDF/` → `NLP/word2vec/` → `NLP/Email_spam_classifier/`.
13. **Experiment tracking** — `MLflow/`.
14. **Containerization** — `Docker/Hello_World/`, then `Docker/docker_compose/`.
15. **Data storage** — `MongoDB/`.
16. **Web apps and deployment** — `Flase/` and `Streamlit/`.

---

## Practice

Practice material is concentrated in two places:

**`Practice_set/`** — question notebooks paired with solution notebooks:

| Folder | Topic |
| --- | --- |
| `advancefunctions/` | Advanced functions |
| `assignment_solution/` and `assignment_solutions/` | Mixed assignment sets |
| `dictionaries_assignment/` | Dictionaries |
| `exceptionhandlingsolution/` | Exception handling |
| `filehandlingquestions/` | File handling |
| `inheritancesolutions/` | Inheritance |
| `itergendecorsolutions/` | Iterators, generators and decorators |
| `list_assignment_solution/` | Lists |
| `numpypandasassignments/` | NumPy and pandas |
| `oopsquestion/` | Object-oriented programming |
| `packagessolution/` | Packages and modules |
| `set_assignments_solution/` | Sets |
| `tuple_assignment_solution/` | Tuples |

A good approach is to open the question notebook, attempt it yourself, then compare with the matching solution notebook.

**In-topic practice notebooks** — several folders include dedicated practice files, for example:

- `Python_basic/Practice1.ipynb`
- `NLP/Tokenization/practice_tokenization.ipynb`
- `Machine_learning/Supervised_ML/Linear_regression_Pritacle/practice_linear_regression.ipynb`
- `Python_basic/Logging/task_for_logging/` (task description plus solution script)

---

## Who Is This For?

- **Beginners learning Data Science** who want runnable, example-driven notebooks instead of pure theory.
- **Python learners** moving from language basics into data analysis and machine learning.
- **Students practicing Machine Learning** who want to see individual algorithms implemented one notebook at a time.
- **Developers exploring ML/MLOps** who want small, self-contained introductions to MLflow, Docker, Flask and Streamlit.
- **Anyone who wants a structured, hands-on Data Science repository** to read, run, and extend.

---

## How to Use This Repository

1. **Follow the folders progressively** — the structure roughly mirrors a learning path, so working from top to bottom avoids gaps.
2. **Read the notebooks** — markdown cells in the notebooks explain the concepts alongside the code.
3. **Run the examples locally** — activate your virtual environment and execute the cells to see the actual output and plots.
4. **Modify the code** — change hyperparameters, swap models, alter plots, and observe what changes.
5. **Complete the practice exercises** — attempt the question notebooks in `Practice_set/` before looking at the solutions.
6. **Build on the examples** — turn a notebook into a script, or reuse a trained model in a Flask or Streamlit app as done in this repository.
7. **Experiment with different datasets or models** — the datasets in the repository are small samples, so they are easy to replace with your own data.

---

## Repository Notes

A few things worth knowing before exploring:

- **No license file is included** in this repository, so the default "all rights reserved" applies. If you plan to reuse the material, please check with the author.
- **`Machine_learning/Supervised_ML/Linear_regression_Pritacle` is recorded in Git as a nested repository pointer (a gitlink), not as regular tracked files.** As a result, on GitHub this path may appear as a folder link rather than browsable file contents, and there is no `.gitmodules` file in the repository. If you need that material, use a local clone of this repository where the folder is present.
- **There is no root-level `requirements.txt`, `pyproject.toml`, `environment.yml`, `setup.py` or CI configuration.** Dependencies are declared per topic (see [Getting Started](#getting-started)).
- **Some notebooks contain saved outputs from the author's own machine**, so paths and package versions visible inside outputs may not match yours.
- **Naming is inconsistent in places** — for example the Flask folder is named `Flase/`, and several notebooks are named `Untitled.ipynb`. This is a learning repository rather than a packaged library.

---

## Contributing

This is primarily a personal learning repository, but suggestions, fixes and improvements are welcome.

```bash
git checkout -b feature/your-feature
git add .
git commit -m "Add your change"
git push origin feature/your-feature
```

Then open a pull request against the `main` branch and describe what you changed and why. For small corrections (typos, broken notebooks, clearer comments), feel free to open an issue instead.

---

## Author

**Madhav Kumar Yadav**

- GitHub: [@Madhavkumaryadav](https://github.com/Madhavkumaryadav)

---

## Repository Link

- **GitHub:** [https://github.com/Madhavkumaryadav/DataScience-Bootcamp](https://github.com/Madhavkumaryadav/DataScience-Bootcamp)

If you find this repository useful for your own learning, consider giving it a star.
