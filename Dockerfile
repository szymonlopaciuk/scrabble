FROM python:3.6
WORKDIR /code
COPY . .
RUN pip install pipenv
RUN pipenv install --system
EXPOSE 5005
RUN useradd -m herokutestuser
USER herokutestuser
CMD python /code/wsgi.py