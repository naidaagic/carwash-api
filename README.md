# Carwash API

## Installation

```bash
python3.10 -m venv carwash-venv/
source carwash-venv/bin/activate
(carwash-venv) pip install -r requirements.txt
(carwash-venv) python manage.py makemigrations
(carwash-venv) python manage.py migrate
```

## Tests

```bash
python manage.py test
```

## Running

```bash
python manage.py runserver
```

### API Endpoints

- `/user`
- `/user/{ID}`
- `/bill`
- `/bill/{ID}`
- `/washing_program`
- `/washing_program/{ID}`
- `/washing_step`
- `/washing_step/{ID}`

# Other tasks

- [Algorithmic task #1](algorithmic_task_1.py)
- [Algorithmic task #2](algorithmic_task_2.py)
- [Algorithmic and data structures task #3](algorithmic_data_struct_task.py)