import itchat

itchat.auto_login(hotReload=True)
itchat.dump_login_status()

users = itchat.search_friends(name=u'符新凯')
#找到UserName
userName = users[0]['UserName']
#然后给他发消息
itchat.send('hello',toUserName = userName)
