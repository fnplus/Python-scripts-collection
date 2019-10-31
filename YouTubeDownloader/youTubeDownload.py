from pytube import YouTube

def dowload_youtube_videos(urls, output_path, num=1):
    if isinstance(urls, list):
        for index, url in enumerate(urls):
            dowload_youtube_videos(url, output_path, num=index +1 )
    else:
        urls = urls.strip()
        yt = YouTube(urls)
        stream = yt.streams.first()
        stream.download(output_path=output_path)
        print(f"{num}: Downloaded file from {urls}")

if __name__ == "__main__":
    # https://www.youtube.com/watch?v=dQw4w9WgXcQ is the best one ;-)
    user_input = input("Give us a youtube URL (separate multiple with a comma (`,`)): ")

    dowload_youtube_videos(str(user_input).split(","), output_path="./")
