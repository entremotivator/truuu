import streamlit as st
import requests

def fetch_data(api_key):
    # Replace 'YOUR_TRUERA_API_ENDPOINT' with the actual TruEra API endpoint
    api_endpoint = 'YOUR_TRUERA_API_ENDPOINT'
    
    # Replace 'YOUR_TRUERA_API_KEY' with the provided API key
    headers = {'Authorization': f'Bearer {api_key}'}
    
    # Make a GET request to the TruEra API
    response = requests.get(api_endpoint, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error(f"Error fetching data: {response.status_code} - {response.text}")
        return None

def main():
    st.title("TruEra API Data Display")
    
    # Input API key from the user
    api_key = st.text_input("Enter TruEra API Key:")
    
    if api_key:
        # Fetch data using the provided API key
        data = fetch_data(api_key)
        
        if data:
            # Display the fetched data
            st.write("Fetched Data:")
            st.write(data)
    
if __name__ == "__main__":
    main()
