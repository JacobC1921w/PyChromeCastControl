from requests import post as POST
from requests import get as GET
from requests.exceptions import ConnectionError
from time import sleep as delay
from http.client import responses as CODES

def CCInfo(IP):
	response = GET("http://" + IP + ":8008/setup/eureka_info", allow_redirects=True, headers={"Content-Type": "application/json"})
	if response.status_code != 200:
		return {response.status_code:CODES[response.status_code]}
	else:
		return response.json()

def CCID(IP):
	response = POST("http://" + IP + ":8008/setup/get_app_device_id", data='{"app_id":"E8C28D3C"}', allow_redirects=True, headers={"Content-Type": "application/json"})
	if response.status_code != 200:
		return {response.status_code:CODES[response.status_code]}
	else:
		return response.json()

def CCTimeZones(IP):
	response = GET("http://" + IP + ":8008/setup/supported_timezones", allow_redirects=True, headers={"Content-Type": "application/json"})
	if response.status_code != 200:
		return {response.status_code:CODES[response.status_code]}
	else:
		return response.json()

def CCLocales(IP):
	response = GET("http://" + IP + ":8008/setup/supported_locales", allow_redirects=True, headers={"Content-Type": "application/json"})
	if response.status_code != 200:
		return {response.status_code:CODES[response.status_code]}
	else:
		return response.json()

def CCReboot(IP): #
	POST("http://" + IP + ":8008/setup/reboot", data='{"params":"now"}', allow_redirects=True, headers={"Content-Type": "application/json"})

def CCFactoryReset(IP): #
	POST("http://" + IP + ":8008/setup/reboot", data='{"params":"fdr"}', allow_redirects=True, headers={"Content-Type": "application/json"})

def CCSavedNetworks(IP):
	response = GET("http://" + IP + ":8008/setup/configured_networks", allow_redirects=True, headers={"Content-Type": "application/json"})
	if response.status_code != 200:
		return {response.status_code:CODES[response.status_code]}
	else:
		return response.json()

def CCScanNetworks(IP, scanDelay=15): #
	POST("http://" + IP + ":8008/setup/scan_wifi", data='', allow_redirects=True, headers={"Content-Type": "application/json"})
	delay(scanDelay)
	response = GET("http://" + IP + ":8008/setup/scan_results", allow_redirects=True, headers={"Content-Type": "application/json"})
	if response.status_code != 200:
		return {response.status_code:CODES[response.status_code]}
	else:
		return response.json()

def CCForgetWiFi(IP, WPAID=0):
	try:
		POST("http://" + IP + ":8008/setup/forget_wifi", data='{"wpa_id":' + WPAID + '}', allow_redirects=True, headers={"Content-Type": "application/json"}, timeout=0.5)
	except:
		pass

def CCVerify(IP):
	try:
		response = GET("http://" + IP + ":8008/setup/eureka_info", allow_redirects=True, headers={"Content-Type": "application/json"})
	except ConnectionError:
		return False

	if response.status_code != 200:
		return False
	else:
		try:
			return response.json()["ip_address"] == IP
		except KeyError:
			return False

if __name__ == "__main__":
    print("This is an import-only file")
