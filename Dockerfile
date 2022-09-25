FROM python:3.10 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

COPY . ./app

FROM base as test-base

COPY dev-requirements.txt .
RUN pip install --no-cache-dir --upgrade -r dev-requirements.txt

FROM base as build

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM test-base as test

CMD ["pytest"]

FROM build as final
