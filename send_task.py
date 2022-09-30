from datetime import datetime, timedelta

from tasks import test_add, hello

# Simple task, instantly executed
res = test_add.delay(4, 4)
print(res.get())


# More complex task, will be executed on the ETA passed
# as `datetime`
some_time = datetime.utcnow() + timedelta(seconds=30)
hello.apply_async(eta=some_time) # Run the task 30 seconds after
