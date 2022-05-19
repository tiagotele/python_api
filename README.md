# Python API

Exemplo de API Rest com Python

## Para executar localmente
Crie um ambiente virutal Python
```bash
python -m venv venv
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
pip install "fastapi[all]"
pip install "uvicorn[standard]"
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
docker build -t myimage .
```

```bash
docker run --name mycontainer -p 80:80 myimage
```

Acesse o browser no endereço: http://localhost:8000/
