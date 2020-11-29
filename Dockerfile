FROM python:3.8

WORKDIR /usr/src/

COPY workspace/requirements_dev.txt requirements.txt
RUN pip install -r requirements.txt

COPY workspace/tests tests/
COPY workspace/ecdemo ecdemo/

ENTRYPOINT ["pytest"]
CMD ["tests/test_ecdemo.py"]
