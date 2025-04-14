import pickle
import pandas as pd
import streamlit as st

# Load the trained model
model_file = '/workspaces/streamlit/models/decision_tree_classifier_default_42.sav'

with open(model_file, 'rb') as input_file:
    model = pickle.load(input_file)

# Dictionary for translating predictions
class_dict = {
    0: 'Not diabetic',
    1: 'Diabetic'}

# Page Configuration
st.set_page_config(
    page_title="Prediccion de Diabetes App",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# App Title and Description
st.title("aplicacion web de prediccion de diabetes")
st.markdown(
    """
    ### Bienvenidos! 🩺
    Esta aplicación predice si una persona es diabética basándose en los datos ingresados. Proporcione la información necesaria a continuación.
    """
)

# Sidebar Styling and Input Section
st.sidebar.header("Introduzca sus datos")
st.sidebar.markdown("### Rellene sus datos de salud:")

# Input Fields
glucose = st.sidebar.number_input('Nivel de Glucosa (mg/dL)', min_value=0, max_value=300, step=1, value=100, help="Enter glucose level.")
insulin = st.sidebar.number_input('Nivel de insulina (μIU/mL)', min_value=0, max_value=1000, step=1, value=50, help="Enter insulin level.")
bmi = st.sidebar.number_input('Indice de masa corporal (IMC)', min_value=0.0, max_value=70.0, step=0.1, value=25.0, help="Enter BMI value.")
age = st.sidebar.number_input('Edad(Años)', min_value=0, max_value=120, step=1, value=30, help="Enter your age.")
Pregnancies = st.sidebar.number_input('embarazos', min_value=0, max_value=30, step=1, value=0, help="Enter Pregnancies level.")
BloodPressure = st.sidebar.number_input('Presion sanguinea', min_value=0, max_value=140, step=1, value=50, help="Enter BloodPressure level.")
SkinThickness = st.sidebar.number_input('Grosor de la piel', min_value=0.0, max_value=70.0, step=0.1, value=25.0, help="Enter SkinThickness value.")
DiabetesPedigreeFunction = st.sidebar.number_input('Promedio antecedentes de diabetes en la familia', min_value=0.0, max_value=2.5, step=0.1, value=1.0, help="Enter DiabetesPedigreeFunction value.")
# Input Data Frame
input_data = pd.DataFrame({'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],'BloodPressure': [BloodPressure],'SkinThickness': [SkinThickness],'Pregnancies': [Pregnancies],'Glucose': [glucose],'Insulin': [insulin], 'BMI': [bmi], 'Age': [age]})

# Prediction Button
st.markdown("---")
if st.button("Predict"):
    try:
        # Prediction logic
        prediction = model.predict(input_data)[0]
        predicted_class = class_dict[prediction]

        # Display Results
        st.success(f"Prediction: {predicted_class}")
        if prediction == 1:
            st.warning("Consult a healthcare professional for further evaluation.")
        else:
            st.info("Maintain a healthy lifestyle to reduce risks.")
    except Exception as e:
        st.error(f"An error occurred while predicting: {e}")

# Footer
st.markdown("---")
st.markdown( """ ### Notes: 
    - Model trained with health-related data     
    - Ensure input values are within reasonable ranges.
    - Consult a healthcare provider for clinical advice.""")

# Styling with external CSS
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px; }</style>""",
    unsafe_allow_html=True)