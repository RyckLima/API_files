import  os 
from  flask  import  Flask ,  request ,  redirect ,  url_for 
from  werkzeug.utils  import  secure_filename

UPLOAD_FOLDER  =  '/caminho/para/os/uploads' 
ALLOWED_EXTENSIONS  =  set ([ 'txt' ,  ' pdf ' ,  'png' ,  'jpg' ,  'jpeg' ,  'gif' ])

app  =  Flask ( __name__ ) 
app.config[ ' UPLOAD_FOLDER ' ] = UPLOAD_FOLDER 

def  allowed_file ( filename ): #Verificação se uma função é válida.
    return  '.'  in  filename  and \
            filename . rsplit ( '.' ,  1 )[ 1 ]  in  ALLOWED_EXTENSIONS


          