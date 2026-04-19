FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --no-cache-dir pytest

COPY . .

CMD pytest -q; code=$?; [ $code -eq 5 ] && exit 0 || exit $code
