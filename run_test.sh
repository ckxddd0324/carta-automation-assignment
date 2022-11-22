#!/bin/bash

docker-compose build
docker-compose run api-test bash -c "pytest -s --html=report.html --self-contained-html"

docker cp "$(docker ps -aq -f name=carta-automation-assignment_api -f status=exited | awk 'NR==1')":tests/report.html ./Report.html