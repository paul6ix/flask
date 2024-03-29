FROM python:3.9.12

WORKDIR /user/desktop/flask

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY hello .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]