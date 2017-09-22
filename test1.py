
urls = [
	"http://www.google.com/a.txt",
	"http://www.google.com.tw/a.txt",
	"http://www.google.download/c.jpg",
	"http://www.google.co.jp/a.txt",
	"http://www.google.com/b.txt",
	"http://facebook.com/movie/b.txt",
	"http://yahoo.com/123/000/c.jpg",
	"http://gliacloud.com/haha.png",
]

def count(urls):
	filenames = {}
	for url in urls:
		filename = url.split('/')[-1]
		if filename in filenames:
			filenames[filename] += 1
		else:
			filenames[filename] = 1

	sorted_files = sorted(filenames.items(), key=lambda x: x[1])

	for i in range(1,4):
		print(sorted_files[-i][0],sorted_files[-i][1])

count(urls)