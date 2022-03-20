FROM python:3.8

ADD main.py .

RUN pip install gurobipy numpy

CMD [ "python", "./main.py" ]