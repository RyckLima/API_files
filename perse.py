import requests 
import os

file_name = 'name.pdf'
path = os.path.join('uploads' , file_name)
api_key = 'llx-rW7ACedLCrKxe07hcxTOyg090kRSKZhdr96TACPDyNdqOoIC'

with open(path , 'rb') as f:
    
    response = requests.post(url = 'https://api.cloud.llamaindex.ai/api/v1/parsing/upload', 
                    headers = {
                        'accept' : 'application/json' , 
                        'Content-Type' : 'multipart/form-data' ,
                        'Authorization' : f'Bearer {api_key}' },
                    data = {
                        'language' : 'pt'},
                    file = f
                    )

response2 = requests.get(url = 'https://api.cloud.llamaindex.ai/api/v2/parse/:job_id',
                        headers = {
                        'accept' : 'application/json' ,
                        'Authorization' : f'Bearer {api_key}' }
                        )

