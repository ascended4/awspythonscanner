FROM python:3.10-alpine
WORKDIR /app
COPY app.py requirements.txt /app/
RUN pip install -r requirements.txt
CMD python run_app.py