FROM python:3-bullseye


LABEL maintainer="KrunchMuffin"
LABEL support = "https://github.com/krunchmuffin/plexMIOC"

WORKDIR /app
RUN wget https://mediaarea.net/repo/deb/repo-mediaarea_1.0-19_all.deb && dpkg -i repo-mediaarea_1.0-19_all.deb && apt-get update
RUN rm -rf ./repo-mediaarea_1.0-19_all.deb

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ["config.py", "constants.py", "log_handler.py", "main.py", "scan.py", "./"]
COPY config logs logos ./

VOLUME [ "/movies" ]
VOLUME [ "/tv" ]
VOLUME [ "/config" ]
VOLUME [ "/logs" ]

CMD ["python", "main"]
