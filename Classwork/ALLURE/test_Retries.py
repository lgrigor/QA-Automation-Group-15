import allure
import random
import time

@allure.step
def flaky_broken_step():
    if random.randint(1, 10) != 1:
        raise Exception('Broken!')

def test_broken_with_randomized_time():
    #time.sleep(random.randint(1, 3))
    time.sleep(1)
    flaky_broken_step()