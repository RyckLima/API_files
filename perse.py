import requests 
import os
import time

file_name = 'SIMITA1aFASE-07022026-C0.pdf'
path = os.path.join('uploads' , file_name)
api_key = 'llx-rW7ACedLCrKxe07hcxTOyg090kRSKZhdr96TACPDyNdqOoIC'

with open(path , 'rb') as f:
    
    response = requests.post(url = 'https://api.cloud.llamaindex.ai/api/v1/parsing/upload', 
                    headers = {
                        'accept' : 'application/json' ,
                        'Authorization' : f'Bearer {api_key}' },
                    data = {
                        'language' : 'pt'},
                    files = {'file' : f}
                    )


job_id  = response.json()['id']
path2 = os.path.join('outputs' , f'{job_id}.json')

#Polling (para resolver o assincronismo na API da web)
while True:
    response_text = requests.get(url = f'https://api.cloud.llamaindex.ai/api/v1/parsing/job/{job_id}/result/text',
                            headers = {
                            'accept' : 'application/json' ,
                            'Authorization' : f'Bearer {api_key}' }
                            )
    response_metadata = requests.get(url = f'https://api.cloud.llamaindex.ai/api/v1/parsing/job/{job_id}/result/json',
                            headers = {
                            'accept' : 'application/json' ,
                            'Authorization' : f'Bearer {api_key}' }
                            )


    dados_text = response_text.json()
    dados_metadata = response_metadata.json()
    status1 = dados_text.get('status')
    status2 = dados_metadata.get('status')
    print(dados_text)

    if status1 == 'SUCCESS' and status2 == 'SUCCESS' : #se os status tiver ok pode prosseguir
        texto = dados_text.get('text')
        metadados = dados_metadata.get('job_metadata')
        with open( path2 , 'w') as f:
            f.write(f'Aqui está os metadados: Aqui está o texto: {texto}\n')
        break
    elif status1 == 'FAILED' or status2 == 'FAILED' :
        print("Erro no processamento")
        break
    
    time.sleep(2)

    


