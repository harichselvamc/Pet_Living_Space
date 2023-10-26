import streamlit as st
import pandas as pd
import joblib

# Mapping for features
size_mapping = {
    'Small': 0,
    'Medium': 1,
    'Large': 2
}

gender_mapping = {
    'Male': 0,
    'Female': 1,
}

vaccination_mapping = {
    'Vaccinated': 0,
    'Not Vaccinated': 1,
}

spaying_mapping = {
    'Spayed/Neutered': 0,
    'Not Spayed/Neutered': 1,
}

medical_history_mapping = {
    'Healthy': 0,
    'Minor Health Issues': 1,
    'Chronic Condition': 2,
}

location_mapping = {
    'Shelter': 0,
    'Rescue Organization': 1,
}

color_mapping = {
    'Brown': 0,
    'Black': 1,
    'White': 2,
    'Spotted': 3,
    'Mixed': 4,
}

special_characteristics_mapping = {
    'Playful': 0,
    'Calm': 1,
    'Loyal': 2,
    'Affectionate': 3,
    'Active': 4,
    'Aggressive': 5,
}

diet_mapping = {
    'Dry food': 0,
    'Canned food': 1,
    'Mixed diet': 2,
}

training_level_mapping = {
    'Basic': 0,
    'Advanced': 1,
    'None': 2,
}

# Mapping for pet types
pet_type_mapping = {
    'Dog': 0,
    'Cat': 1,
    'Rabbit': 2,
    'Turtle': 3,
    'Lizard': 4,
    'Chameleon': 5,
    'Crocodile': 6,
    'Frog': 7,
    'Gecko': 8,
    'Iguana': 9,
    'Salamander': 10,
    'Snake': 11,
    'Toad': 12,
    'Tortoise': 13,
}

# Mapping for living conditions
living_condition_mapping = {
    0: 'Apartment',
    1: 'Farm',
    2: 'Indoor',
    3: 'Outdoor',
    4: 'House',
}

# Load the saved Decision Tree model
model_filename = 'decision_tree_model.pkl'
loaded_model = joblib.load(model_filename)

# Streamlit setup
st.title('Pet Living Condition Prediction App')


pet_type = st.selectbox('Pet Type', list(pet_type_mapping.keys()))
age = st.slider('Age', 1, 20, 1)
owner= st.slider('Previous Owners', 1, 3, 1)
size = st.selectbox('Size', list(size_mapping.keys()))
gender = st.selectbox('Gender', list(gender_mapping.keys()))
vaccination_status = st.selectbox('Vaccination Status', list(vaccination_mapping.keys()))
spaying_status = st.selectbox('Spaying/Neutering Status', list(spaying_mapping.keys()))
medical_history = st.selectbox('Medical History', list(medical_history_mapping.keys()))
location = st.selectbox('Location', list(location_mapping.keys()))
color = st.selectbox('Color', list(color_mapping.keys()))
weight = st.number_input('Weight (kg)', value=1, step=1)
special_characteristics = st.selectbox('Special Characteristics', list(special_characteristics_mapping.keys()))
diet = st.selectbox('Diet', list(diet_mapping.keys()))
training_level = st.selectbox('Training Level', list(training_level_mapping.keys()))

# Create input data as a dictionary
input_data = {
    'Pet Type': [pet_type_mapping[pet_type]],
    'Age': [age],
    'Size': [size_mapping[size]],
    'Gender': [gender_mapping[gender]],
    'Vaccination Status': [vaccination_mapping[vaccination_status]],
    'Spaying/Neutering Status': [spaying_mapping[spaying_status]],
    'Medical History': [medical_history_mapping[medical_history]],
    'Location': [location_mapping[location]],
    'Color': [color_mapping[color]],
    'Weight (kg)': [weight],
    'Special Characteristics': [special_characteristics_mapping[special_characteristics]],
     'Previous Owners':[owner],
    'Diet': [diet_mapping[diet]],
    'Training Level': [training_level_mapping[training_level]]
}

# Create a DataFrame for the input data
input_df = pd.DataFrame(input_data)

# Create a button to make predictions
if st.button('Predict Living Condition'):
    # Predict with the Decision Tree model
    predicted_class = loaded_model.predict(input_df)

    # Get the predicted living condition label
    predicted_condition_label = living_condition_mapping.get(predicted_class[0], 'Unknown')

    # Display the prediction result
    st.write(f'Predicted Living Condition: {predicted_condition_label}')
