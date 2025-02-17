FROM python:3.10.13-alpine3.18

# Install dependencies
RUN apk update
RUN apk add --no-cache wget tar firefox
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Create application directory
RUN mkdir /srv/app
WORKDIR /srv/app

# Copy application files
COPY ./crypto-wss/main.py ./main.py

# Install Python packages
RUN pip install --upgrade pip
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock ./

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --only wss,db --no-interaction --no-ansi --no-root

CMD ["tail", "/dev/null"]