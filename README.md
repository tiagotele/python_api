# Python API

Exemplo de API Rest com Python

## Para executar localmente
Crie um ambiente virutal Python
```bash
python3 -m venv venv
```

Ative esse abiente no Linux:
```bash
source venv/bin/activate
```

ou Windows:
```bash
source venv/Scripts/activate
```

Instale dependências do framework FastApi
```bash
pip install -r requirements.txt
```

Inicie a aplicação
```bash
uvicorn app.api:app --reload
```

Acesse o browser no endereço: http://localhost:8000/


## Execução via Docker

```bash
export DOCKER_SCAN_SUGGEST=false
```

```bash
docker build -t tiagotele/python_api .
```

```bash
docker run -p 80:80 tiagotele/python_api
```

Acesse o browser no endereço: http://localhost

### Docker image
Docker image are available at [DockerHub](https://hub.docker.com/repository/docker/tiagotele/python_api).

## Docker compose
Para rodar a aplicação principal juntaente como Prometheus basta subir tudo com docker-compose:
```bash
docker-compose up
```

## Execução de testes unitários
```bash
make unit_test
```