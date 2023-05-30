

docker-build-dev:
	@docker-compose build

docker-up-dev:
	@docker-compose up

docker-stop:
	@for CONTAINER_ID in $$(docker container ls -q --filter name="${PROJECT_LABEL}*"); do \
		docker container stop $$CONTAINER_ID ; \
	done

docker-clean: docker-stop
	@for CONTAINER_ID in $$(docker ps -a -q --filter name="${PROJECT_LABEL}*"); do \
		docker container rm $$CONTAINER_ID ; \
	done
	@docker volume prune

docker-reset-dev: docker-clean
	@docker-compose up --build

docker-rebuild-ui:
	@docker-compose up -d --no-deps --build frontend

docker-backend:
	@docker exec -it adverity-transformer-challenge-backend bash

docker-backend-test:
	@docker exec -it adverity-transformer-challenge-backend pytest
