FROM python:3.12.2 as build
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
	      build-essential gcc 

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt ./
RUN pip install -r requirements.txt

FROM python:3.12.2-slim
COPY --from=build /usr/app/venv ./venv

COPY . .


ENV PATH="/usr/app/venv/bin:$PATH"

CMD [ "python", "app.py" ]