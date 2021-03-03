FROM python:3.8-alpine
LABEL maintainer="Galen Guyer <galen@galenguyer.com>"

RUN apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo "America/New_York" > /etc/timezone

WORKDIR /app
ADD requirements.txt /app
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
 
 ADD . /app

ENTRYPOINT ["gunicorn", "quotes:APP", "--bind=0.0.0.0:5000"]
