# ELK stack and Jupyter in Docker Compose

1. Run `docker-compose up setup`
2. After Elasticsearch server is ready, you can run `docker compose up -d`

You shall be able to access:

- `localhost:9200`: Elasticsearch
- `localhost:5601`: Kibana
- `localhost:9600`: Logstash
- **`localhost:10000`: Jupyter**