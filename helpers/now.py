from datetime import datetime
from bson.timestamp import Timestamp


def now():
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return current_timestamp
