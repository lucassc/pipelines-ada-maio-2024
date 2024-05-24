#!/usr/bin/env bash
set -e

execute_unit_tests()

docker build --file ./docker_files/preparar_ambiente.Dockerfile --tag registry-production/app-projeto-ada:preparar-ambiente .
docker build --file ./docker_files/producer.Dockerfile --tag registry-production/app-projeto-ada:producer .
docker build --file ./docker_files/consumer.Dockerfile --tag registry-production/app-projeto-ada:consumer .

scan_conatiners_for_vulnerabilities()

login_to_container_registry()

docker push registry-production/app-projeto-ada:preparar-ambiente
docker push registry-production/app-projeto-ada:producer
docker push registry-production/app-projeto-ada:consumer


