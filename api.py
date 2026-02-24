import  os 
from  flask  import  Flask , jsonify,  request ,  redirect ,  url_for 
from  werkzeug.utils  import  secure_filename
from  flask  import  send_from_directory
from dotenv import load_dotenv
import requests
import time

load_dotenv()

api_key = os.getenv('LLAMA_API_KEY')
UPLOAD_FOLDER  =  './uploads' 
ALLOWED_EXTENSIONS = {'pdf'}
headers = {'accept' : 'application/json' ,
           'Authorization' : f'Bearer {api_key}' }

app  =  Flask ( __name__ ) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
app.config['MAX_CONTENT_LENGHT']= 16*1000*1000


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/parse', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}) , 400
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '': 
            return jsonify({'error': 'No file selected'}) , 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            path = os.path.join('uploads' , filename)

            with open(path , 'rb') as f:
                response = requests.post(url = 'https://api.cloud.llamaindex.ai/api/v1/parsing/upload', 
                    headers = headers,
                    data = {
                        'language' : 'pt'},
                    files = {'file' : f}
                    )
            job_id  = response.json()['id']

            #Polling (para resolver o assincronismo na API da web)
            while True:

                response_job = requests.get(url = f'https://api.cloud.llamaindex.ai/api/v1/parsing/job/{job_id}',
                                        headers = headers
                                        )
                response_job_result = requests.get(url = f'https://api.cloud.llamaindex.ai/api/v1/parsing/job/{job_id }/result/json',
                                        headers = headers
                                        )


                status  = response_job.json().get('status')
                print(status)

                if status == 'SUCCESS' : #se os status tiver ok pode prosseguir
                    return jsonify(response_job_result.json()) , 200
                elif status == 'FAILED' :
                    return jsonify({'error' : 'Erro no processamento'}) , 400
                
                time.sleep(2)
                             
if __name__ == '__main__':
    app.run(debug=True)