# Calculadora Python · Taller CI/CD

## Preparar ambiente 

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Comandos del taller

```bash
python -m pytest -q
ruff check .
python -m pytest -q --cov=calculadora --cov-report=term-missing
```