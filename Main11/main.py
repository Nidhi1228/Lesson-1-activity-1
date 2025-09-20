from concept import API_KEY
import requests 
api_url = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"
headers = {

         "Authorization": f"Bearer {API_KEY}"

}

# Text to classify (example sentence)

text = "I love learning about AI! It's so fascinating."

# Make a POST request to the Hugging Face API

response = requests.post(api_url, headers=headers, json={"inputs": text})

if response.status_code == 200:

# Parse and print the results

    classification = response.json()

# print(classification)

    print("Predicted label:", classification[0][0]['label'])

    print("Confidence:", classification[0][0]['score'])

else:

            print(f"Error: {response.status_code}")