FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -e .[rag,recsys]
EXPOSE 8000
CMD ["uvicorn","apps.rag_qa.api:app","--host","0.0.0.0","--port","8000"]
