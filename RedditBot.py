import praw # reddit API interface - Python Reddit API Wrapper

# defining username, password and useragent for reddit praw
CLIENTID = "xKbqf1MksaNi2Q"
CLIENTSECRET = "i34E8l6qyOYolNoEtaXhNAaa9QI"
USERAGENT = "internship thread data gather bot v1.0 by internship_bot"
USERNAME = "internship_bot"
PASSWORD = "INTERNSHIP_BOT"

reddit = praw.Reddit(
    client_id=CLIENTID,
    client_secret=CLIENTSECRET,
    user_agent=USERAGENT,
    username=USERNAME,
    password=PASSWORD,
)

keyword = "internship"  # change appropriately for specific search word
subs = "csMajors"  # change appropriately for specific subreddits to scrape

# initialise list for holding data
title = []
post_id = []
post = []
score = []
reply = [[] for id in range(0, len(post_id))]

# main function
while True:

    for submission in reddit.subreddit(subs).top(limit=10000):

        if keyword in submission.title.lower() and submission.id not in post_id:

            # print("Thread title: " + submission.title)
            # print("Score: ", submission.score)
            title.append(submission.title)
            post_id.append(submission.id)
            post.append(submission.selftext)
            score.append(submission.score)

            top_comment = ""
            top_comment_score = 0
            for parent_comment in submission.comments:

                if parent_comment.score > top_comment_score:
                    top_comment_score = parent_comment.score
                    top_comment = parent_comment.body

                # comment = parent_comment.body
                # upvote = parent_comment.score
                # print("Upvote: %d, Comments: %s" % (upvote, comment))
            reply.append(top_comment)

    break


with open("Internship.txt", "w") as textfile:
        for i in range(0, len(post_id)):
            textfile.write("%s\n" % title[i] + "\n")
            textfile.write("%s\n" % score[i] + "\n")
            textfile.write("%s\n" % post[i].encode("UTF-8") + "\n ----------------------------------------------- \n\n")
            textfile.write("%s\n" % reply[i] + "\n =============================================== \n\n")