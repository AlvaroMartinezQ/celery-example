# Steps to run the example:

1. Start your Redis broker and Mongo db:
```shell
docker-compose up --build -d
```

2. Start the *task* worker
```shell
celery -A tasks worker --loglevel=INFO
```

3. Start the *beat* worker (config inside the `beat_schedule` section of `celeryconfig.py`). This worker will submit the same task each minute.
```shell
celery -A tasks beat --loglevel=INFO
```

4. Run the `send_task.py` file which will:
  - Create a task for instant execution (`test_add.delay(...)`).
  - Create a scheduled task that will execute in 30 seconds from now (`hello.apply_async()`)
  
