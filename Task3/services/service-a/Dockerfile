FROM python:3.11-slim
WORKDIR /app
RUN pip install flask requests opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-http opentelemetry-instrumentation-flask opentelemetry-instrumentation-requests
COPY service-a.py .
CMD ["python", "service-a.py"]

#FROM python:3.11-slim
#WORKDIR /app
#RUN pip install flask requests opentelemetry-api opentelemetry-sdk opentelemetry-exporter-jaeger opentelemetry-instrumentation-flask opentelemetry-instrumentation-requests deprecated
#COPY service-a.py .
#CMD ["python", "service-a.py"]