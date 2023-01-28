FROM python:3.9

WORKDIR /app
ADD . ./

RUN set -e ;\
  pip install pipenv ;\
  pipenv sync

CMD python3 echo.py