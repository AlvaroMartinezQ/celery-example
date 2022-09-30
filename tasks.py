from celery import Celery

# The celery scheduler
app = Celery('tasks', backend="mongodb://mongo:mongo@localhost:27017", broker="redis://:test@localhost:6379")

# Locad config from the celeryconfig.py file
app.config_from_object('celeryconfig')

# ----------------
# Celery tasks

@app.task()
def test_add(x: int, y: int) -> int:
    result = x + y
    print(f"Result task -> {x}+{y}={result}")
    return result

@app.task()
def hello():
    return 'hello world'

# End of celery tasks
# ----------------
