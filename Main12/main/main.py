from concept import API_KEY
import requests 
# api_url = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"
api_url = "https://api-inference.huggingface.co/models/siebert/sentiment-roberta-large-english"
headers = {

         "Authorization": f"Bearer {API_KEY}"

}

# Text to classify (example sentence)

text = input("enter your text here:  ")

# Make a POST request to the Hugging Face API

response = requests.post(api_url, headers=headers, json={"inputs": text})
# print(response.json())

if response.status_code == 200:
    reply = (response.json())
    print(reply[0][0]["label"])
    print(reply[0][0]["score"])
else:
    print("Not valid",response.status_code)

