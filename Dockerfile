FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY src/ src/

COPY . /app 
RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "src/main.py"]