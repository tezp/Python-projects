from bs4 import BeautifulSoup as bs
import requests
import argparse
import sys

parser = argparse.ArgumentParser(description='Shows details of video and suggested videos from Youtube.')
parser.add_argument('-u', '--url', help='url of youtube video', required=True)
result = parser.parse_args()
print(len(sys.argv))

if len(sys.argv) != 3:
    sys.exit(1)

r = requests.get(sys.argv[2])
soup = bs(r.text, 'lxml')
print("Video Details : ")
title = soup.find('span', {'id': 'eow-title', 'dir': 'ltr'})
print(title.string.strip())
views = soup.find('div', {'id': 'watch7-views-info'}).next.string
print("Total Views : ", views)
likes = soup.find('button', {'title': "I like this"}).next.string
print("Total Likes : ", likes)
unlikes = soup.find('button', {'title': "I dislike this"}).next.string
print("Total Unlikes : ", unlikes)
description = soup.find('p', {'id': 'eow-description'}).get_text()
print("Description : ", description)

upnext = soup.find('div', {'class': 'watch-sidebar-body'})
span = upnext.find_all('span')
print("##########################################################################################")
print("Up-next Video : ")
print("Title : ", span[0].string.strip())
print("Channel Name : ", span[2].string.strip())
print("Duration : ", span[6].string.strip())
print("Views : ", span[4].string.strip())
print("##########################################################################################")

nextVideoList = soup.find_all('div', {'class': 'content-wrapper'})
print(len(nextVideoList))
print("\nVideos suggested : ")

for video in nextVideoList:
    current_videos = video.find_all('span')
    # print(current_videos[1].string)
    print("Title : ", current_videos[0].string.strip())
    print("Channel Name : ", current_videos[2].string.strip())
    print("Duration : ", ":".join((current_videos[1].string.strip()).split(':')[1:]).strip('.'))
    print("Views : ", current_videos[4].string.strip())
    print("========================================+++++===========================================")
