import random
from string import ascii_lowercase, digits, punctuation


class TestData():
    
    ADMIN_USERNAME = 'admin1@gmail.com' 
    ADMIN_PASSWORD = 'J@}4HnJ6=;]>;!8u'

    RANDOM_USERNAME = ''.join(random.choices(ascii_lowercase, k=10) + random.choices(digits, k=2)) + '@gmail.com'
    RANDOM_PASSWORD = ''.join(random.choices(ascii_lowercase + digits + punctuation, k=10))