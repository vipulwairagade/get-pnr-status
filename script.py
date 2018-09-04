import requests
from bs4 import *

pnr=['8708694048',
'8430879199',
'8430878279',
'8208677931',
'8208677931',
'8608788264',
'8208677931',
'8208693658',
'8708694048',
'8430878279',
'8208796233',
'8208693658',
'8208796233',
'8208796233',
'8208693658',
'8608788264',
'8208677931',
'8708696048',
'8208796233',
'8708694048',
'8708694048',
'8608788264',
'8208795600',
'8608788264',
'8208693658',
'8208693658',
'8308870880',
'8608788264',
'8708810604',
'8208693658',
'8430878279',
'8430878279',
]


URL_PATTERN = 'https://www.railyatri.in/pnr-status/{}' #General URL pattern for entered PNR

for pnr1 in pnr:
	#pnr = raw_input("Enter PNR Number : ")  #User Enters PNR
	print "Finding Booking Status for PNR ", pnr1
	url = URL_PATTERN.format(pnr1)
	srcCode = requests.get(url)
	plainText = srcCode.text
	soup = BeautifulSoup(plainText,"lxml")

	div = soup.find('div', {'id': 'status'}) 
	sub_soup = BeautifulSoup(str(div),"lxml")
	status = sub_soup.findAll("div",{"class":"chart-stats"})
	for x in status:
		seat = x.find('p').text
		print seat
	
#status = soup.select("div#status > div.chart-stats")[1].find('p').getText()
#print status