FROM python:3.11.4-bullseye
ENV FLASK_APP app.py
WORKDIR /app
COPY ./requirements/common.txt ./requirements/
RUN pip install --no-cache-dir -r ./requirements/common.txt
COPY ./src src
COPY ./static static
COPY ./templates templates
COPY ./app.py app.py
# Initial database
COPY ./db.json db.json
CMD ["flask", "run", "--host", "0.0.0.0"]
EXPOSE 5000