FROM python:3.10

RUN apt update

RUN mkdir "bot"

WORKDIR /bot


COPY ./app ./app
COPY ./main.py ./main.py
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

RUN python -m pip install --upgrade pip

RUN pip install pipenv
RUN pipenv install --system --deploy

CMD ["python", "main.py"]
