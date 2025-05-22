FROM python:3.12.10
LABEL local.authors="arm2arm@gmail.com"

# Your main changes
WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8501

#ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

#ENTRYPOINT ["streamlit", "hello", "--server.port=8501", "--server.address=0.0.0.0"]

