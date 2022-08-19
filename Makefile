clean:
	rm -rf dist build poetry_build_issue/generated/file.py

build:
	poetry build

cleanbuild: clean build
