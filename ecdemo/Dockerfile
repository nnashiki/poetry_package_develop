FROM python:3.8

WORKDIR /usr/src/
COPY requirements_dev.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY tests tests/
COPY ecdemo ecdemo/

ENTRYPOINT ["pytest"]
CMD ["tests/test_ecdemo.py"]