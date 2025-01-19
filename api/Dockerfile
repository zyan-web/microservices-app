FROM python:3.9-slim
WORKDIR /app

# Make sure requirements.txt is copied first to leverage caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

COPY app.py /app/
COPY templates /app/templates

EXPOSE 5002
CMD ["python", "app.py"]
