__author__ = 'ruchir'

import gearman

gm_worker = gearman.GearmanWorker(['localhost:4730'])

#Simulates the tasks file in the backend
def process_user(gearman_worker, gearman_job):
    num_tweets = 200
    for x in range(num_tweets):
        result = process_tweet(x)
        #if result % 199 == 0:
        #    print x, ' factorial mod 200 is ' #, result % 200
    print 'End user'


def process_tweet(num):
    #computes num!
    print 'Tweet (computing factorial) number ',  num
    y = 1
    for x in range(1,num * 200):
        y = y * x
        if x > num:
            y = y/x
    return y

gm_worker.register_task('process_user', process_user)

gm_worker.work()
