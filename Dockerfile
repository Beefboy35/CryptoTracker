FROM python:3.12

RUN mkdir /CryptoTracker

WORKDIR /CryptoTracker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000"]


