# API DE AÇAÍ.

### TECNOLOGIAS UTILIZADAS.
* Django
* Django Rest Framework
* Python Decouple

###
Como utilizar esse projeto
1. Clonar o repósitorio
2. Crie um virtualenv com python 3.7
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
8. Execute o servidor.
```
git clone git@github.com:ffabiorj/acai_api.git
cd acai
python3 -m venv .venv
sourch .venv/bin/activate
pip install -r requirements-dev.txt
renomei exemplo_.env para .env
python manage.py runserver
```

## Endpoints da api

```
http://127.0.0.1:8000/api/v1/acai/
http://127.0.0.1:8000/api/v1/acai/<id>
http://127.0.0.1:8000/api/v1/personalizacao/
http://127.0.0.1:8000/api/v1/personalizacao/<id>
http://127.0.0.1:8000/api/v1/pedido/
http://127.0.0.1:8000/api/v1/pedido/<id>

```

## Para fazer o method POST:

```
Exemplo: 
Acai
{
    "tamanho": "médio (ml500)",
    "sabor": "banana"
}
Personalizacao
{
    "acai": id-acai
    "personalizacao": "granola"
}
Pedido
{
    "pedido": id-acai
}

```
