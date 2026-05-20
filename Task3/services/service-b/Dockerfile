FROM python:3.11-slim
WORKDIR /app
RUN pip install flask opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http opentelemetry-instrumentation-flask
COPY service-b.py .
CMD ["python", "service-b.py"]

#FROM python:3.11-slim
#WORKDIR /app
#RUN pip install flask opentelemetry-api opentelemetry-sdk opentelemetry-exporter-jaeger opentelemetry-instrumentation-flask deprecated
#COPY service-b.py .
#CMD ["python", "service-b.py"]