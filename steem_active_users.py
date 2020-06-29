from beem import Steem
from beem.blockchain import Blockchain
from beem.nodelist import NodeList
import time
import re


def hour_active(chain):
        nodelist = NodeList()
        nodelist.update_nodes()
        if chain=='steem':
                s = Steem(node=nodelist.get_steem_nodes())
        else:
                s = Steem(node=nodelist.get_hive_nodes())
        b=Blockchain(s)
        bl_=[]
        bl_num=int(b.get_current_block_num())
        bl_num_=bl_num-1250
        bl=b.blocks(bl_num_,bl_num)
        for i in bl:
                bl_.append(i['transactions'])

	
        x=('follower','account','voter','from','author')
        account=[]
        new=[]
        for i in x:
                acc=re.findall('"'+i+'":"(.+?)"',str(bl_))
                for l in acc:
                        if l not in account:
                                account.append(l)
        if chain=='steem':
                file=open('active_acc_steem.txt','r')
                old=file.readlines()
                file.close()
                file=open('active_acc_steem.txt','a')

                for i in account:
                        if i+'\n' not in old:
                                file.write(str(i)+'\n')
                                new.append(i)
                file.close()
        else:
                file=open('active_acc_hive.txt','r')
                old=file.readlines()
                file.close()
                file=open('active_acc_hive.txt','a')
                for i in account:
                        if i+'\n' not in old:
                                file.write(str(i)+'\n')
                                new.append(i)
                file.close()
                
        print ('one hour accounts '+chain,len(account))
        print ('one hour brand new '+chain,len(new))
        print ('total ACTIVE accounts '+chain,len(old))
	


counter=1
while True:
        print (counter)
        try:
        	hour_active('steem')
        	hour_active('hive')
        except Exception as e:
        	print (e)
        	pass
        counter+=1
        print ('__________________________')
        time.sleep(3580)
