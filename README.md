Python XP
==========
Códigos utilizados na apresentação da palestra [Desacoplando seus testes com HTTPretty](https://www.youtube.com/watch?v=-nVfdy7TWHU).

Como preparar o ambiente
------------------------
Você vai precisar ter instalado Python na versão 3.5, 3.6 ou 3.7. O pacote que utilizaremos (HTTPretty) ainda não tem um bom suporte para versão 3.8. Feito isto, você vai precisar de um ambiente virtual criado:

```bash
➜ python -m venv .venv
```

Instalar as dependências do projeto:
```bash
➜ pip install -r requirements.txt
```

E pronto, já pode brincar a vontade! :smiley:

Para poder executar os exemplos 2 e 3, você vai precisar rodar o `app.py` que está no diretório `shipping-api`. É um projeto criado com o [`Chalice`](https://aws.github.io/chalice/). Para deixar ele rodando localmente, tudo que você precisa fazer é entrar no diretório e executar o seguinte comando em um terminal separado:

```bash
➜ chalice local
```

Como rodar os testes?
---------------------
Tudo o que você precisa fazer, é executar o comando `pytest` passando para ele o caminho onde o teste que você quer executar está. Por exemplo:

```bash
➜ pytest product_example_2/test_order.py
```

Como preparar o ambiente com Docker
---------------------------
Adicionei no repositório um `Dockerfile` e um `docker-compose.yml` caso queira subir o ambiente com Docker. Para isso, você vai precisar instalar o [Docker](https://docs.docker.com/engine/installation/) e o [Docker-Compose](https://docs.docker.com/compose/install/).

Primeiramente vamos "buildar" o serviço `python-xp` com o comando `docker-compose build`. Quando finalizar, estaremos prontos para rodar os primeiros comandos usando o `run` como atalho.

- para ter acesso ao bash dentro do container, basta executar: `./run bash`. A partir daí, você vai poder executar os testes.