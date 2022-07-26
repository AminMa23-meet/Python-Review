def create_youtube_video(title,description):
	youtubevid = {"title": title,"description":description,"likes":0,"dislikes":0,"comments":{}}
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
	youtubevid["comments"][username] = comments_text
	return youtubevid
hi = create_youtube_video(hi,bye)
for i in range(495):
	like(hi)
dislike(hi)
add_comment(hi,"amin","goodbye")
