FROM python:3.10

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "little_test.py" ]