import itchat

itchat.auto_login(hotReload=True)
itchat.dump_login_status()

users = itchat.search_friends(name=u'方宇')
#找到UserName
userName = users[0]['UserName']
#然后给他发消息

itchat.send('hello',toUserName = userName)
##
##file = open('C:\\Users\\Administrator\\Desktop\\123.txt')
##
##while 1:
##	line=file.readline()
##	print(line)
##	itchat.send(str(line),toUserName = userName)
##	if not line:
##		break
##	pass


filepath='C:/Users/Administrator/Desktop/DataMulti1_2/A1Multi1_2.asc'
	
def chat(filepath):
    file=open(filepath);
    while 1:
            line=file.readline()
            print(num)
            
            if not line:
                break
            else:
                energy=str.split(line)[1]
                if float(energy)>10000:
                        itchat.send(str(line),toUserName = userName)
                else:
                        print('Safe')
            
            pass
chat(filepath)
