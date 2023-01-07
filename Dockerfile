FROM python:3.11-slim

RUN mkdir /pizza_time
COPY . /pizza_time/
WORKDIR /pizza_time

RUN pip install -r requirements.txt

RUN useradd -ms /bin/bash pizza_time
USER pizza_time

EXPOSE 8080

CMD ["/bin/bash", "bin/run"]