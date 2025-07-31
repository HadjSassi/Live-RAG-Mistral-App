VENV_ACTIVATE = . .venv/bin/activate

run:
	@if [ "$(shell docker ps -q -f name=qdrant)" ]; then \
		docker stop qdrant; \
	fi
	docker run -d --rm -p 6333:6333 -p 6334:6334 --name qdrant qdrant/qdrant
	sleep 1
	$(VENV_ACTIVATE) && python main.py

cli:
	$(VENV_ACTIVATE) && python query.py

stop:
	docker ps -q --filter ancestor=qdrant/qdrant | xargs -r docker stop