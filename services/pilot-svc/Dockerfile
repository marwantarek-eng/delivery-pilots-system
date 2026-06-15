FROM python:3.12-slim AS base

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS runtime
COPY app/ .

# Non-root user — required for production security posture
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

EXPOSE 5000
HEALTHCHECK --interval=15s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import httpx; httpx.get('http://127.0.0.1:5000/health').raise_for_status()"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
