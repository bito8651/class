# pip3 install progressbar
# pip3 install pygame

class YoutubeDownloader:
    def __init__(self):
        print('我誕生ㄌㄜˊ')

    def download_single_video(self, url):
        print('downloading...', url)

    def download_videos(self, video_urls):
        for url in video_urls:
            self.download_single_video(url)