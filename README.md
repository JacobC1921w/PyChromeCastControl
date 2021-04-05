# PyChromeCastControl
A library/wrapper for remotely controlling and enumerating ChromeCast devices on a network

## Features
### This application can:
* Scan the network
* Get certificate data from hosts
* Get general information about hosts (build, WiFi BSSID, locale, name, etc.)
* Get locale information from hosts
* Enumerate saved network data from hosts
* Reboot hosts
* Factory reset hosts, and
* Enumerate timezone data from hosts

### Other features include:
* Verbosity
* Nice graphics
* Multiple device handlers
* Verification of each command

## Installation:
```bash
git clone https://github.com/JacobC1921/PyChromeCastControl
cd PyChromeCastControl
chmod +x PyChromeCastControl.py CCCFunctions.py
python PyChromeCastControl.py
```

## Requirements:
* `PyNetTools` (included)
* `PyPrintSystem` (included)
* `getpass`
* `pygments`
* `json`

## `CCCFunctions.py`
Included is a library for you own use. It is provided under the MIT license, and you are free to use (credit would be nice though).

## Installation (using `git`)
```bash
git clone https://github.com/JacobC1921/PyChromeCastControl
mv PyChromeCastControl/CCCFunctions.py <ProjectDir>
chmod <ProjectDIR>/CCCFunctions.py
```
Then simply import it using `import CCCFunctions`

## Installation (using `curl`)
```bash
cd <ProjectDIR>
curl https://raw.githubusercontent.com/JacobC1921/PyChromeCastControl/main/CCCFunctions.py -O CCCFunctions.py
chmod +x CCCFunctions.py
```
Then, again, simply import it using `import CCCFunctions`

### Information gathering
```python
CCInfo(IP)
```
Various information about the specified IP of thr ChromeCast. (ret: JSON)
- `IP`: (str) IP address of the target ChromeCast

##### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCInfo("192.168.0.149")
{'bssid': 'dX:3X:1X:1X:eX:5X', 'build_version': '230474', 'cast_build_revision': '1.50.230474', 'closed_caption': {}, 'connected': True, 'ethernet_connected': False, 'has_update': False, 'hotspot_bssid': 'FX:8X:CX:7X:8X:3X', 'ip_address': '192.168.0.149', 'locale': 'en-AU', 'location': {'country_code': 'AU', 'latitude': 255.0, 'longitude': 255.0}, 'mac_address': '5X:6X:0X:5X:6X:0X', 'name': 'Family room TV', 'noise_level': -94, 'opencast_pin_code': 'XXXX', 'opt_in': {'crash': False, 'opencast': True, 'stats': False}, 'public_key': 'MIIBCgKCAQEArzEBxETGLTJqkzFTedKpHwW5nQzecKxc7KnphcuurDKNvu/4BowJqqybjLH16KnYrk+LmYWkeYMDaotRtfbNom88foeYS8oOMFqkyBiU2JI0xr9DH2x7vYLWLRYzwMCBzZE5ROQiYtWf1yXzTgxcXQ3i7WyH4tBMQA+N5edDW3PRR8E9hapHbwLCfQYccRAR9+03zopBMhFZR4/+hAosz+LjMv2hYbABNdT5H1fBDqtSjO2RTpbKUhFoDWxh2ICodeXgemh+jAbvXnkU14pzfj8a228t6dnNWwAPJHVQXGPvJlDNNA8osigje5D4vAUvov68cDdSC9mCWEXI/zrpiQIDAQAB', 'release_track': 'preview-joining-stable-channel', 'setup_state': 60, 'setup_stats': {'historically_succeeded': True, 'num_check_connectivity': 0, 'num_connect_wifi': 0, 'num_connected_wifi_not_saved': 0, 'num_initial_eureka_info': 0, 'num_obtain_ip': 0}, 'signal_level': -59, 'ssdp_udn': 'd22acfc2-88c8-605f-8706-af7bcd598f9b', 'ssid': 'XXXXXXXXXXXXX-5G', 'time_format': 1, 'timezone': 'Australia/Sydney', 'tos_accepted': True, 'uptime': 356.06511, 'version': 12, 'wpa_configured': True, 'wpa_id': 2, 'wpa_state': 10}
>>>
```

<br />
<br />

### Getting Certificate Information
```python
CCID(IP)
```
Enumerates certificate information for the targeted ChromeCast. (ret: JSON)
- `IP`: (str) IP address of the target ChromeCast

#### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCID("192.168.0.149")
{'app_device_id': '8E47DFDFC207C262C691A90E5402C461', 'certificate': '-----BEGIN CERTIFICATE-----\nMIIDpzCCAo+gAwIBAgIEWCr4tDANBgkqhkiG9w0BAQUFADB+MQswCQYDVQQGEwJV\nUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNTW91bnRhaW4gVmlldzET\nMBEGA1UECgwKR29vZ2xlIEluYzENMAsGA1UECwwEQ2FzdDEeMBwGA1UEAwwVQ2hy\nb21lY2FzdCBJQ0EgNSAoNEspMB4XDTE2MTExNTExNTk0OFoXDTM2MTExMDExNTk0\nOFowfDELMAkGA1UEBhMCVVMxDTALBgNVBAsMBENhc3QxFjAUBgNVBAcMDU1vdW50\nYWluIFZpZXcxEzARBgNVBAoMCkdvb2dsZSBJbmMxEzARBgNVBAgMCkNhbGlmb3Ju\naWExHDAaBgNVBAMME0NZUTlSQSBGQThGQ0E3ODg4M0QwggEiMA0GCSqGSIb3DQEB\nAQUAA4IBDwAwggEKAoIBAQC8h/Uda/eC8oefS22BjeRe9N2pqj+XB9/fnJz3wATr\nxEA4Q9Vk2xkzxSObilLb2ycvDF7jtC9cH2FGlhCyBUsW1tfup6XOLfhNv9gJQV69\noVh6+9Vp7XAakM9IM5eejg3482Xxac9q/lQ3CwFcDWphKogpROQ5+6au1Rb1K8fE\nx4yNdKczibjmOwkTEzSr1/e1GoMvPrWfU20hkIG6CSTs5npD1lbCbvV68Kw2d5kl\nojsz9QLjAjlXTJ2Lwxt2qsX3OUoqTLz1sKU/0ymVjGl7R2NinaZZPkWqf6HQIEEX\ntsRt4gbOd5ZqKk/EDyD4/8C7KWolApMpjXUu2sixD2dJAgMBAAGjLzAtMAkGA1Ud\nEwQCMAAwCwYDVR0PBAQDAgeAMBMGA1UdJQQMMAoGCCsGAQUFBwMCMA0GCSqGSIb3\nDQEBBQUAA4IBAQBLasJCnf7FKFm9VF/ILiN2NJ1dp9zOIwkcuuSb8t/sbmWwgsaA\nLNrN0lxIY0q5Bzw1Xyu0VZL88RWNd4mZKiiOaIhVA9vSj+jvrBJ04pfKBfccx6+L\ndTEM4o/v6l4GHJVId4SxeohM1X9vXEPmsAt0EDQuakSfT+dOCGmXJJom4zJiG0Yk\nva1D5MMRVKY7tgRhGbhyT543g4CDZu7/pqvIY2SZZvQJ0GNCxnHrtHwHdG8bkNV1\nhZIY5ALm412zoK+Y/N2RK86TnG0oVN49Tc1FlKjAOsI/eD70M5MAyR3qZ9gSdWl/\nUhiP+lF9HVS/3x7IpTDEAu01EcyQ33QOlaAL\n-----END CERTIFICATE-----\n', 'signed_data': 'B1sRR9TC8jVWXZ86lhWEFlPUIuQ6ScvWx6rytu8dOl4aYFrZbZpbgWxThtkhafJf8wPzunVLGOFyGasnhp78A9yLwhMqPodKiPmyEY40OU2+Mym9XCDh3nsAMbLWUW0rt+AGvJd83p/eiGi/sSEDwVyIMX9esuRxyAfHO0rD1pw0jkyIw61bDreHqEpoiDieI5/sI34Cxuql0lfZ8aMhCy6wKBpusUULhgt/yYdzZQMiZUTGw/hY5a0lWdDHLCuLoNIzqCNYZjxg3X1X/sItJuIw8Ot2MqG5fBgrf3B0gFGQR/VEM22Kw2L7paMlt1UTW5uMrnlRvm/vyl4qy4D9nw=='}
```

<br />
<br />

### Enumerating Timezone Information
```python
CCTimeZones(IP)
```
Enumerates timezone information for the target ChromeCast. (ret: JSON)
- `IP`: (str) IP address of the target ChromeCast

#### Example:
```python
>>> CCCFunctions.CCTimeZones("192.168.0.149")
[{'display_string': 'Samoa Standard Time (Midway)', 'offset': -660, 'timezone': 'Pacific/Midway'}, {'display_string': 'Hawaii-Aleutian Standard Time (Honolulu)', 'offset': -600, 'timezone': 'Pacific/Honolulu'}, {'display_string': 'Hawaii-Aleutian Daylight Time (Adak)', 'offset': -540, 'timezone': 'America/Adak'}, {'display_string': 'Alaska Daylight Time (Anchorage)', 'offset': -480, 'timezone': 'America/Anchorage'}, {'display_string': 'Pacific Daylight Time (Los Angeles)', 'offset': -420, 'timezone': 'America/Los_Angeles'}, {'display_string': 'Pacific Daylight Time (Vancouver)', 'offset': -420, 'timezone': 'America/Vancouver'}, {'display_string': 'Pacific Daylight Time (Tijuana)', 'offset': -420, 'timezone': 'America/Tijuana'}, {'display_string': 'Mountain Standard Time (Phoenix)', 'offset': -420, 'timezone': 'America/Phoenix'}, {'display_string': 'Mountain Daylight Time (Denver)', 'offset': -360, 'timezone': 'America/Denver'}, {'display_string': 'Mountain Daylight Time (Edmonton)', 'offset': -360, 'timezone': 'America/Edmonton'}, {'display_string': 'Mexican Pacific Daylight Time (Chihuahua)', 'offset': -360, 'timezone': 'America/Chihuahua'}, {'display_string': 'Central Standard Time (Regina)', 'offset': -360, 'timezone': 'America/Regina'}, {'display_string': 'Central Standard Time (Costa Rica)', 'offset': -360, 'timezone': 'America/Costa_Rica'}, {'display_string': 'Central Daylight Time (Chicago)', 'offset': -300, 'timezone': 'America/Chicago'}, {'display_string': 'Central Daylight Time (Mexico City)', 'offset': -300, 'timezone': 'America/Mexico_City'}, {'display_string': 'Central Daylight Time (Winnipeg)', 'offset': -300, 'timezone': 'America/Winnipeg'}, {'display_string': 'Colombia Standard Time (Bogota)', 'offset': -300, 'timezone': 'America/Bogota'}, {'display_string': 'Eastern Daylight Time (New York)', 'offset': -240, 'timezone': 'America/New_York'}, {'display_string': 'Eastern Daylight Time (Toronto)', 'offset': -240, 'timezone': 'America/Toronto'}, {'display_string': 'Venezuela Time (Caracas)', 'offset': -240, 'timezone': 'America/Caracas'}, {'display_string': 'Atlantic Standard Time (Barbados)', 'offset': -240, 'timezone': 'America/Barbados'}, {'display_string': 'Atlantic Daylight Time (Halifax)', 'offset': -180, 'timezone': 'America/Halifax'}, {'display_string': 'Amazon Standard Time (Manaus)', 'offset': -240, 'timezone': 'America/Manaus'}, {'display_string': 'Chile Standard Time (Santiago)', 'offset': -240, 'timezone': 'America/Santiago'}, {'display_string': 'Newfoundland Daylight Time (St Johns)', 'offset': -150, 'timezone': 'America/St_Johns'}, {'display_string': 'Brasilia Standard Time (Sao Paulo)', 'offset': -180, 'timezone': 'America/Sao_Paulo'}, {'display_string': 'Brasilia Standard Time (Araguaina)', 'offset': -180, 'timezone': 'America/Araguaina'}, {'display_string': 'Argentina Standard Time (Buenos Aires)', 'offset': -180, 'timezone': 'America/Argentina/Buenos_Aires'}, {'display_string': 'Argentina Standard Time (San Luis)', 'offset': -180, 'timezone': 'America/Argentina/San_Luis'}, {'display_string': 'Uruguay Standard Time (Montevideo)', 'offset': -180, 'timezone': 'America/Montevideo'}, {'display_string': 'West Greenland Summer Time (Godthab)', 'offset': -120, 'timezone': 'America/Godthab'}, {'display_string': 'South Georgia Time (South Georgia)', 'offset': -120, 'timezone': 'Atlantic/South_Georgia'}, {'display_string': 'Cape Verde Standard Time (Cape Verde)', 'offset': -60, 'timezone': 'Atlantic/Cape_Verde'}, {'display_string': 'Azores Summer Time (Azores)', 'offset': 0, 'timezone': 'Atlantic/Azores'}, {'display_string': 'GMT+01:00 (Casablanca)', 'offset': 60, 'timezone': 'Africa/Casablanca'}, {'display_string': 'British Summer Time (London)', 'offset': 60, 'timezone': 'Europe/London'}, {'display_string': 'Irish Standard Time (Dublin)', 'offset': 60, 'timezone': 'Europe/Dublin'}, {'display_string': 'Central European Summer Time (Amsterdam)', 'offset': 120, 'timezone': 'Europe/Amsterdam'}, {'display_string': 'Central European Summer Time (Belgrade)', 'offset': 120, 'timezone': 'Europe/Belgrade'}, {'display_string': 'Central European Summer Time (Berlin)', 'offset': 120, 'timezone': 'Europe/Berlin'}, {'display_string': 'Central European Summer Time (Brussels)', 'offset': 120, 'timezone': 'Europe/Brussels'}, {'display_string': 'Central European Summer Time (Copenhagen)', 'offset': 120, 'timezone': 'Europe/Copenhagen'}, {'display_string': 'Western European Summer Time (Lisbon)', 'offset': 60, 'timezone': 'Europe/Lisbon'}, {'display_string': 'Central European Summer Time (Madrid)', 'offset': 120, 'timezone': 'Europe/Madrid'}, {'display_string': 'Central European Summer Time (Oslo)', 'offset': 120, 'timezone': 'Europe/Oslo'}, {'display_string': 'Central European Summer Time (Paris)', 'offset': 120, 'timezone': 'Europe/Paris'}, {'display_string': 'Central European Summer Time (Rome)', 'offset': 120, 'timezone': 'Europe/Rome'}, {'display_string': 'Central European Summer Time (Stockholm)', 'offset': 120, 'timezone': 'Europe/Stockholm'}, {'display_string': 'Central European Summer Time (Sarajevo)', 'offset': 120, 'timezone': 'Europe/Sarajevo'}, {'display_string': 'Central European Summer Time (Vienna)', 'offset': 120, 'timezone': 'Europe/Vienna'}, {'display_string': 'Central European Summer Time (Warsaw)', 'offset': 120, 'timezone': 'Europe/Warsaw'}, {'display_string': 'Central European Summer Time (Zurich)', 'offset': 120, 'timezone': 'Europe/Zurich'}, {'display_string': 'Central Africa Time (Windhoek)', 'offset': 120, 'timezone': 'Africa/Windhoek'}, {'display_string': 'West Africa Standard Time (Lagos)', 'offset': 60, 'timezone': 'Africa/Lagos'}, {'display_string': 'West Africa Standard Time (Brazzaville)', 'offset': 60, 'timezone': 'Africa/Brazzaville'}, {'display_string': 'Eastern European Standard Time (Cairo)', 'offset': 120, 'timezone': 'Africa/Cairo'}, {'display_string': 'Central Africa Time (Harare)', 'offset': 120, 'timezone': 'Africa/Harare'}, {'display_string': 'Central Africa Time (Maputo)', 'offset': 120, 'timezone': 'Africa/Maputo'}, {'display_string': 'South Africa Standard Time (Johannesburg)', 'offset': 120, 'timezone': 'Africa/Johannesburg'}, {'display_string': 'Eastern European Summer Time (Helsinki)', 'offset': 180, 'timezone': 'Europe/Helsinki'}, {'display_string': 'Eastern European Summer Time (Athens)', 'offset': 180, 'timezone': 'Europe/Athens'}, {'display_string': 'Eastern European Summer Time (Amman)', 'offset': 180, 'timezone': 'Asia/Amman'}, {'display_string': 'Eastern European Summer Time (Beirut)', 'offset': 180, 'timezone': 'Asia/Beirut'}, {'display_string': 'Israel Daylight Time (Jerusalem)', 'offset': 180, 'timezone': 'Asia/Jerusalem'}, {'display_string': 'Moscow Standard Time (Minsk)', 'offset': 180, 'timezone': 'Europe/Minsk'}, {'display_string': 'Arabia Standard Time (Baghdad)', 'offset': 180, 'timezone': 'Asia/Baghdad'}, {'display_string': 'Arabia Standard Time (Riyadh)', 'offset': 180, 'timezone': 'Asia/Riyadh'}, {'display_string': 'Arabia Standard Time (Kuwait)', 'offset': 180, 'timezone': 'Asia/Kuwait'}, {'display_string': 'Eastern Africa Time (Nairobi)', 'offset': 180, 'timezone': 'Africa/Nairobi'}, {'display_string': 'Iran Daylight Time (Tehran)', 'offset': 270, 'timezone': 'Asia/Tehran'}, {'display_string': 'Moscow Standard Time (Moscow)', 'offset': 180, 'timezone': 'Europe/Moscow'}, {'display_string': 'Gulf Standard Time (Dubai)', 'offset': 240, 'timezone': 'Asia/Dubai'}, {'display_string': 'Georgia Standard Time (Tbilisi)', 'offset': 240, 'timezone': 'Asia/Tbilisi'}, {'display_string': 'Mauritius Standard Time (Mauritius)', 'offset': 240, 'timezone': 'Indian/Mauritius'}, {'display_string': 'Azerbaijan Standard Time (Baku)', 'offset': 240, 'timezone': 'Asia/Baku'}, {'display_string': 'Armenia Standard Time (Yerevan)', 'offset': 240, 'timezone': 'Asia/Yerevan'}, {'display_string': 'Afghanistan Time (Kabul)', 'offset': 270, 'timezone': 'Asia/Kabul'}, {'display_string': 'Pakistan Standard Time (Karachi)', 'offset': 300, 'timezone': 'Asia/Karachi'}, {'display_string': 'Turkmenistan Standard Time (Ashgabat)', 'offset': 300, 'timezone': 'Asia/Ashgabat'}, {'display_string': 'West Kazakhstan Time (Oral)', 'offset': 300, 'timezone': 'Asia/Oral'}, {'display_string': 'India Standard Time (Kolkata)', 'offset': 330, 'timezone': 'Asia/Kolkata'}, {'display_string': 'India Standard Time (Colombo)', 'offset': 330, 'timezone': 'Asia/Colombo'}, {'display_string': 'Nepal Time (Kathmandu)', 'offset': 345, 'timezone': 'Asia/Kathmandu'}, {'display_string': 'Yekaterinburg Standard Time (Yekaterinburg)', 'offset': 300, 'timezone': 'Asia/Yekaterinburg'}, {'display_string': 'East Kazakhstan Time (Almaty)', 'offset': 360, 'timezone': 'Asia/Almaty'}, {'display_string': 'Bangladesh Standard Time (Dhaka)', 'offset': 360, 'timezone': 'Asia/Dhaka'}, {'display_string': 'Myanmar Time (Rangoon)', 'offset': 390, 'timezone': 'Asia/Rangoon'}, {'display_string': 'Indochina Time (Bangkok)', 'offset': 420, 'timezone': 'Asia/Bangkok'}, {'display_string': 'Western Indonesia Time (Jakarta)', 'offset': 420, 'timezone': 'Asia/Jakarta'}, {'display_string': 'Omsk Standard Time (Omsk)', 'offset': 360, 'timezone': 'Asia/Omsk'}, {'display_string': 'Novosibirsk Standard Time (Novosibirsk)', 'offset': 420, 'timezone': 'Asia/Novosibirsk'}, {'display_string': 'China Standard Time (Shanghai)', 'offset': 480, 'timezone': 'Asia/Shanghai'}, {'display_string': 'Hong Kong Standard Time (Hong Kong)', 'offset': 480, 'timezone': 'Asia/Hong_Kong'}, {'display_string': 'Malaysia Time (Kuala Lumpur)', 'offset': 480, 'timezone': 'Asia/Kuala_Lumpur'}, {'display_string': 'Singapore Standard Time (Singapore)', 'offset': 480, 'timezone': 'Asia/Singapore'}, {'display_string': 'Philippine Standard Time (Manila)', 'offset': 480, 'timezone': 'Asia/Manila'}, {'display_string': 'Taipei Standard Time (Taipei)', 'offset': 480, 'timezone': 'Asia/Taipei'}, {'display_string': 'Central Indonesia Time (Makassar)', 'offset': 480, 'timezone': 'Asia/Makassar'}, {'display_string': 'Krasnoyarsk Standard Time (Krasnoyarsk)', 'offset': 420, 'timezone': 'Asia/Krasnoyarsk'}, {'display_string': 'Australian Western Standard Time (Perth)', 'offset': 480, 'timezone': 'Australia/Perth'}, {'display_string': 'Australian Central Western Standard Time (Eucla)', 'offset': 525, 'timezone': 'Australia/Eucla'}, {'display_string': 'Irkutsk Standard Time (Irkutsk)', 'offset': 480, 'timezone': 'Asia/Irkutsk'}, {'display_string': 'Korean Standard Time (Seoul)', 'offset': 540, 'timezone': 'Asia/Seoul'}, {'display_string': 'Japan Standard Time (Tokyo)', 'offset': 540, 'timezone': 'Asia/Tokyo'}, {'display_string': 'Eastern Indonesia Time (Jayapura)', 'offset': 540, 'timezone': 'Asia/Jayapura'}, {'display_string': 'Australian Central Standard Time (Adelaide)', 'offset': 570, 'timezone': 'Australia/Adelaide'}, {'display_string': 'Australian Central Standard Time (Darwin)', 'offset': 570, 'timezone': 'Australia/Darwin'}, {'display_string': 'Australian Eastern Standard Time (Brisbane)', 'offset': 600, 'timezone': 'Australia/Brisbane'}, {'display_string': 'Australian Eastern Standard Time (Hobart)', 'offset': 600, 'timezone': 'Australia/Hobart'}, {'display_string': 'Australian Eastern Standard Time (Sydney)', 'offset': 600, 'timezone': 'Australia/Sydney'}, {'display_string': 'Yakutsk Standard Time (Yakutsk)', 'offset': 540, 'timezone': 'Asia/Yakutsk'}, {'display_string': 'Chamorro Standard Time (Guam)', 'offset': 600, 'timezone': 'Pacific/Guam'}, {'display_string': 'Papua New Guinea Time (Port Moresby)', 'offset': 600, 'timezone': 'Pacific/Port_Moresby'}, {'display_string': 'Vladivostok Standard Time (Vladivostok)', 'offset': 600, 'timezone': 'Asia/Vladivostok'}, {'display_string': 'Sakhalin Standard Time (Sakhalin)', 'offset': 660, 'timezone': 'Asia/Sakhalin'}, {'display_string': 'Magadan Standard Time (Magadan)', 'offset': 660, 'timezone': 'Asia/Magadan'}, {'display_string': 'New Zealand Standard Time (Auckland)', 'offset': 720, 'timezone': 'Pacific/Auckland'}, {'display_string': 'Fiji Standard Time (Fiji)', 'offset': 720, 'timezone': 'Pacific/Fiji'}, {'display_string': 'Marshall Islands Time (Majuro)', 'offset': 720, 'timezone': 'Pacific/Majuro'}, {'display_string': 'Tonga Standard Time (Tongatapu)', 'offset': 780, 'timezone': 'Pacific/Tongatapu'}, {'display_string': 'Apia Standard Time (Apia)', 'offset': 780, 'timezone': 'Pacific/Apia'}, {'display_string': 'Line Islands Time (Kiritimati)', 'offset': 840, 'timezone': 'Pacific/Kiritimati'}]
>>>
```

<br />
<br />

### Enumerating Locale Information
```python
CCLocales(IP)
```
Enumerates locale information for the target ChromeCast. (ret: JSON)
- `IP`: (str) IP address of the target ChromeCast

#### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCLocales("192.168.0.149")
[{'display_string': 'Amharic - አማርኛ', 'locale': 'am'}, {'display_string': 'Arabic - العربية', 'locale': 'ar'}, {'display_string': 'Bulgarian - български', 'locale': 'bg'}, {'display_string': 'Bengali - বাংলা', 'locale': 'bn'}, {'display_string': 'Catalan - català', 'locale': 'ca'}, {'display_string': 'Czech - čeština', 'locale': 'cs'}, {'display_string': 'Danish - dansk', 'locale': 'da'}, {'display_string': 'German - Deutsch', 'locale': 'de'}, {'display_string': 'Greek - Ελληνικά', 'locale': 'el'}, {'display_string': 'English (United Kingdom)', 'locale': 'en-GB'}, {'display_string': 'English (United States)', 'locale': 'en-US'}, {'display_string': 'Spanish - español', 'locale': 'es'}, {'display_string': 'Spanish (Latin America) - español (Latinoamérica)', 'locale': 'es-419'}, {'display_string': 'Estonian - eesti', 'locale': 'et'}, {'display_string': 'Persian - فارسی', 'locale': 'fa'}, {'display_string': 'Finnish - suomi', 'locale': 'fi'}, {'display_string': 'Filipino', 'locale': 'fil'}, {'display_string': 'French - français', 'locale': 'fr'}, {'display_string': 'Gujarati - ગુજરાતી', 'locale': 'gu'}, {'display_string': 'Hebrew - עברית', 'locale': 'he'}, {'display_string': 'Hindi - हिन्दी', 'locale': 'hi'}, {'display_string': 'Croatian - hrvatski', 'locale': 'hr'}, {'display_string': 'Hungarian - magyar', 'locale': 'hu'}, {'display_string': 'Indonesian - Indonesia', 'locale': 'id'}, {'display_string': 'Italian - italiano', 'locale': 'it'}, {'display_string': 'Japanese - 日本語', 'locale': 'ja'}, {'display_string': 'Kannada - ಕನ್ನಡ', 'locale': 'kn'}, {'display_string': 'Korean - 한국어', 'locale': 'ko'}, {'display_string': 'Lithuanian - lietuvių', 'locale': 'lt'}, {'display_string': 'Latvian - latviešu', 'locale': 'lv'}, {'display_string': 'Malayalam - മലയാളം', 'locale': 'ml'}, {'display_string': 'Marathi - मराठी', 'locale': 'mr'}, {'display_string': 'Malay - Melayu', 'locale': 'ms'}, {'display_string': 'Norwegian Bokmål - norsk bokmål', 'locale': 'nb'}, {'display_string': 'Dutch - Nederlands', 'locale': 'nl'}, {'display_string': 'Polish - polski', 'locale': 'pl'}, {'display_string': 'Portuguese (Brazil) - português (Brasil)', 'locale': 'pt-BR'}, {'display_string': 'Portuguese (Portugal) - português (Portugal)', 'locale': 'pt-PT'}, {'display_string': 'Romanian - română', 'locale': 'ro'}, {'display_string': 'Russian - русский', 'locale': 'ru'}, {'display_string': 'Slovak - slovenčina', 'locale': 'sk'}, {'display_string': 'Slovenian - slovenščina', 'locale': 'sl'}, {'display_string': 'Serbian - српски', 'locale': 'sr'}, {'display_string': 'Swedish - svenska', 'locale': 'sv'}, {'display_string': 'Swahili - Kiswahili', 'locale': 'sw'}, {'display_string': 'Tamil - தமிழ்', 'locale': 'ta'}, {'display_string': 'Telugu - తెలుగు', 'locale': 'te'}, {'display_string': 'Thai - ไทย', 'locale': 'th'}, {'display_string': 'Turkish - Türkçe', 'locale': 'tr'}, {'display_string': 'Ukrainian - українська', 'locale': 'uk'}, {'display_string': 'Vietnamese - Tiếng Việt', 'locale': 'vi'}, {'display_string': 'Chinese (Simplified) - 中文（简体）', 'locale': 'zh-CN'}, {'display_string': 'Chinese (Traditional) - 中文（繁體）', 'locale': 'zh-TW'}, {'display_string': 'English (Australia)', 'locale': 'en-AU'}, {'display_string': 'English (Canada)', 'locale': 'en-CA'}, {'display_string': 'English (India)', 'locale': 'en-IN'}, {'display_string': 'English (Singapore)', 'locale': 'en-SG'}, {'display_string': 'Spanish (United States) - español (Estados Unidos)', 'locale': 'es-US'}, {'display_string': 'French (Canada) - français (Canada)', 'locale': 'fr-CA'}]
>>>
```

<br />
<br />

### Reboot ChromeCast
```python
CCReboot(IP)
```
Reboots the target ChromeCast. <b>Currently not working, trying to fix :)</b> (ret: None)
- `IP`: (str) IP address of the target ChromeCast

#### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCReboot("192.168.0.133")
>>>
```

<br />
<br />

### Factory Reset ChromeCast
```python
CCFactoryReset(IP)
```
Factory resets the target ChromeCast. <b>Currently not working, trying to fix :)</b> (ret: None)
- `IP`: (str) IP address of the target ChromeCast

#### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCFactoryReset("192.168.0.133")
>>>
```

<br />
<br />

### Enumerating Saved Networks
```python
CCSavedNetworks(IP)
```
Shows information about any saved networks stored on the ChromeCast. <b>Not working, and I'm not sure I'll be able to fix, but I'm working on it!</b> (ret: JSON)
- `IP`: (str) IP address of the target ChromeCast

#### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCSavedNetworks("192.168.0.149")
{403: 'Forbidden'}
>>>
```

<br />
<br />

### Pivot Scanning WiFi
```python
CCScanNetworks(IP, scanDelay=15)
```
Scans and displays WiFi Access Point information through the targetted ChromeCast. <b>Also not working, but I'll try my best :)</b> (ret: JSON)
- `IP`: (str) IP address of the target ChromeCast
- `scanDelay`: (int) Delay (in seconds) between scan packet and fetch packet

#### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCScanNetworks("192.168.0.149")
{403: 'Forbidden'}
>>>
```

<br />
<br />

### Forgetting WiFi Networks
```python
CCForgetWiFi(IP, WPAID=0)
```
Deletes WiFi networks from the targetted ChromeCast. `WPAID` is the `wpa_id` integer retrieved from either `CCInfo()` or `CCSavedNetworks()`. <b>Lastly, also not working, sorry!</b>. (ret: JSON)
- `IP`: (str) IP address of the target ChromeCast
- `WPAID`: (int) `wpa_id` of the target WiFi Access Point

#### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCForgetWiFi("192.168.0.149", 2)
>>>
```

<br />
<br />

### Verifying ChromeCast
```python
CCVerify(IP)
```
Verifies whether the specified target ChromeCast is indeed a ChromeCast, using port checking, and API scraping. (ret: bool)
- `IP`: (str) IP address of the target ChromeCast

#### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCVerify("192.168.0.149") # Is a ChromeCast
True
>>> CCCFunction.CCVerify("192.168.0.1") # Isn't a ChromeCast
False
>>>
```
