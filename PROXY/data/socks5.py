import requests


def proxy_socks5(proxy):
    try:
        proxies = {
            "http": f"socks5://{proxy}",
            "https": f"socks5://{proxy}"
        }
        response = requests.get('http://httpbin.org/get', proxies=proxies, timeout=5, verify=False)
        if response.status_code == 200:
            return True
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
            requests.exceptions.InvalidProxyURL
    ):
        return False
