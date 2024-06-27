FROM python:3.9

WORKDIR /app

COPY requirements.txt . 
COPY src/credentials.json /app/src/credentials.json
COPY src/token.json .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "src/main.py"]
