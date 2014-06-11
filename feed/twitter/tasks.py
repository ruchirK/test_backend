__author__ = 'ruchir'

from celery import celery

#Simulates the tasks file in the backend
@celery.task
def process_user():
    num_tweets = 200
    for x in range(num_tweets):
        result = process_tweet(x)
        #if result % 199 == 0:
        #    print x, ' factorial mod 200 is ' #, result % 200
    print 'End user'
@celery.task
def process_tweet(num):
    #computes num!
    print 'Tweet (computing factorial) number ',  num
    y = 1
    for x in range(1,num * 200):
        y = y * x
        if x > num:
            y = y/x
    return y
