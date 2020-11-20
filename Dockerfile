FROM python:3.8-slim

COPY requirements.txt /PersonalPyFi/
WORKDIR /PersonalPyFi
ENV PIP_DEFAULT_TIMEOUT=100

RUN pip install --upgrade pip \
    &&  pip install --trusted-host pypi.python.org --requirement requirements.txt

COPY . /PersonalPyFi

CMD ["python", "PyFi_cli.py"]
