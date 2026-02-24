Reestruturação do projeto, correções a serem feitas:

PROPOSTA: A API recebe um arquivo qualquer, dai, esse arquivo é enviado para API do Llama, cria o JOB, e depois espera um pouco para dar um GET usando o job_id


1. Adicionar .gitignore, evitar subir pycache / venv ,etc.
SEMPRE ATIVE AO CRIAR O REPOSITÓRIO
2. Uploads não faz sentido no repositório. O FOCO DO REPOSITÓRIO É A API. 
3. Outputs não faz sentido. Pois o JSON é para ser gerado na resposta.
4. API RESTFul retorna um JSON / XML na resposta , não um HTML como no nosso caso. 
5. view.py não faz sentido 
6.  O tipo de informação que queremos é metadados tipo ADOBE. 
Esses metadados nem precisam ser pegos da API do Llama.
esses que eu coloquei são insuficientes.
7. Ao invés de usar base.txt , o padrão é README.md
8. O metódo deve ser usado apenas o POST, para receber o PDF.
9. A função para puxar as coisas da API do Llama é para ser usada dentro do upload_file() por meio de requests
10. API key tem que estar em um arquivo .env, e usar a biblioteca dotenv
11. Ajeitar o nome do arquivo ,só '/' não quer dizer muita coisa.
12. READ pode pedir pro gpt pra o projeto.
