FROM python:3.8

WORKDIR /usr/src/

COPY ecdemo/requirements_dev.txt requirements.txt
RUN pip install -r requirements.txt

COPY ecdemo/tests tests/
COPY ecdemo/ecdemo ecdemo/

ENTRYPOINT ["pytest"]
CMD ["tests/test_ecdemo.py"]