#this is MALT API Wrapper that contains definitions for communicating with JAVA web API
import requests
from config import BASE_URL


def start_test(ip, index):
    url= f"{BASE_URL}/start-test"
    params={"ipAddress": ip,"testIndex": index}
    response = requests.post(url,params)
    try:
        return response.json()
    except ValueError:
        return response.text #fallback for text response

def reset(ip):
    url= f"{BASE_URL}/reset"
    params={"ipAddress": ip}
    response = requests.post(url,params)
    try:
        return response.json()
    except ValueError:
        return response.text #fallback for text response

def get_testSettings(ip,index):
    return requests.get(f"{BASE_URL}/test-settings",params={"ipAddress": ip,"testIndex": index}).json()

def get_calibrationSettings(ip,channel):
    return requests.get(f"{BASE_URL}/calibration-settings",params={"ipAddress": ip,"channel":channel}).json()

def get_optionSettings(ip):
    return requests.get(f"{BASE_URL}/option-settings",params={"ipAddress": ip}).json()

def set_calibration(ip, payload):
    return requests.post(f"{BASE_URL}/set-calibration",params={"ipAddress": ip},json=payload).json()

def set_options(ip, payload):
    return requests.post(f"{BASE_URL}/set-option",params={"ipAddress": ip},json=payload).json()

def set_testSettings(ip,payload):
    return requests.post(f"{BASE_URL}/set-test",params={"ipAddress": ip},json=payload).json()

def is_test_running(ip):
    return requests.get(f"{BASE_URL}/is-test-running", params={"ipAddress": ip}).json()

def get_status_lights(ip):
    response = requests.get(f"{BASE_URL}/status-lights", params={"ipAddress": ip})
    try:
        return response.json()
    except ValueError:
        return response.text #fallback for text response

def get_result_code(ip):
    return requests.get(f"{BASE_URL}/result-code", params={"ipAddress": ip}).json()

def get_last_data(ip):
    response = requests.get(f"{BASE_URL}/last-data", params={"ipAddress": ip})
    try:
        return response.json()
    except ValueError:
        return response.text #fallback for text response

def configure(ip, config_json):
    response= requests.post(f"{BASE_URL}/configure", params={"ipAddress": ip}, json=config_json)
    try:
        return response.json()
    except ValueError:
        return response.text #fallback for text response
