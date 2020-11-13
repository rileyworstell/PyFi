FROM python:3.8-slim

COPY requirements.txt /PersonalPyFi/
WORKDIR /PersonalPyFi

RUN pip install --upgrade pip \
    &&  pip install --trusted-host pypi.python.org --requirement requirements.txt

COPY . /PersonalPyFi

CMD ["python", "PyFi_cli.py"]
