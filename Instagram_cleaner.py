import requests
from time import sleep
from json import dumps
from maskpass import advpass

def login():
	global head_login , data_login,req_login , time_sleep ,get_sessions

	url_login = "https://www.instagram.com/accounts/login/ajax/"
	head_login = {

		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'content-length': '272',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r;',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/accounts/login/',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': '0',
		'x-instagram-ajax': '790551e77c76',
		'x-requested-with': 'XMLHttpRequest'
		}
	
	data_login = {
		"username": user,
		"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}",
		"queryParams": "{}",
		"optIntoOneTap": "false"}
	
	req_login = requests.post(url_login,headers=head_login,data=data_login)
	
	if '"authenticated":true' in req_login.text:
		get_sessions = req_login.cookies['sessionid']
		print('Done login')

		if select_number == '1':
			time_sleep = int(input('[+] Enter Your Sleep: '))
			print('')
			id_following()
		elif select_number == '2':
			time_sleep = int(input('[+] Enter Your Sleep: '))
			print('')
			chat_id()
		elif select_number == '3':
			time_sleep = int(input('[+] Enter Your Sleep: '))
			print('')
			id_post()
		elif select_number == '4':
			time_sleep = int(input('[+] Enter Your Sleep: '))
			print('')
			info_save()

	elif ("two_factor") in req_login.text:
		print(f'\n{user} Has Two Factor Authentication')
		Two_Factor()
	elif ("checkpoint_url")  in req_login.text:
		print(f'\n{user} Is Secure')
		security_code()
	else:
		print('\nWrong username or password !')

def info_save():
		global  id_info_save 
		while True:
			url_info_save = f'https://www.instagram.com/{user}/?__a=1'
			
			header_info_save = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
			'cache-control': 'no-cache',
			'cookie': f'ig_did=D5BC7E80-9785-4758-B94C-E128617D353B; mid=XsL1CAAAAAG9iRyIP2cLrfuZ7CUm; ig_nrcb=1; csrftoken=origpnsxJ21mHIJCxkuOltceXsKKhTA2; sessionid={get_sessions}',
			'pragma': 'no-cache',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'cross-site',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
			sleep(time_sleep)
			req_info_save = requests.get(url_info_save,headers=header_info_save)
			try:
				id_info_save = req_info_save.json()['graphql']['user']['edge_saved_media']['edges'][0]['node']['id']
				delete_save()
			except IndexError:
				print('There is not saved post !')

				exit()

def delete_save():
 
		url_delete_save = f'https://www.instagram.com/web/save/{id_info_save}/unsave/'
		
		head_delete_save = {

			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid={get_sessions}',
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/p/CMsEWimjxqE/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
			'x-csrftoken': 'mnnbqhStTDAfu10DkI2VrW5VoCg9InFk',
			'x-ig-app-id': '936619743392459',
			'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4',
			'x-instagram-ajax': '753ce878cd6d',
			'x-requested-with': 'XMLHttpRequest'}
		
		req_delete = requests.post(url_delete_save,headers=head_delete_save)
		if '"status":"ok"' in req_delete.text:
			print('[+] The saved video has been deleted')
		else:
			print('[-] You have been banned !')

def chat_id():
		global thread_id , thread_username 
		while True:
			url_chat_id = 'https://i.instagram.com/api/v1/direct_v2/inbox/?persistentBadging=true&cursor='
			
			head_chat_id = {
				'accept': '*/*',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid={get_sessions}',
				'origin': 'https://www.instagram.com',
				'referer': 'https://www.instagram.com/',
				'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
				'sec-ch-ua-mobile': '?0',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-site',
				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
				'x-ig-app-id': '936619743392459',
				'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'}
			sleep(time_sleep)
			req_chat_id=requests.get(url_chat_id,headers=head_chat_id)
			
			try:
				thread_id = str(req_chat_id.json()['inbox']['threads'][0]['thread_id'])
				
				thread_username = str(req_chat_id.json()['inbox']['threads'][0]['users'][0]['username'])
				Delete_Chat()
			except IndexError:
				print('\nThere are no messages to delete !')

				exit()

def Delete_Chat():
		
		url_delete_chat = f'https://i.instagram.com/api/v1/direct_v2/threads/{thread_id}/hide/'
		
		head_delete_chat = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid={get_sessions}',
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
			'x-csrftoken': 'mnnbqhStTDAfu10DkI2VrW5VoCg9InFk',
			'x-ig-app-id': '1217981644879628',
			'x-ig-www-claim': 'hmac.AR24Fkd2DvunQ5ELQD_I_6FoVMTbIdkiDD08ZF2jyPhpEmIg',
			'x-instagram-ajax': '753ce878cd6d'}
		
		req_delete_chat = requests.post(url_delete_chat,headers=head_delete_chat)
		
		if '"status":"ok"' in req_delete_chat.text:
			print(f'[+] The chat has been deleted -> {thread_username}')
		
		else:
			print('[-] You have been banned ! ')

def id_post():
		global   post_id
		while True:
			url_post_id = f'https://www.instagram.com/{user}/?__a=1'
			
			head_post_id = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
			'cache-control': 'no-cache',
			'cookie': f'ig_did=D5BC7E80-9785-4758-B94C-E128617D353B; mid=XsL1CAAAAAG9iRyIP2cLrfuZ7CUm; ig_nrcb=1; csrftoken=origpnsxJ21mHIJCxkuOltceXsKKhTA2; ds_user_id=45572593982; sessionid={get_sessions}',
			'pragma': 'no-cache',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'cross-site',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
			sleep(time_sleep)
			req_post_id = requests.get(url_post_id,headers=head_post_id)
			try:
				post_id = req_post_id.json()['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['id']
				Delete_post()
			except IndexError:
				print('There are no videos to delete !')
				exit()

def Delete_post():

		url_post_delete = f'https://www.instagram.com/create/{post_id}/delete/'
		
		head_post_delete = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid={get_sessions}',
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/p/CM5_0EfBliscG9z8SJBY1iasqct_jP0jEJsNCU0/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
			'x-csrftoken': 'mnnbqhStTDAfu10DkI2VrW5VoCg9InFk',
			'x-ig-app-id': '1217981644879628',
			'x-ig-www-claim': 'hmac.AR24Fkd2DvunQ5ELQD_I_6FoVMTbIdkiDD08ZF2jyPhpEvg3',
			'x-instagram-ajax': '753ce878cd6d',
			'x-requested-with': 'XMLHttpRequest'}
		
		req_post_delete = requests.post(url_post_delete,headers=head_post_delete)
		if '"status":"ok"' in req_post_delete.text:
			print(f'[+] Deleted [ id post > {post_id}]')
		else:
			print('[!] Your account has been banned !')


def id_following():
		global get_id_following 

		url_id_following = f'https://www.instagram.com/{user}/?__a=1'
		
		head_id_following = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		'cache-control': 'no-cache',
		'cookie': f'ig_did=D5BC7E80-9785-4758-B94C-E128617D353B; mid=XsL1CAAAAAG9iRyIP2cLrfuZ7CUm; ig_nrcb=1; csrftoken=origpnsxJ21mHIJCxkuOltceXsKKhTA2; sessionid={get_sessions}',
		'pragma': 'no-cache',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'cross-site',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
		
		req_id_following = requests.get(url_id_following,headers=head_id_following)
		get_id_following = req_id_following.json()['graphql']['user']['id']
		session_following()

def session_following():
		global  id_session_following , username_session_following
		for following in range(10000):
			query_hash = 'd04b0a864b4b54837c0d870b0e77e076'

			cookies = {
			"sessionid": get_sessions,}
			
			variables = {
				"id": get_id_following,
				"first": 50}
			
			params = {
				"query_hash": query_hash,
				"variables": dumps(variables)}
			sleep(time_sleep)
			req_session_following = requests.get("https://www.instagram.com/graphql/query/", params = params, cookies = cookies)
			try:
				id_session_following = str(req_session_following.json()['data']['user']['edge_follow']['edges'][0]['node']['id'])

				username_session_following = str(req_session_following.json()['data']['user']['edge_follow']['edges'][0]['node']['username'])
				Delete_Following()	
			except IndexError:
				print('There are no posts to delete')
				exit()


def Delete_Following():
		
		url_delete_following = f'https://www.instagram.com/web/friendships/{id_session_following}/unfollow/'
		
		head_delete_following = {

			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid={get_sessions}',
			'origin': 'https://www.instagram.com',
			'referer': f'https://www.instagram.com/{user}/following/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
			'x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi',
			'x-ig-app-id': '936619743392459',
			'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq',
			'x-instagram-ajax': '753ce878cd6d',
			'x-requested-with': 'XMLHttpRequest'
			}
		
		req_delete_following = requests.post(url_delete_following,headers=head_delete_following)
		
		if '"status":"ok"' in req_delete_following.text:
			print(f'[+] Deleted username >> {username_session_following}')
		elif 'Please' in req_delete_following.text:
			print('[-] Banned, try another time !')
		else:
			print('error !')

	
def security_code():
	global time_sleep,get_sessions

	req_sec_code = req_login.json()['checkpoint_url']
	cookie_sec_code = req_login.cookies

	url_sec_code= f'https://www.instagram.com{req_sec_code}'

	req_sec_code=requests.post(url_sec_code,data=data_login,headers=head_login,cookies=cookie_sec_code)
	if ("phone_number") in req_sec_code.text:
		print("\n (0) Phone \n")
	if ("email") in req_sec_code.text:
		print("\n (1) Email \n")
	choice_number = input('Enter the type of send : ')
	data_choice = {
		"choice": choice_number}
	req_choice = requests.post(url_sec_code,data=data_choice,headers=head_login,cookies=cookie_sec_code)

	if ("security_code") in req_choice.text:
		choice_code = input('\n Enter the security code : ')
		data_code = {
			"security_code": choice_code}
		req_code = requests.post(url_sec_code,data=data_code,headers=head_login,cookies=cookie_sec_code)
		if ("ok") in req_code.text:
			print(f'@{user} logged in')

			if select_number == '1':
				time_sleep = int(input('[+] Enter sleep : '))
				print('')
				id_following()
			elif select_number == '2':
				time_sleep = int(input('[+] Enter sleep : '))
				print('')
				chat_id()
			elif select_number == '3':
				time_sleep = int(input('[+] Enter sleep : '))
				print('')
				id_post()
			elif select_number == '4':
				time_sleep = int(input('[+] Enter sleep : '))
				print('')
				info_save()
		else:
			print('\n The security code is invalid !')

def Two_Factor():

	global  time_sleep

	print('\ntwo factor')

	req_2fa_id = req_login.json()['two_factor_info']['two_factor_identifier']
	cookie_2fa = req_login.cookies
	cod = input('\n Enter the security code : ')
	
	data_2fa = {
		'username': user,
		'verificationCode': cod,
		'identifier': req_2fa_id,
		'queryParams': '{"next":"/"}'}
	
	req_2fa = requests.post('https://www.instagram.com/accounts/login/ajax/two_factor/', headers=head_login,data=data_2fa,cookies=cookie_2fa)
	
	if ("userId") in req_2fa.text:
		print(f'\n@{user} logged in\n')
		if select_number == '1':
			time_sleep = int(input('[+] Enter Your sleep: '))
			print('')
			id_following()
		elif select_number == '2':
			time_sleep = int(input('[+] Enter Your sleep: '))
			print('')
			chat_id()
		elif select_number == '3':
			time_sleep = int(input('[+] Enter Your sleep: '))
			print('')
			id_post()
		elif select_number == '4':
			time_sleep = int(input('[+] Enter sleep : '))
			print('')
			info_save()
	elif ("checkpoint_url")  in req_2fa.text:
		security_code()
	else:
		print('\n The security code is invalid !')



select_number = input(
"""
-----------------------------
[1] delete following 
-----------------------------
[2] delete Direct Message
-----------------------------
[3] delete your post 
-----------------------------
[4] delete Saved Post
-----------------------------

Choose the number: """
)


user = input("\nEnter username : ")
password = advpass("Enter password : ") # it makes paswword as ******

if __name__ == "__main__":
	login()