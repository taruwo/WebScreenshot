FROM mcr.microsoft.com/playwright/python:v1.34.0-jammy

RUN pip install playwright && playwright install

WORKDIR /screenshot

COPY getss.py /srv

ENTRYPOINT ["python","/srv/getss.py"]
