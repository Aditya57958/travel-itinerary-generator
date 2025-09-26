import requests
import os

# API Configuration
try:
    api_key = os.environ["sk-igUDB1syx8WueaauQk6R5p6wwL0hzdB8eeGsZuZG3Xw"]
except KeyError:
    raise ValueError("LANGFLOW_API_KEY environment variable not found. Please set your API key in the environment variables.")

url = "http://localhost:7860/api/v1/run/866fbfbc-2186-4ff9-b520-e452fd54d529"  # The complete API endpoint URL for this flow

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "Create a travel itinerary for a trip from São Paulo to Uberlândia, MG on August 23, 2024. The traveler enjoys drinking beer, eating pão de queijo, and drinking special coffee."
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key  # Authentication key from environment variable
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")