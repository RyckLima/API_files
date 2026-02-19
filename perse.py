import requests 
import os

file_name = 'name.pdf'
path = os.path.join('uploads' , file_name)

with open(path , 'rb') as f:
    api_key = 'llx-rW7ACedLCrKxe07hcxTOyg090kRSKZhdr96TACPDyNdqOoIC'
    response = requests.post(url = 'https://api.cloud.llamaindex.ai/api/v1/parsing/upload', 
                    headers = {
                        'accept' : 'application/json' , 
                        'Content-Type' : 'multipart/form-data' ,
                        'Authorization' : f'Bearer {api_key}' },
                    data = {
                        'language' : 'pt'},
                    file = f,
                    )

