import clipboard
from bs4 import BeautifulSoup as bs
#clipboard.copy("abc")  # now the clipboard content will be string "abc"
text = clipboard.paste()  # text will have the content of clipboard

#print(text)





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


'''

a= ffff ff00 0000 ffff ff00 0000 ffff
ff00 0000 ffff ff00 0000 ffff ff00 0000
ffff ff00 0000 ffff ff00 0000 ffff ff00
0000 ffff ff00 0000 ffff ff00 0000 ffff
ff00 0000 ffff ff00 0000 ffff ff00 0000
ffff ff00 0000 ffff ff00 0000 ffff ff00
0000 ffff ff00 0000 ffff ff00 0000 ffff
ff00 0000 ffff ff00 0000 ffff ff00 0000
ffff ff00 0000 ffff ff00 0000 ffff ff00
0000 ffff ffff ffff 0000 00ff ffff 0000
00ff ffff 0000 00ff ffff 0000 00ff ffff
0000 00ff ffff ffff ff00 0000 ffff ff00
0000 ffff ff00 0000 ffff ff00 0000 ffff
ff00 0000 ffff ff00 0000 ffff ff00 0000
ffff ff00 0000 ffff ff00 0000 0000 00ff
ffff 0000 00ff ffff 0000 00ff ffff 0000
00ff ffff 0000 00ff ffff 0000 00ff ffff
0000 00ff ffff 0000 00ff ffff 0000 00ff
ffff 0000 00ff ffff 0000 00ff ffff 0000
00ff ffff 0000 00ff ffff 0000 00ff ffff
0000 00ff ffff 0000 00ff ffff 0000 00ff
ffff 0000 00ff ffff
'''
def temp():
	a=a.split()
	b=""
	for i in a:
		b+=i
	print(b)
	c="f"*300 + "0"*300
	b=""
	for i in range (600):
		b+=c[i]
		if i+1==600:
			break
		if (i+1)%4==0:
			if i==7:
				b+="\n"
			elif (i+1-8)%32==0:
				b+="\n"
			else:
				b+=" "
	#print(b)

	#Led build rule: 2 frame with the start of 1 mask


import math
from PIL import Image
length = 1531
height = 200
im = Image.new('RGB', (length, height))
ld = im.load()

def gaussian(x, a, b, c, d=0):
    return a * math.exp(-(x - b)**2 / (2 * c**2)) + d



def normalgradient():
	global im,ld
	for x in range(im.size[0]):
	    #r = int(gaussian(x, 158.8242, 201, 87.0739) + gaussian(x, 158.8242, 402, 87.0739))
	    #g = int(gaussian(x, 129.9851, 157.7571, 108.0298) + gaussian(x, 200.6831, 399.4535, 143.6828))
	    #b = int(gaussian(x, 231.3135, 206.4774, 201.5447) + gaussian(x, 17.1017, 395.8819, 39.3148))
	    r = int(255		*(x<255) + (255-(x-255))	*(x>=255 and x<511) + (0)		*(x>=511 and x<767) + (0)			*(x>=767 and x<1023) + (x-1023)			*(x>=1023 and x<1279) + (255)			*(x>=1279 and x<1531))
	    g = int(x  		*(x<255) + (255)			*(x>=255 and x<511) + (255)		*(x>=511 and x<767) + (255-(x-767))	*(x>=767 and x<1023) + (0)				*(x>=1023 and x<1279) + (0)				*(x>=1279 and x<1531))
	    b = int(0  		*(x<255) + 0				*(x>=255 and x<511) + (x-511)	*(x>=511 and x<767) + (255)			*(x>=767 and x<1023) + (255)			*(x>=1023 and x<1279) + (255-(x-1279))	*(x>=1279 and x<1531))
	    for y in range(im.size[1]):
	        ld[x, y] = (r, g, b)

	im.show()




def sunsetgradient():
	global im,ld
	for x in range(im.size[0]):
	    r = 0
	    g = 0
	    b = 0
	    for y in range(im.size[1]):
	        ld[x, y] = (r, g, b)

	im.show()

#sunsetgradient()