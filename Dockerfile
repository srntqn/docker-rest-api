FROM  python:3.7
RUN pip install flask connexion connexion[swagger-ui] swagger_ui_bundle docker
WORKDIR /app
COPY *.py swagger.yml ./
COPY templates ./templates
#COPY static ./static
ENTRYPOINT ["python", "server.py"]