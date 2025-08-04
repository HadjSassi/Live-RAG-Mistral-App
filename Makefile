VENV_ACTIVATE = . .venv/bin/activate

run:
	@if [ "$(shell docker ps -q -f name=qdrant)" ]; then \
		docker stop qdrant; \
	fi
	docker run -d --rm -p 6333:6333 -p 6334:6334 --name qdrant qdrant/qdrant
	sleep 1
	$(VENV_ACTIVATE) && python app/__init__.py &
	$(VENV_ACTIVATE) && streamlit run app/Home.py &

run_cli:
	$(VENV_ACTIVATE) && python main.py &

cli:
	$(VENV_ACTIVATE) && python query.py

stop:
	pkill -f "python" || true
	pkill -f "streamlit" || true
	docker ps -q --filter ancestor=qdrant/qdrant | xargs -r docker stop

ps:
	docker ps

logs:
	docker logs qdrant