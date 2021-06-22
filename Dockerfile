FROM python:3.9


WORKDIR /app
ADD . .

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

RUN mkdir site
RUN mkdir test_folder
RUN mkdir pdf



# CMD ["python","cli.py","test", "test_folder", "$SITE"]

ENTRYPOINT python cli.py test test_folder $SITE






