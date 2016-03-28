import praw
import urllib.request
import os.path
import sys

STORE_LOCATION = 'images/'
STORE_FILE_NAME = 'images/stored'


# returns a dictionary of the form {'postId','url'}
def get_image_urls(reddit, theme, NUMBER_OF_POSTS):
	print(NUMBER_OF_POSTS)
	dict={}
	subreddit=reddit.get_subreddit(theme)
	print(subreddit)
	posts=subreddit.get_hot(limit=NUMBER_OF_POSTS)
	for post in posts:
		print ("adding : ", post.title, " to download list")
		dict[post.id]=post.url
	return dict

# takes filename and url and stores the image at url at $filename
def download_image(image_name,image_url):
	if '.jpg' in image_url or '.png' in image_url:	
		print ("downloading: "+image_url)
		urllib.request.urlretrieve(image_url,STORE_LOCATION+image_name)
	else:
		print ("ignoring: "+image_url)

def download_start():
	theme=input('Which subreddit would you like to download images from today?')
	n=input('Enter number of posts (<100) : ')
	try:
		NUMBER_OF_POSTS=int(n)
	except ValueError:
		print("Please enter a number")
		exit(0)
	print("downloading upto ",NUMBER_OF_POSTS," from ", theme)
	try:
		dict=get_image_urls(praw.Reddit(user_agent = "downloading HD wallpapers by /u/not_a_b0t"),theme,NUMBER_OF_POSTS)
		for key in dict.keys():
			download_image(key,dict.get(key))
	except praw.errors.InvalidSubreddit:
		print("Invalid Subreddit. Please try again.")	


download_start()


