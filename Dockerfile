FROM python:3.12-slim-bookworm

RUN pip install poetry gunicorn

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-root

RUN mkdir data models

COPY ["./prediction.py", "./"]

COPY ["./data/test_data.json", "./data/features_names.yaml", "./data/"]

COPY ["./models/model.pkl", "./models/"]

EXPOSE 1717

ENTRYPOINT ["poetry", "run", "gunicorn", "--bind=0.0.0.0:1717", "prediction:app"]
