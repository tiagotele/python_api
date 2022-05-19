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
 uvicorn api:app --reload
```

Acesse o browser no endereço: http://localhost:8000/