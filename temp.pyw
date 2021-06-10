import requests
import urllib3
def testrequests(url):

	page = requests.get(url)

	soup = bs(page.content,features="html.parser")

	#print(soup)
	#print(soup.prettify())
	return soup 

#testrequests()

from pynput.mouse import Button, Controller
import keyboard
import schedule
import time
import click
import webbrowser
import subprocess
import os
import urllib

url = ['','']


# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


mouse = Controller()

# Linux
# chrome_path = '/usr/bin/google-chrome %s'
class Myautodownloader():
	def fetchinglocation(self,url):
		fetchingurl=str(testrequests(url))
		ans=""
		num=0
		imgtype=[0,0,0]
		findurl="https://t.nhentai"
		findpage = "pages%3A%3C"
		i=0
		mytrue = 1
		while(mytrue):
			for k in range(len(findurl)):
				if fetchingurl[i+k]!=findurl[k]:
					i+=1
					mytrue = 1
					break
				else:
					mytrue =0
		ans=fetchingurl[i:i+40]
		ans=ans[0:8] + 'i' +ans[9:]
		while(str(ans[-1]).isalnum()):  ans=ans[:-1]
		i+=40
		mytrue = 1
		while(mytrue):
			for k in range(len(findpage)):
				if fetchingurl[i+k]!=findpage[k]:
					i+=1
					mytrue = 1
					break
				else:
					mytrue =0
		i+=len(findpage)+23
		try:
			num = int(fetchingurl[i:i+3])		
		except ValueError:
			try:
				num = int(fetchingurl[i+1:i+4])
			except ValueError:
				try:
					num = int(fetchingurl[i:i+2])
				except:
					num = int(fetchingurl[i+1:i+3])

		return ans , num 


	def updateurl(self,url,count):
		webbrowser.get(chrome_path).open(url+str(count))
	
	def initfolder(self,url):
		ans=''
		origdir='C:\\Users\\ADMIN\\OneDrive\\Pictures\\Mytestimage'
		for i in range(len(url)):
			if url[i]=='g':
				ans=url[i+2:]
				break
		ans = os.path.join(origdir,ans)+'\\'
		try:
			os.mkdir(ans)
		except FileExistsError:
			pass
		return ans

first = time.time()
imgtype=[".png",".jpg",".jpeg"]
a = Myautodownloader()
for m in range(len(url)):
	mydir=a.initfolder(url[m])
	create_img , numberofpage = a.fetchinglocation(url[m])
	print(create_img,numberofpage)
	for i in range(1,numberofpage+1):
		try: 
			suffix = str(i)+ imgtype[0]
			urllib.request.urlretrieve(create_img + suffix, mydir + suffix)
		except:
			try:
				suffix = str(i)+ imgtype[1]
				urllib.request.urlretrieve(create_img + suffix, mydir + suffix)
			except:
				suffix = str(i)+ imgtype[2]
				urllib.request.urlretrieve(create_img + suffix, mydir + suffix)
		print(i,end=' ')
	print("\nDone ",m)

second = time.time()
print("Time = ",second - first)
'''

mouse.position = (494, 612)
mouse.press(Button.left)
mouse.release(Button.left)

time.sleep(1)
mouse.position = (1075, 477)
mouse.press(Button.left)
mouse.release(Button.left)

Current position: ()

'''
def job():

	print ("Current position: " + str(mouse.position))

	
	mouse.position = (1179, 314)
	mouse.press(Button.left)
	mouse.release(Button.left)
	#time.sleep(3)
	#subprocess.call(["C:/Users/ADMIN/Desktop/Python folder/turn-off-screen-master/turn-off-screen-master/turnoff.exe"])

    #print("I'm working...")
def exitjob():
	print ("Current position: " + str(mouse.position))
	mouse.position = (1445, 762)
	mouse.press(Button.left)
	mouse.release(Button.left)
	mouse.position = (1285, 754)
	mouse.press(Button.left)
	mouse.release(Button.left)

def funnyjob():
	print ("Current position: " + str(mouse.position))


#schedule.every(2).seconds.do(funnyjob)
#schedule.every(17).seconds.do(exitjob)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at('09:00').do(job)
#schedule.every().day.at('12:00').do(exitjob)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)
#subprocess.call(["C:/Users/ADMIN/Desktop/Python folder/turn-off-screen-master/turn-off-screen-master/turnoff.exe"])
def testjob():
	while True:
	    schedule.run_pending()
	    time.sleep(1)

#testjob()

