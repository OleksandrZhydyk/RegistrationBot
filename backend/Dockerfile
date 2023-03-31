FROM python:3.10

RUN apt update

RUN mkdir "backend"

WORKDIR backend

# COPY ./start.sh ./start.sh
COPY ./src ./src
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

RUN python -m pip install --upgrade pip

RUN pip install pipenv
RUN pipenv install --system --deploy

RUN chmod a+x ./start.sh

CMD ["bash"]
