pip install poetry
pip install sqlalchemy
poetry init
poetry lock
poetry update package
poetry add psycopg2-binary
pip show psycopg2-binary
poetry show
poetry add psycopg2
pip install faker
pip install alembic
alembic init alembic
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
python my_select.py
