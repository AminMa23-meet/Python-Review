def create_youtube_video(title,description):
	youtubevid = {"title": title,"description":description,"likes":0,"dislikes":0,"comments":comments={}}
	return youtubevid
def like(youtubevid):
	if "likes" in youtubevid:
		youtubevid["likes"]+=1
	return youtubevid
def dislike(youtubevid):
	if "dislikes" in youtubevid:
		youtubevid["dislikes"]+=1
	return youtubevid
def add_comment(youtubevid,username,comments_text):
	youtubevid[username] = comments_text
	return youtubevid