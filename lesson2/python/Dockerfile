# ПОДСКАЗКА1: можно использовать примеры практически 
# любого Dokcerfile для Python приложения

### ПОДСКАЗКА2: тут используется flask==3.0.3 в качестве зависимости

FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8000
CMD ["python", "app.py"]