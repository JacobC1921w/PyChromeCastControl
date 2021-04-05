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

### Information gathering
```python
CCInfo(IP)
```
Various information about the specified IP of thr ChromeCast. (ret: JSON)
- `IP`: (str) IP address of the target ChromeCast

#### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCInfo("192.168.0.133")
{'bssid': '', 'build_version': '246969', 'cast_build_revision': '1.52.246969', 'closed_caption': {}, 'connected': True, 'ethernet_connected': False, 'has_update': False, 'hotspot_bssid': 'FX:8X:9X:0X:8X:BX', 'ip_address': '192.168.0.133', 'locale': 'en-US', 'location': {'country_code': 'US', 'latitude': 255.0, 'longitude': 255.0}, 'mac_address': '00:00:00:00:00:00', 'name': 'BLAUPUNKT 4K Android TV', 'opt_in': {'crash': False, 'opencast': False, 'stats': False}, 'public_key': 'MIIBCgKCAQEAueuYvXqabggMGs5iYRCJnxDnWB2IBaYdXtRAkwlT/PDz2EDEnwsAv4TVgszY9UnwFpTAjafCFygOyBJXN9eOmD+oJOytOEHgBhPTB4d+sQUhkN6wZcagImHLTMt9Ne4Q8uge0z6pdm6ZaM7bbMTiW1RdO0Hw81L3wG4QG08GJjgShrwaaINEYhp/P3fJw4Frtv7WjxdZ2sAFjp/xDn8mcLzeGob91ITxwD+WrY8vjEnNPIq1O4lHlq3/v1t2SBFpIYUa4dxlz90DnLClkBpGJI0FohBUBY3J7JlFtRzqMFCQtFumYsPYt5ttJVKekhk5LNvBjAywoBOdJdrlaq2CNQIDAQAB', 'release_track': '', 'setup_state': 60, 'setup_stats': {'historically_succeeded': True, 'num_check_connectivity': 0, 'num_connect_wifi': 0, 'num_connected_wifi_not_saved': 0, 'num_initial_eureka_info': 0, 'num_obtain_ip': 0}, 'ssdp_udn': '26dc517c-1451-07f5-46b4-f2dde2909736', 'ssid': '', 'time_format': 1, 'tos_accepted': True, 'uptime': 28261.162158, 'version': 12, 'wpa_configured': False, 'wpa_state': 0}
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

### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCID("192.168.0.133")
{'app_device_id': 'AD8932D52906ADE62499F4F00BC123AC', 'certificate': '-----BEGIN CERTIFICATE-----\nMIID+zCCAuOgAwIBAgIJANJUtESF1APeMA0GCSqGSIb3DQEBCwUAMIGJMQswCQYD\nVQQGEwJVUzETMBEGA1UECAwKV2FzaGluZ3RvbjERMA8GA1UEBwwIS2lya2xhbmQx\nEzARBgNVBAoMCkdvb2dsZSBJbmMxETAPBgNVBAsMCFdpZGV2aW5lMSowKAYDVQQD\nDCFNVEMgVFYgYmFuZ2JhZSBNU3RhciBUMjIgQ2FzdCBJQ0EwHhcNMjEwMzIxMDAy\nNTE4WhcNNDEwMzIxMDAyNTE4WjB8MQswCQYDVQQGEwJVUzETMBEGA1UECAwKV2Fz\naGluZ3RvbjERMA8GA1UEBwwIS2lya2xhbmQxEzARBgNVBAoMCkdvb2dsZSBJbmMx\nETAPBgNVBAsMCFdpZGV2aW5lMR0wGwYDVQQDDBQtMzI5MDgwNzIyMTMwNDk0OTc5\nNDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMxWxwqloqXJsvmvdwlX\nOy2Hkp1XrqYotSmC5gqBcXNMLp6b7fDk/jReRjGTSDPqBmo0C3BWbisQ9Pwzx+C7\nuSaNvJY1iqva7L5OZ6XSRdHRV0ZPO9TcAMkbAd846V8PJOWBu8v67vsxre9FR2vn\n7XvxzjKXPblLoxmtofQUyuNY1nY1lj5gtInCgy0KAC0GQz/Cum3xiwNoR8iZtR91\nKEAVnuzg7xtSi2UkK2zM5aeZWxXBE01zU44NO02P70HAgx5wBsYVb3b7lNHbmCw+\nPh+TY3YbDAGH6seLHqsq0xM/k2iMigo9mIHv8deBX0DgmR/f+BPl5OD4JsfpdZRZ\nFy8CAwEAAaNyMHAwDAYDVR0TAQH/BAIwADALBgNVHQ8EBAMCB4AwEwYDVR0lBAww\nCgYIKwYBBQUHAwIwHQYDVR0OBBYEFIUAETZltrf7Z6ERaseBmyfrntT+MB8GA1Ud\nIwQYMBaAFFI0844bFwcKZGYRxU4DkHGs7zxVMA0GCSqGSIb3DQEBCwUAA4IBAQAy\nZymKPhHNBuJB3DbFJLGLeHBwi03G7YX/walb5kS12V13oeGfW47ELvXxVh0Xx8xi\nOwYHBskt+zfBZup+d4NKbCE1QDA9DL4kctZMsX2aVv7/YnUmWMBSTc05jxLEer/6\nIMz2INpCuVqJpIzCyC4v+rIAavIB9W0OWnk5bgY9+cYHq+a+sy5/qGnZajCukJUn\nZIkoEdyGwCMqFZ08aPw1dROH7rojlFVoXqHOOf8lVmyd2Fel2zMJB42XvDUz+tiL\np7DFMrs5SqgwOW8bLQtEWfEM5erOy5bS56UaGhz1BtAxWVmkVHhpMSKdDQpfOU2m\nbl3j/ecN6QGy4yNbfTLN\n-----END CERTIFICATE-----\n', 'signed_data': 'LC7qWGZ9Lt6Wn9ZlhmU/tb/qomOdVGgapX1Eeuf45pCZ7TeCrd40mRfflozzysAzQIrKgHKfefWOhMVNVY4jvniksy8hoDqKXNLrLdUYyaXhfJeKtFpZR955PMV2LDBEoz2xaYND80hJxZVAWMVu3ldvGL3AfnDSA0bayQEvgmWYMrukgmVnpRHezVxK3Of0YNkZ3gkgFRC/WJrugopLruZAGs87yVG0rGvmTkkDGd1IfR043oDClCXB/4B951VHlynibW0DHNzz1hIhoQ8lZDJMnlb/sD1ormfABmSzHqeyQuiVcPA5sygI5EzhJvM6rKPdTTcuIPNaQiVNsi//0w=='}
>>>
```

<br />
<br />

### Enumerating Timezone Information
```python
CCTimeZones(IP)
```
Enumerates timezone information for the target ChromeCast. <b>NOT CURRENTLY WORKING, WORKING ON FIX</b> (ret: JSON)
- `IP`: (str) IP address of the target ChromeCast

### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCTimeZones("192.168.0.133")
{404: 'Not Found'} # :(
>>>
```

<br />
<br />

### Enumerating Locale Information
```python
CCLocales(IP)
```
Enumerates locale information for the target ChromeCast. <b>NOT CURRENTLY WORKING, WORKING ON FIX</b> (ret: JSON)
- `IP`: (str) IP address of the target ChromeCast

### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCLoocales("192.168.0.133")
{404: 'Not Found'}
>>>
```

<br />
<br />

### Reboot ChromeCast
```python
CCReboot(IP)
```
Reboots the target ChromeCast (ret: None)
- `IP`: (str) IP address of the target ChromeCast

### Example:
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
Factory resets the target ChromeCast (ret: None)
- `IP`: (str) IP address of the target ChromeCast

### Example:
```python
>>> import CCCFunctions
>>> CCCFunctions.CCFactoryReset("192.168.0.133")
>>>
```

<br />
<br />

### CCSavedNetworks(IP)

### CCScanNetworks(IP, scanDelay=15)

### CCForgetWiFi(IP, WPAID=0)

### CCVerify(IP)

