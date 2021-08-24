FROM python:3-alpine

EXPOSE 8000/tcp

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY api.py ./
COPY methods.py ./

CMD ["python", "./api.py"]
