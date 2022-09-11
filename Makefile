install:
	poetry install

run-gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

build:
	poetry build

publish: # отладка публикации
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

tests:
	poetry run pytest
