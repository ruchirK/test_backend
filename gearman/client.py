__author__ = 'ruchir'


#Simulate the feed class from the real backend

import gearman
import datetime
import timeit
from worker import process_user
from worker import process_tweet
num_users = 20
#set last accessed
user_last_accessed = [datetime.datetime.utcnow() for x in range(num_users)]
num_iterations = 10
import time


def main_loop(iterations):

    for y in range(iterations):
        print 'Starting iteration ', y, '--------------------------------'
        iterate_users()


def iterate_users():
    for index, d in enumerate(user_last_accessed):
        if datetime.datetime.utcnow() - d > datetime.timedelta(seconds=1) or d == datetime.datetime.utcnow():
            print 'Starting user ', index, 'with time ', d, ' '
            print'==============================================='
            gm_client.submit_job("process_user", "")

gm_client = gearman.GearmanClient(['localhost:4730'])



print 'Starting main_loop'
time.sleep(2)
print timeit.timeit(iterate_users, number=1)

#print timeit.timeit(process_user, number = 2)
#process_tweet.delay(200)
#print timeit.timeit("twitter.tasks.process_tweet(200)", "import twitter", number = 1)
