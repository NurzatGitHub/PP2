from datetime import datetime

time = datetime.now().replace(second=0).replace(microsecond=0)

print(time)