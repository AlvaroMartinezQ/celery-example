from celery.schedules import crontab

# Store data in the mongo db
result_backend = "mongodb"
mongodb_backend_settings = {
    "host": "127.0.0.1",
    "port": 27017,
    "database": "jobs", 
    "taskmeta_collection": "stock_taskmeta_collection",
}

# Used to schedule tasks periodically and passing optional arguments.
# Celery does not seem to support scheduled task but only periodic.
beat_schedule = {
    'every-minute': {
        'task': 'tasks.hello',
        'schedule': crontab(minute='*/1'),
        # 'args': (1,2), # Passing args to the callable function
    },
}