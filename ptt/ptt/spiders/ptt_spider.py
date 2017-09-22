import scrapy
import html2text
f = open("/Users/skye/result.txt","w")
class PTTSpider(scrapy.Spider):
	name = "ptt"

	def start_requests(self):
		urls = ['https://www.ptt.cc/bbs/lesbian/index.html']
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):
		#data = response.css('title::text').extract()[0]
		articles = response.css("div.r-ent")
		for article in articles:
			# get title
			title = article.css("div.title")
			title = title.css("a::text").extract_first()
			# get date
			meta = article.css("div.meta")
			date = meta.css("div.date::text").extract_first()
			# get author
			author = meta.css("div.author::text").extract_first()

			#print(title,date,author)
			
			#f.write(str(date))
			#f.write(str(title))
			#f.write(str(author))
			# get url
			title = article.css("div.title")
			url = title.css("a::attr(href)").extract_first()
			url = 'https://www.ptt.cc' + url
			yield scrapy.Request(url, callback=self.parse_content)
			#print(content)
		#with open("/Users/skye/result.txt","w") as f:
				
	def parse_content(self,response):
		content = response.xpath('//div[@id="main-content"]')
		converter = html2text.HTML2Text()
		converter.ignore_links = True
		#print(converter.handle(content.extract()[0]))
		f.write(converter.handle(content.extract()[0]))