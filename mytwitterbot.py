# mytwitterbot.py
# IAE 101, Fall 2021
# Project 04 - Building a Twitterbot
# Name: Nikhil
# netid:  nsundaresan   
# Student ID: 114587309

import sys
import time, random
import simple_twit

# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# Consumer Key also known as API key
CONSUMER_KEY = "b37NODAQBwDTT7QqLcM6gZMsR"
# Consumer Secret also known as API Key Secret
CONSUMER_SECRET = "luCsdclCIafY3qu1LaWM2OoUpuwZ4tKPIU4AI0Q0UIIDWkriQg"

# Project 04 Exercises
    
# Exercise 1 - Get and print 10 tweets from your home timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise1(api):
    t_list = simple_twit.get_home_timeline(api, 10)

    for i in t_list:
        print("Tweet ID: " + str(i.id))
        print("Username: " + str(i.user.name))
        print("Handle: " + str(i.user.screen_name))
        print("Time of creation: " + str(i.user.created_at))
        print("Tweet text: " + str(i.full_text))
        print(" ")
        time.sleep(2)


# Exercise 2 - Get and print 10 tweets from another user's timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
def exercise2(api):
    User_name = "IAE101114587309"                                    #enter user's name
    t_list = simple_twit.get_user_timeline(api, User_name, 1)

    for i in t_list:
        print("Tweet ID: " + str(i.id))
        print("Username: " + str(i.user.name))
        print("Handle: " + str(i.user.screen_name))
        print("Time of creation: " + str(i.user.created_at))
        print("Tweet text: " + str(i.full_text))
        print(" ")
        time.sleep(2)


# Exercise 3 - Post 1 tweet to your timeline
def exercise3(api):
    text = "abcd"                       #type tweet text
    simple_twit.send_tweet(api, text)
    time.sleep(2)

# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(api):
    text = "Lebron James"                                       #type tweet text
    filename = "Lebron.jpg"                                     #type file url
    simple_twit.send_media_tweet(api, text, filename)
    time.sleep(2)

# End of Project 04 Exercises


# YOUR BOT CODE GOES IN HERE
def twitterbot(api):
##    text = "Reply to this pinned tweet by writing the full name of a current NBA star you would like to know the stats of. Example- Luka Doncic" 
##    simple_twit.send_tweet(api, text)
##    time.sleep(2)
    x = simple_twit.get_mentions(api, 1)
    for i in x:
        a = i.full_text
        z = a.replace("@IAE101114587309 ","")
        txtfile = open(z + ".txt", "r")
        text = "@" + str(i.user.screen_name) + " " + str(z) + " " + txtfile.read()
        print(text)
        filename = z + ".jpg"
        simple_twit.send_media_tweet(api, text, filename)
        txtfile.close()
        time.sleep(900)
##    in progress


if __name__ == "__main__":
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
    #exercise1(api)
    #exercise2(api)
    #exercise3(api)
    #exercise4(api)

    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(api)
