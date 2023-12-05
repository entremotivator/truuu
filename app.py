import streamlit as st
import requests
from truera.client.truera_workspace import TrueraWorkspace
from truera.client.truera_authentication import TokenAuthentication

# Replace these placeholders with your actual TruEra URL and token
TRUERA_URL = "<YOUR_TRUERA_URL>"
TOKEN = "<YOUR_TRUERA_TOKEN>"

auth = TokenAuthentication(TOKEN)
tru = TrueraWorkspace(TRUERA_URL, auth)

def fetch_data(api_key, endpoint):
    # Replace 'YOUR_TRUERA_API_ENDPOINT' with the actual TruEra API endpoint
    api_endpoint = f'{TRUERA_URL}/{endpoint}'
    
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
        st.subheader("Example Endpoints:")
        for i in range(1, 11):
            endpoint = f"example_endpoint_{i}"
            st.write(f"Endpoint {i}: {endpoint}")
            data = fetch_data(api_key, endpoint)
            
            if data:
                # Display the fetched data for each endpoint
                st.write(f"Fetched Data for Endpoint {i}:")
                st.write(data)

if __name__ == "__main__":
    main()
