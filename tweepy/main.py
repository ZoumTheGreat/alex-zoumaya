# main.py
import time
import const
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import sys


class TweetListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

def BFS(users, api):  # s is the source, i.e.g, udaytonID
    s = users[0]
    bfs_printer = open('bfs_printer.txt', 'w+')

    visitedIDs = set()  # insert all visited IDs into a set visitedIDs

    # Create a queue for BFS

    queue = []  # list is the most versatile data structure in python

    # Mark the source node as visited and enqueue it

    queue.append(s)

    # insert s into visitedIDs <-- leave it to you, write your own code
    print(s.screen_name)
    visitedIDs.add(s.screen_name)
    count = 0
    while queue:

        # Dequeue the first ID from queue
        s = queue.pop(0)
        visitedIDs.add(s.screen_name)
        # Get all friends of the dequeued ID s. If a friend has not been visited, then mark it
        bfs_printer.write("Friends of " + s.screen_name + ":\n")
        friendCount = 0
        for friend in tweepy.Cursor(api.friends, screen_name=s.screen_name).items(5):
            if friend.screen_name in visitedIDs:
                continue
            elif friend not in visitedIDs and friendCount < 2:
                friendCount += 1
                bfs_printer.write(friend.screen_name)
                bfs_printer.write("\n")
                visitedIDs.add(friend.screen_name)
                queue.append(friend)
                if friendCount == 2:
                    break
        count += 1
        if count % 15 == 0:
            time.sleep(15*60)
        if count is 32:
            return
            bfs_printer.close()
            # inserted i into visitedIDs <-- you need to write your code


def main():
    auth = tweepy.OAuthHandler(const.CONSUMER_KEY, const.CONSUMER_SECRET)
    auth.set_access_token(const.ACCESS_TOKEN, const.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    user_names = []
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                for word in line.split():
                    user_names.append(word)
    except IOError:
        print('No such file exists')
        exit(1)

    keywords = ["Ohio", "weather"]
    users = api.lookup_users(screen_names=user_names)
    crawl_profile_data(users)
    crawl_social_network_data(users, api)
    getTweets(api, keywords)
    findTweetsInRegion(api, "39.758949,-84.191605,50mi")
    BFS(users, api)

def getTweets(api, keywords):
    print("Recent tweets with both \"Ohio\" and \"Weather\" in them\n")
    count = 1
    for tweet in tweepy.Cursor(api.search, q=keywords).items(10):
        print("Tweet #%d: %s" % (count, tweet.text))
        count += 1

def findTweetsInRegion(api, region):
    Dayton = region
    results = tweepy.Cursor(api.search, geocode=region).items(50)
    print("\nTweets within 50 miles of Dayton, OH\n")
    count = 1
    for tweet in results:
        print("Tweet #%d: %s" % (count, tweet.text))
        count += 1


def crawl_profile_data(users):
    for user in users:
        print('---------------------------------------------')
        print("User Name: %s" % user.name)
        print("Screen Name: %s" % user.screen_name)
        print("User ID: %s" % user.id)
        print("Location: %s" % user.location)
        print("User Description: %s" % user.description)
        print("The number of followers: %s" % user.followers_count)
        print("The number of friends: %s" % user.friends_count)
        print("The number of tweets: %s" % user.statuses_count)
        print("User URL: %s" % user.url)
    return


# given a list of users, for each user, displays friends and first 20 followers
def crawl_social_network_data(users, api):
    # crawl 20 friends and 20 followers of each user
    for user in users:
        counter = 0
        print('---------------------------------------------')
        print("User: %s\n") % user.name
        # loop through 20 friends
        print("Friends of %s" % user.name)
        listOfFriends = []
        print(tweepy.Cursor(api.friends, screen_name=user.name).items(20))
        for friend in tweepy.Cursor(api.friends, screen_name=user.name).items(20): #listOfFriends:
            counter += 1
            print("Friend #%s of %s is %s") % (str(counter), user.name, friend.screen_name)
        counter = 0
        # loop through 20 followers
        print("\nFollowers of " + user.name)
        for follower in tweepy.Cursor(api.followers, screen_name=user.name).items(20):
            counter += 1
            print("Follower #%s of %s is %s") % (str(counter), user.name, follower.screen_name)


if __name__ == "__main__":
    main()
