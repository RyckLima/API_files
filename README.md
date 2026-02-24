API de Extração de Metadados PDF 📄
API Flask que recebe um arquivo PDF via POST, envia para o LlamaCloud e retorna os dados estruturados em JSON.

#Instalação
Ative seu ambiente virtual (venv).

Instale as dependências:

Bash
pip install flask requests python-dotenv
Crie um arquivo .env e adicione sua chave:

Plaintext
LLAMA_API_KEY=sua_chave_aqui

# Como usar
Inicie a API: python api.py.

No Postman, envie um POST para /parse:

Aba Body > form-data.

Chave: file (tipo File).

Valor: selecione seu PDF.

# Funcionamento
Upload: Salva o arquivo em ./uploads temporariamente.

Polling: Consulta o status do processamento a cada 2 segundos até concluir.

Resposta: Retorna o JSON com job_metadata e o conteúdo das páginas.