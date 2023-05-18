from python:3.11
ADD . /app
WORKDIR /app
#COPY requirements.txt
RUN pip install -r requirements.txt
#COPY . . 
EXPOSE 8000
RUN chmod +x /app/manage.py
RUN chmod +x /app/start.sh
#CMD ["./manage.py", "runserver"]
CMD ["./start.sh"]