#!/bin/sh

exec gunicorn --bind $HOST:$PORT "$APP_MODULE" -k uvicorn.workers.UvicornWorker