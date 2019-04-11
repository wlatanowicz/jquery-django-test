ARG PYTHON_VERSION="2.7"

FROM python:${PYTHON_VERSION}

ARG BITBUCKET_CREDENTIALS="username:TOKENtokenTOKEN"
ARG DJANGO_VERSION="1.11"

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

RUN ./manage.py collectstatic

ENTRYPOINT ["/app/entrypoint.sh"]
