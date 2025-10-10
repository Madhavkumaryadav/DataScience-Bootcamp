import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names


df, target_name = load_data()

# Train model (use a fixed random_state for reproducibility)
model = RandomForestClassifier(random_state=42)
model.fit(df.iloc[:, :-1], df['species'])

# Sidebar inputs (use exact column names from the dataframe)
sepal_length = st.sidebar.slider(
    label=str(df.columns[0]),
    min_value=float(df[df.columns[0]].min()),
    max_value=float(df[df.columns[0]].max()),
    value=float(df[df.columns[0]].mean()),
)
sepal_width = st.sidebar.slider(
    label=str(df.columns[1]),
    min_value=float(df[df.columns[1]].min()),
    max_value=float(df[df.columns[1]].max()),
    value=float(df[df.columns[1]].mean()),
)
petal_length = st.sidebar.slider(
    label=str(df.columns[2]),
    min_value=float(df[df.columns[2]].min()),
    max_value=float(df[df.columns[2]].max()),
    value=float(df[df.columns[2]].mean()),
)
petal_width = st.sidebar.slider(
    label=str(df.columns[3]),
    min_value=float(df[df.columns[3]].min()),
    max_value=float(df[df.columns[3]].max()),
    value=float(df[df.columns[3]].mean()),
)


## Prediction
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(input_data)
# prediction is an array like [0] — pick the first element
predicted_species = target_name[int(prediction[0])]

# App UI
st.title('Iris Species Prediction')
st.write('Use the sidebar to set feature values, then see the predicted species below.')
st.write('Input values:')
st.write({'sepal_length': sepal_length, 'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width})

st.success(f'Predicted species: {predicted_species}')

