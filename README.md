# Projeto Docker Flask-psql

Este projeto consiste em uma aplicação web simples desenvolvida com Flask, que se conecta a um banco de dados PostgreSQL. A aplicação permite aos usuários visualizar e adicionar registros a uma tabela exemplo, que contém informações sobre diversos itens. A configuração e execução do serviço é feita utilizando Docker.

<img src="https://flask.palletsprojects.com/en/3.0.x/_images/flask-horizontal.png" width="100" alt="Flask"> <img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/postgresql_original_wordmark_logo_icon_146392.png" width="100" alt="PostgreSQL"> <img src="https://cdn.icon-icons.com/icons2/2107/PNG/512/file_type_docker_icon_130643.png" width="100" alt="Docker">



## Pré-Requisitos

Antes de começar, você precisará ter o Docker instalado em sua máquina. Se você ainda não tem o Docker, pode baixá-lo e instalá-lo a partir do [Docker Desktop](https://www.docker.com/products/docker-desktop). Siga as instruções de instalação específicas para o seu sistema operacional.

## Configuração Inicial

Antes de executar o projeto, você precisa configurar algumas variáveis de ambiente que serão usadas pelo Docker Compose para configurar os serviços de aplicação e banco de dados (a configuração de exemplo atual pode ser mantida, pois funciona, mas não é segura).

1. Navegue até a pasta `conf` no diretório raiz do projeto.
2. Abra o arquivo `var.env` com o seu editor de texto favorito.
3. Modifique as variáveis de ambiente conforme necessário. As variáveis disponíveis são:
   - `POSTGRES_DB`: Nome do banco de dados PostgreSQL.
   - `POSTGRES_USER`: Usuário do banco de dados.
   - `POSTGRES_PASSWORD`: Senha do banco de dados.
   - `DATABASE_HOST`: Host do banco de dados (deve ser o nome do serviço do banco de dados definido no `docker-compose.yml`).
   - `DATABASE_NAME`: Nome do banco de dados a ser acessado pela aplicação Flask.
   - `DATABASE_USER`: Usuário do banco de dados para a conexão pela aplicação Flask.
   - `DATABASE_PASSWORD`: Senha do banco de dados para a conexão pela aplicação Flask.
4. Salve e feche o arquivo `var.env` após fazer as modificações.

## Executando o Projeto

Com o Docker instalado e as variáveis de ambiente configuradas, você está pronto para executar o projeto usando o Docker Compose.

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório raiz do projeto.
3. Execute o seguinte comando para construir e iniciar os serviços definidos no `docker-compose.yml`:

```bash
docker-compose up --build
```

4. Após os serviços serem inicializados, você poderá acessar a aplicação Flask navegando para `http://localhost:5000` no seu navegador.

## Encerrando o Projeto

Para parar e remover os contêineres, redes e volumes criados pelo Docker Compose, execute o seguinte comando no diretório raiz do projeto:

```bash
docker-compose down
```
## Repositório e Documentação Adicional

É possível também encontrar as imagens do [projeto flask](https://hub.docker.com/repository/docker/larissa606/projeto-flask-ada/general) e do [banco PostgreeSQL](https://hub.docker.com/repository/docker/larissa606/projeto-psql-ada/general) no DockerHub.
