FROM python:3.6
WORKDIR /code
RUN pip install pipenv
RUN pipenv install
EXPOSE 5005
CMD ["pipenv", "run", "python3", "wsgi.py"]