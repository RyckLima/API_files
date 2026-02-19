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


while True:
    response2 = requests.get(url = f'https://api.cloud.llamaindex.ai/api/v1/parsing/job/{job_id}',
                            headers = {
                            'accept' : 'application/json' ,
                            'Authorization' : f'Bearer {api_key}' }
                            )
    
    dados = response2.json()
    status = dados.get('status')
    print(dados)

    if status == 'SUCCESS': # Ou o status final indicado na doc da v2
        # SÓ AQUI as chaves 'text' e 'metadata' vão existir!
        texto = dados.get('text')
        with open( path2 , 'w') as f:
            f.write(f' Aqui estão os dados: {texto}')
        break
    elif status == 'FAILED':
        print("Erro no processamento")
        break
    
    time.sleep(2)

    


