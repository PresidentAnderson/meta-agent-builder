FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "meta_agent.py", "--desc", "Auto-deploy agent"]
