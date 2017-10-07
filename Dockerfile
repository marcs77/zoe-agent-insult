FROM voiser/zoe-agent:v3

WORKDIR /code

ADD pip-requirements.txt /code
RUN pip3 install -r pip-requirements.txt

ADD src /code/src
ADD res /code/res

CMD python3 -u src/agent.py
