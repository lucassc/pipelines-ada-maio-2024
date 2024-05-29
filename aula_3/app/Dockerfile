FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]