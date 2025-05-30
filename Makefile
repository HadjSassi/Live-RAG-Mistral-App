run:
	docker run -d --rm -p 6333:6333 -p 6334:6334 --name qdrant qdrant/qdrant
	sleep 1
	python main.py

cli:
    python query.py
stop:
	docker ps -q --filter ancestor=qdrant/qdrant | xargs -r docker stop