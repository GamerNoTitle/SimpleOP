# -*- coding: utf-8 -*-
import time
stop_enable=1
waiting_time=10	# Setting up your waiting time after typing the command to restart/stop the server

SimpleOP_msg='''
§r====== §6SimpleOP Server Controller §r======
§6!!SimpleOP §rto open this use guide
§6!!op §rto get the OP permission
§6!!restart §rto restart the whole server (MCDR not included)
§6!!stop §rto stop the server (MCDR will be terminate too, need to enable)
§4Forked from §6Fallen_Breath/SimpleOP §4by §6GamerNoTitle
'''

def on_info(server, info):
	if info.is_player and info.content == '!!i_promise_i_will_not_abuse_OP_permission':
		server.execute('op ' + info.player)

	if info.content == '!!restart':
		time_left=waiting_time
		restart_message=''
		while True:
			restart_message='Server will restart in {} second(s), please save your work!'.format(time_left)
			server.say(restart_message)
			if(time_left==0):
				server.restart()
				break
			else:
				time.sleep(1)
				time_left=time_left-1

	if info.content == '!!stop':
		time_left=waiting_time
		if(stop_enable==1):
			stop_message=''
			while True:
				stop_message='Server will close in {} second(s), please save your work!'.format(time_left)
				server.say(stop_message)
				if(time_left==0):
					server.stop_exit()
					break
				else:
					time.sleep(1)
					time_left=time_left-1
		else:
			server.say('§4Error: NotEnabled')
			server.say('§rServer-stop function is not enabled yet, please contact your administrator to enable it!')
	if info.content == '!!SimpleOP' or info.content == '!!simpleop' or info.content == '!!sop':
		server.tell(info.player,SimpleOP_msg)
