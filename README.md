## Django-logstash
<hr>

Application monitors request data with ELK stack.

### Usage
Please follow steps:
1) `git clone https://github.com/KonradMarzec1991/django-logstash.git`
2) Run docker `docker-compose up (--build)`
3) Visit endpoint `/hello_world`
4) Query Elasticsearch - index `web` (you can use curl or kibana)