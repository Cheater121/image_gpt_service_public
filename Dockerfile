FROM python:3.11

RUN mkdir /image_gpt_service
WORKDIR /image_gpt_service

RUN pip install gigachain-cli==0.0.21
RUN gigachain-cli install-rus-certs

RUN pip install --upgrade pip "poetry==1.8.3"
RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

COPY . .

RUN chmod a+x docker/*.sh
