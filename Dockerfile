FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy the application code
COPY . .

CMD ["python","-u","main.py"]
