from pytube import YouTube
from colorama import init, Fore
class YouVideoDownloadLogic:
    def on_complete(self,stream, file_path):
        print(stream)
        print(file_path)
        print('Download Complete')

    def on_progress(self,stream, chunk, bytes_remaining):
        print(f'{100 - round(bytes_remaining / stream.filesize * 100)}%')

    def video_information(self,video_object):
        ""
        init()
        print(Fore.RED+ f'Title : \033[39m {video_object.title}')
        print(Fore.RED+ f'Length : \033[39m {round(video_object.length /60,2)} minutes')
        print(Fore.RED+ f'Views : \033[39m {video_object.views /1000000} million')
        print(Fore.RED+ f'Author : \033[39m {video_object.author}')

    def download_choice(self):
        #Download
        print(
            Fore.RED+'download:' +
            Fore.GREEN+'(a)Video \033[39m|'+
            Fore.YELLOW+'(b)Audio\033[39m')
        download_choice= input('choice: ')
        return download_choice

    def download_youtube_video(self,video_object):
        video_object.streams.get_highest_resolution().download(r'C:\Users\mvhit\Downloads\Youtube\Video')
    def download_youtube_audio(self,video_object):
        video_object.streams.get_audio_only().download(r'C:\Users\mvhit\Downloads\Youtube\Audio')

    def youtube_video(self):
        link = str(input("Enter the YouTube link :"))
        video_object = YouTube(link, on_complete_callback= self.on_complete,
                               on_progress_callback=self.on_progress)
        self.video_information(video_object)
        download_choice = self.download_choice()
        if download_choice == 'a':
            self.download_youtube_video(video_object)
        elif download_choice == 'b':
            self.download_youtube_audio(video_object)