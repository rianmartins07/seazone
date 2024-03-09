# Configuração do Ambiente

1. Inicie criando um ambiente de desenvolvimento:
    <strong>python -m venv venv</strong>


2. Instale as dependências do projeto:
    <strong>pip install -r requirements.txt</strong>


# Configuração do Banco de Dados

1. Crie um banco de dados no PostgreSQL utilizando o pgAdmin. Configure o endereço, porta e usuário conforme necessário.

2. Crie um arquivo `.env` a partir do `.env.example`, alterando as informações de acordo com as configurações locais.

3. Com o banco criado e o `.env` configurado corretamente, realize as tratativas e migrações do banco:

## Migrando as configurações do banco de dados:
    <strong>python manage.py migrate</strong>


## Rodando as fixtures (dados para dentro do banco de dados):
    <strong>python manage.py loaddata fixture/imoveis.json;</strong>
    <strong>python manage.py loaddata fixture/plataformas.json;</strong>
    <strong>python manage.py loaddata fixture/anuncios.json;</strong>
    <strong>python manage.py loaddata fixture/reserva.json;</strong>


# Executando o Servidor

Para rodar o servidor e garantir seu correto funcionamento:
    <strong>python manage.py runserver</strong>


Acesse o domínio da aplicação que será exibido no terminal e visite o seguinte URL:
    <strong>http://seu_dominio.com.br/api</strong>


Neste endereço, você terá acesso a todas as interfaces de consumo, criação, alteração e deleção de dados de acordo com o estabelecido no arquivo.

# Testes Automatizados

Para realizar os testes automatizados, utilize o seguinte comando:
    <strong>python manage.py test</strong>

É de suma importância rodar esse comando toda a vez que for realizado alguma feature/fix no projeto.



