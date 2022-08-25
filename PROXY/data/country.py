import requests


def proxy_country(proxy, type_proxy):
    try:
        proxies = {
            "http": f"{type_proxy}://{proxy}",
            "https": f"{type_proxy}://{proxy}"
        }
        response = requests.get('http://ip-api.com/json/', proxies=proxies, timeout=5, verify=False).json()
        status = response['status']
        if status == 'success':
            country = response['country']
            return country
        else:
            return False
    except(
            requests.exceptions.ProxyError,
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.TooManyRedirects,
            ConnectionResetError,
            requests.exceptions.ChunkedEncodingError,
            requests.exceptions.InvalidProxyURL,
            KeyError,
            requests.exceptions.JSONDecodeError
    ):
        return False
