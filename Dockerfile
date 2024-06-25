FROM python:slim-bookworm

WORKDIR /app

COPY . /app 
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001
CMD ["streamlit", "run", "--server.port", "8001", "src/main.py"]