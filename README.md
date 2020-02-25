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
6. Execute os testes.
7. Execute o servidor.
```
git clone git@github.com:ffabiorj/acai_api.git
cd acai
python3 -m venv .venv
sourch .venv/bin/activate
pip install -r requirements-dev.txt
renomei exemplo_.env para .env
python manage.py test
python manage.py runserver
```