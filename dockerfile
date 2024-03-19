FROM python:3.12

ADD * .
RUN pip install discord-py-interactions

CMD ["python", "main.py"]