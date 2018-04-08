from steem import Steem
from steem.blockchain import Blockchain
import time
import re

b=Blockchain()
s=Steem()

def hour_active():
	bl_num=int(b.get_current_block_num())
	bl_num_=bl_num-1250
	bl=(str(s.get_blocks_range(bl_num_,bl_num)))

	
	x=('follower','account','voter','from','author')
	account=[]
	for i in x:
		acc=re.findall('"'+i+'":"(.+?)"',str(bl))
		for l in acc:
			if l not in account:
				account.append(l)
		
	file=open('active_acc.txt','r')
	old=file.readlines()
	file.close()
	file=open('active_acc.txt','a')

	for i in account:
		if i+'\n' not in old:
			file.write(str(i)+'\n')
	file.close()
	print ('one hour accounts',len(account))
	print ('total accounts',len(old))


	
counter=1
while True:
	print (counter)
	try:
		hour_active()
	except Exception :
		pass
		print ('FAILED')
	counter+=1
	print ('__________________________')
	time.sleep(3600)

	
