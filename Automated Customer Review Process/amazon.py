#a-section review
#review:review-text
#website:amazon.com
#rate:a-icon-alt
#time:review-date

import requests,bs4

class amazon:
	def __init__(self):
		self.address='http://www.amazon.com/VIZIO-E50-C1-50-Inch-1080p-Smart/product-reviews/B00SMBFP4U/ref=cm_cr_pr_btm_link_1?ie=UTF8&showViewpoints=1&sortBy=recent&reviewerType=all_reviews&formatType=all_formats&filterByStar=all_stars&pageNumber='
		self.page=0
		self.reviewBlock='.a-section .review'
		self.reviewText='.review-text'
		self.reviewRate='.a-icon-alt'
		self.reviewDate='.review-date'
		self.reviewWeb='amazon.com'
		self.ret=[]
		
	def run(self):
	    for i in range(130):
			self.page+=1
			print self.page
			try:
				res=requests.get(self.address+str(self.page))
			except:
				continue
			res.raise_for_status()
			bs=bs4.BeautifulSoup(res.text,'html.parser')
			elem=bs.select(self.reviewBlock)
			for j in range(10):
				try:
					text=elem[j].select(self.reviewText)[0].getText()
					rate=elem[j].select(self.reviewRate)[0].getText()[0:3]
					dt=elem[j].select(self.reviewDate)[0].getText()[3:]
					strRet=self.reviewWeb+'\t'+str(text).replace('\n',' ')+'\t'+str(rate)+'\t'+str(dt)
					self.ret.append(strRet)
				except:
					pass

	def result(self):
		return self.ret




if __name__=="__main__":
	amz=amazon()
	amz.run()
	ret=amz.result()
	with open('reviews.txt','w') as infile:
		for item in ret:
			infile.write(item+'\n')