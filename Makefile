PROJECT_LABEL := "adverity-transformer-challenge"

#-----------------------------------------------------------------------------
include makeutils/docker.mk
#-----------------------------------------------------------------------------

help:
	@echo "Define all available options:"
	@echo "------------------------------------------------------------------------------------"
	@echo "help                     List of all the options'make <option>'"
	@echo ""
	@echo "docker-build-dev         Build applocation in development mode"
	@echo "docker-up-dev            Run the application in development mode"
	@echo "docker-reset-dev         Stop, clean, rebuild and run the entire application"
	@echo "docker-stop              Stop all the containers related to the application"
	@echo "docker-clean             Stop and Remove all the containers, networks, images and volumes related to the application"
	@echo "docker-rebuild-ui        Rebuild only User Interface"
	@echo "docker-backend           Login into backend docker container"
	@echo "docker-backend-test      Perform backend testing"
	@echo ""
#-----------------------------------------------------------------------------
