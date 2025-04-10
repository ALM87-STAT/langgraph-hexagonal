# LangGraph Hexagonal Template

## Instrctions for the template

### How to use the template

#### Create environment
```bash
conda create -y -n llm-agents python=3.11
```

#### Activate the environment
```bash
conda activate llm-agents
```

#### Install the dependencies
```bash
pip install -r requirements/dev.txt
```

#### Export the SSL certificate (opional)
```bash
export SSL_CERT_FILE=$(python -c "import certifi; print(certifi.where())")
```

#### Run the application
```bash
python app/main.py
```

