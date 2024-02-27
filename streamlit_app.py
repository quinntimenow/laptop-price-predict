import streamlit as st
import pandas as pd
import joblib

# Function to load the trained model
def load_model():
    model_path = 'laptop_price_prediction_model.joblib'
    model = joblib.load(model_path)
    return model

model = load_model()

def main():
    st.title('Laptop Price Predictor')

    # User inputs for available features
    brand = st.selectbox('Brand', ['Apple', 'Dell', 'Lenovo', 'HP', 'Asus'])
    processor_type = st.selectbox('Processor Type', ['Intel Core i7', 'Intel Core i5', 'AMD Ryzen'])
    ram = st.selectbox('RAM', ['8GB', '16GB', '32GB'])
    storage = st.selectbox('Storage', ['256GB SSD', '512GB SSD', '1TB HDD'])
    screen_size = st.selectbox('Screen Size', ['13"', '15"', '17"'])

    # Placeholder values for other required features not collected from the user
    placeholders = {
        'TypeName': 'Ultrabook',  # Example placeholder
        'Company': brand,  # Dynamically use the brand as company
        'Cpu': processor_type,  # Use processor type for CPU
        'Weight': '1.5',  # Example weight
        'laptop_ID': 1,  # Example laptop ID
        'OpSys': 'Windows',  # Operating system
        'Inches': float(screen_size.strip('"')),  # Convert screen size to float
        'Ram': ram,  # Use user input for RAM
        'Memory': storage,  # Use storage as memory
        'Product': 'Generic Model',  # Example product model
        'Gpu': 'Integrated',  # Example GPU
        'ScreenResolution': '1920x1080'  # Example screen resolution
    }

    # Convert placeholders into DataFrame for prediction
    input_df = pd.DataFrame([placeholders])

    if st.button('Predict Price'):
        # Make prediction
        predicted_price = model.predict(input_df)[0]

        # Display prediction
        st.success(f'Predicted Laptop Price: ${predicted_price:.2f}')

if __name__ == '__main__':
    main()
  
