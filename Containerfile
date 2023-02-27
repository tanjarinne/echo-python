FROM python:3.10.5-alpine

WORKDIR /app
ADD . ./

RUN set -e ;\
  pip install pipenv ;\
  pipenv sync

CMD ["python3", "echo.py"]
