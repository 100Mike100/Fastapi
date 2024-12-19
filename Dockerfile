FROM python:3.13.1-slim

WORKDIR /app

COPY . .

RUN /bin/sh -c "python -m venv Scanner-env"

RUN /bin/sh -c "Scanner-env/Scripts/activate"

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]