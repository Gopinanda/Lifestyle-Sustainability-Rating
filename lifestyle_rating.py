import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open(r"Sustainability_rating.pkl",'rb'))

st.image("innomatics-research-labs-logo-squared.png")
st.title("Lifestyle Sustainability Rating")

numerical_features = ['Age', 'HomeSize', "MonthlyElectricityConsumption", "MonthlyWaterConsumption"]  
categorical_features = {
    'Gender': ['Female', 'Male', 'Non-Binary', 'Prefer not to say'],
    'Location': ['Urban', 'Suburban', 'Rural'], 
    'DietType': ['Mostly Plant-Based', 'Balanced', 'Mostly Animal-Based'],  
    'LocalFoodFrequency': ['Rarely', 'Sometimes', 'Often', 'Always'],  
    'TransportationMode': ['Car', 'Bike', 'Public Transport', 'Walking'],  
    'EnergySource': ['Renewable', 'Non-renewable', 'Mixed'],  
    'HomeType': ['Apartment', 'House', 'Other'],  
    'ClothingFrequency': ['Rarely', 'Sometimes', 'Often', 'Always'],  
    'SustainableBrands': [ True, False],  
    'CommunityInvolvement':  ['Low', 'Moderate', 'High'],  
    'UsingPlasticProducts': ['Never', 'Rarely', 'Sometimes', 'Often'],  
    'DisposalMethods': ['Recycling', 'Composting', 'Trash'],  
    'PhysicalActivities': ['Low', 'Moderate', 'High']  
}

input_data = {}
for feature in numerical_features:
    input_data[feature] = st.number_input(f'Enter value for {feature}',min_value=0, step=1,format="%d")

def slider_color(value):
    color = {
        1: '#FF0000',  # Red
        2: '#FF7F00',  # Orange
        3: '#FFFF00',  # Yellow
        4: '#7FFF00',  # Lime Green
        5: '#00FF00',  # Green
    }.get(value, '#00FF00')  # Default color (Green)

    return f"""
    <style>
    div[data-testid="stSlider"] div[role="slider"] {{
        background-color: {color};  /* Thumb color */
    }}
    div[data-testid="stSlider"] .st-cb {{
        background: linear-gradient(90deg, {color} {value*20}%, #d3d3d3 {value*20}%);  /* Track color */
    }}
    </style>
    """

st.write('On The Scale of 1 to 5, Please Rate Your Environmental Awareness')

input_value = st.slider('Rate : ', min_value=1, max_value=5)
st.markdown(slider_color(input_value), unsafe_allow_html=True)
input_data['EnvironmentalAwareness'] = int(input_value)

for feature, options in categorical_features.items():
    input_data[feature] = st.selectbox(f'Select {feature}', options)

input_df = pd.DataFrame([input_data])

if st.button('Predict'):
    prediction = model.predict(input_df)

    if prediction[0]==1:
        st.write(f'Prediction: {prediction[0]}')
        st.write('Consider making significant changes to your lifestyle to enhance sustainability.')
        st.image("1_rating.jpg")

    elif prediction[0]==2:
        st.write(f'Prediction: {prediction[0]}')
        st.write("You're on the right path but there's room for improvement.")
        st.image("2_rating.jpg")

    elif prediction[0]==3:
        st.write(f'Prediction: {prediction[0]}')
        st.write("You have a good foundation, but there's potential to do even better.")
        st.image("3_rating.jpg")

    elif prediction[0]==4:
        st.write(f'Prediction: {prediction[0]}')
        st.write("Great job! You're making significant strides toward a sustainable lifestyle.")
        st.image("4_rating.jpg")

    else:
        st.write(f'Prediction: {prediction[0]}')
        st.write("Outstanding! You're a role model for sustainable living.")
        st.image("5_rating.jpg")

    

    
 
