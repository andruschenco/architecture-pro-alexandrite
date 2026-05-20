from flask import Flask
import requests
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

resource = Resource(attributes={SERVICE_NAME: "service-a"})
provider = TracerProvider(resource=resource)
exporter = OTLPSpanExporter(endpoint="http://jaeger-collector:4318/v1/traces")
provider.add_span_processor(BatchSpanProcessor(exporter))
trace.set_tracer_provider(provider)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

@app.route('/')
def hello():
    resp = requests.get('http://service-b:8080/')
    return f"service-a called -> {resp.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
