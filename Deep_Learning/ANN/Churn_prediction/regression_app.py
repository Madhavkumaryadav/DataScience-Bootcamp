import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

st.set_page_config(
    page_title="Customer Salary Prediction",
    page_icon="📊",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Styling (high contrast so every input and value is clearly readable)
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    :root {
        --navy: #0B2545;
        --blue: #1F4E8C;
        --blue-dark: #163B6B;
        --text: #111827;
        --muted: #4B5563;
        --border: #8896A8;
        --panel: #F1F4F8;
        --green: #166534;
    }

    html, body, [class*="css"], .stApp {
        font-family: 'Inter', 'Segoe UI', sans-serif;
        color: var(--text);
    }
    .stApp { background: #FFFFFF; }
    #MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }
    .block-container { padding-top: 1.6rem; padding-bottom: 3rem; max-width: 1150px; }

    /* Title */
    .title {
        font-size: 1.9rem; font-weight: 700; color: var(--navy);
        letter-spacing: -0.02em; line-height: 1.2; padding-top: .4rem;
    }

    /* Section headings */
    .section {
        background: var(--navy); color: #FFFFFF;
        font-size: 1rem; font-weight: 600;
        padding: .6rem 1rem; border-radius: 6px;
        margin: 1.4rem 0 .9rem 0;
    }

    /* Labels: dark and bold so each field is clearly named */
    [data-testid="stWidgetLabel"] p {
        font-size: .95rem !important;
        font-weight: 600 !important;
        color: var(--text) !important;
    }

    /* Input boxes: white fill, dark text, clear border */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background: #FFFFFF !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 6px !important;
        min-height: 44px;
    }
    div[data-baseweb="input"] input,
    div[data-testid="stNumberInput"] input {
        color: var(--text) !important;
        -webkit-text-fill-color: var(--text) !important;
        background: #FFFFFF !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
    }
    div[data-baseweb="select"] div,
    div[data-baseweb="select"] span {
        color: var(--text) !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
    }
    div[data-baseweb="select"] svg { fill: var(--text) !important; }
    div[data-testid="stNumberInput"] button {
        background: var(--panel) !important; color: var(--text) !important;
    }
    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="select"] > div:focus-within {
        border-color: var(--blue) !important;
        box-shadow: 0 0 0 3px rgba(31, 78, 140, .25) !important;
    }

    /* Dropdown list */
    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] li {
        background: #FFFFFF !important;
        color: var(--text) !important;
    }
    div[data-baseweb="popover"] li:hover { background: var(--panel) !important; }

    /* Sliders: visible value and min/max */
    div[data-testid="stSlider"] [data-testid="stThumbValue"] {
        color: var(--blue-dark) !important; font-weight: 700; font-size: .95rem;
    }
    div[data-testid="stSlider"] [data-testid="stTickBarMin"],
    div[data-testid="stSlider"] [data-testid="stTickBarMax"] {
        color: var(--muted) !important; font-weight: 500;
    }
    div[data-testid="stSlider"] [role="slider"] { background: var(--blue) !important; }

    /* Predict button */
    div.stButton > button {
        width: 100%;
        background: var(--blue); color: #FFFFFF;
        border: none; border-radius: 6px;
        padding: .8rem 1rem; font-size: 1.05rem; font-weight: 600;
        margin-top: 1.4rem;
    }
    div.stButton > button:hover { background: var(--blue-dark); color: #FFFFFF; }
    div.stButton > button p { color: #FFFFFF !important; }

    /* Prediction report (top right) */
    .report {
        border: 2px solid var(--navy);
        border-radius: 10px;
        overflow: hidden;
        background: #FFFFFF;
    }
    .report-head {
        background: var(--navy); color: #FFFFFF;
        padding: .45rem 1rem; font-size: .9rem; font-weight: 600;
    }
    .report-body { display: flex; align-items: center; gap: 1rem; padding: .9rem 1rem; }
    .report-icon {
        width: 46px; height: 46px; border-radius: 50%;
        background: #DCFCE7; color: var(--green);
        display: flex; align-items: center; justify-content: center;
        font-size: 1.4rem; flex-shrink: 0;
    }
    .report-label { color: var(--muted); font-size: .85rem; font-weight: 600; }
    .report-value {
        color: var(--navy); font-size: 1.9rem; font-weight: 700;
        line-height: 1.15; font-variant-numeric: tabular-nums;
    }
    .report-empty { color: var(--muted); font-size: 1.05rem; font-weight: 500; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Load the trained model
# ---------------------------------------------------------------------------
model = tf.keras.models.load_model('regression_model.h5')

# load encoder and scaler
with open('gender_encode.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('geo_encode.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('scaler_reg.pkl', 'rb') as file:
    scaler = pickle.load(file)

# ---------------------------------------------------------------------------
# Header: title (left) and prediction report (top right)
# ---------------------------------------------------------------------------
head_left, head_right = st.columns([3, 2], gap="large")
with head_left:
    st.markdown('<div class="title">📊 Customer Salary Prediction</div>', unsafe_allow_html=True)
with head_right:
    report_slot = st.empty()

yes_no = lambda v: "Yes" if v == 1 else "No"

# ---------------------------------------------------------------------------
# User input
# ---------------------------------------------------------------------------
st.markdown('<div class="section">Customer Details</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3, gap="large")
with c1:
    geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
with c2:
    gender = st.selectbox('Gender', label_encoder_gender.classes_)
with c3:
    age = st.slider('Age', 18, 92)

st.markdown('<div class="section">Financial Details</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2, gap="large")
with c1:
    credit_score = st.number_input('Credit Score')
with c2:
    balance = st.number_input('Balance')

st.markdown('<div class="section">Account Details</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2, gap="large")
with c1:
    tenure = st.slider('Tenure', 0, 10)
with c2:
    num_of_products = st.slider('Number Of Products', 1, 4)

c1, c2, c3 = st.columns(3, gap="large")
with c1:
    has_cr_card = st.selectbox('Has Credit Card', [0, 1], format_func=yes_no)
with c2:
    is_active_member = st.selectbox('Is Active Member', [0, 1], format_func=yes_no)
with c3:
    exited = st.selectbox('Exited', [0, 1], format_func=yes_no)

predict_clicked = st.button('📈  Predict Salary', type="primary")

'''
# input order :-
CreditScore
Gender
Age
Tenure
Balance
NumOfProducts
HasCrCard
IsActiveMember
Exited
Geography_France
Geography_Germany
Geography_Spain
'''

## Prepare the input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'Exited': [exited]
})

## One-hot encode 'Geography'
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

## Combine one-hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)

## Predict salary
prediction = model.predict(input_data_scaled)

# ---------------------------------------------------------------------------
# Prediction report (top right)
# ---------------------------------------------------------------------------
if predict_clicked:
    body = f"""
        <div class="report-icon">💰</div>
        <div>
            <div class="report-label">Estimated Salary</div>
            <div class="report-value">{prediction[0][0]:,.2f}</div>
        </div>
    """
else:
    body = '<div class="report-empty">Fill in the details and click Predict Salary.</div>'

report_slot.markdown(
    f"""
    <div class="report">
        <div class="report-head">Prediction Report</div>
        <div class="report-body">{body}</div>
    </div>
    """,
    unsafe_allow_html=True,
)