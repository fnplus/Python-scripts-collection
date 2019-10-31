from pytube import YouTube

urls = ['https://www.youtube.com/watch?v=j440-D5JhjI']

def dowload_videos(urls, output_path):
	
	num = 0s

	for url in urls:
	    yt = YouTube(url)
	    stream = yt.streams.first()
	    stream.download(output_path = output_path)
	    print('{}: Downloaded file from url- {}'.format(num, url))
	    num = num+1
	    
dowload_videos(url, output_path='E:/User/Music/queen/')