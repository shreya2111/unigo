#open csv file
#extract link
#use urllib to access each link
#get image out of each each

import csv


def link_ex(): 
    url_list=[]

    with open('top500domains.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            #print row
            url_list.append(row[1])
    
    return url_list
    


#print link_ex()
