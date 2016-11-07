from selenium import webdriver
import time

class bestbuy:
	def __init__(self,path):
		self.browser=webdriver.PhantomJS(executable_path=path) #'D:\phantomjs-1.9.7-windows\phantomjs.exe'
		self.browser.get("http://www.bestbuy.com/site/insignia-32-class-31-1-2-diag--led-720p-hdtv-black/6080010.p?id=1219191179593&skuId=6080010")
		time.sleep(3)
		self.ret=[]
		self.page=1
		self.websiteName="bestbuy.com"
		self.textByClass="BVRRReviewText"
		self.rateByClass="BVRRRatingNormalOutOf"  #4-11
		self.timeByClass="BVRRReviewDateContainer"

	def clickIt(self,linkT):
		try:
			ele=self.browser.find_element_by_link_text(linkT)
			ele.click()
			rText=[]
			while(len(rText)==0):
				time.sleep(1)
				rText=self.browser.find_elements_by_class_name(self.textByClass)
		except:
			pass
		
		
	def onStart(self):
		self.clickIt('(2,761 customer reviews)')
		self.processData()
		for i in range(200):
			print self.page
			self.page+=1
			self.clickIt(str(self.page))
			self.processData()
		return self.ret	
		
	def processData(self):
		try:
			rText=self.browser.find_elements_by_class_name(self.textByClass)
			rRate=self.browser.find_elements_by_class_name(self.rateByClass)
			rTime=self.browser.find_elements_by_class_name(self.timeByClass)
			if(len(rText)<8): pass
			else:
				for i in range(8):
					temp = self.websiteName+'\t'+str(rText[i].text.replace('\n',' '))+'\t'+str(rRate[i+4].text)+'\t'+str(rTime[i].text)
					self.ret.append(temp)
		except:
			pass
			
if __name__ == "__main__":
	by=bestbuy("phantomjs-1.9.7-windows\phantomjs.exe")
	ret=by.onStart()
	with open('reviews.txt','w') as fin:
		for item in ret:
			fin.write(item+'\n')
