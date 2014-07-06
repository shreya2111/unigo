import urllib2
import link_extractor as le


urllist=le.link_ex()


for i in urllist:
    print i
    url=str('http://www.')+i
    response=urllib2.urlopen(url)
    print response.read()


'''
file="d.txt"
url="http://www.pythonforbeginners.com/"
response=urllib2.urlopen(url)

fh=open(file,"w")

fh.write(response.read())
fh.close()

#with open(file,'w') as f: f.write(response.read())
'''
