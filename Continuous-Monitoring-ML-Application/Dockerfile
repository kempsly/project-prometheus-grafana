FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip 
#copy to code directory
COPY . /code 

#set permissions

RUN chmod +x /code/src
# Set execute permissions for scripts in the /code/src directory
RUN chmod +x /code/src/*.py

# Set execute permissions for files in the /code/src/loan_pred_model directory
RUN chmod +x -R /code/src/loan_pred_model


RUN pip install --no-cache-dir --upgrade -r code/src/requirements.txt

EXPOSE 8005

WORKDIR /code/src

# ENV PYTHONPATH "${PYTHONPATH}:/code/src"
# Add the code directory to PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH};/code/src;/code/src/loan_pred_model"
# CMD pip install -e .

CMD ["python","loan_pred_model/training_pipeline.py"]
WORKDIR /code
CMD ["python","main.py"]