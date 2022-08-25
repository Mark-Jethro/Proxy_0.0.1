#!/usr/bin/env python
# # -*- coding: utf-8 -*-

# Updated : 2022

# Bộ Công Cụ Hỗ Trợ Proxy Được Lập Trình Và Phát Triển Bởi Huỳnh Mai Nhật Minh

"""
/*
 * CÁC PHẦN MỀM VÀ CHƯƠNG TRÌNH NÀY CHỈ NHẰM MỤC ĐÍCH GIÁO DỤC!
 * NẾU BẠN THAM GIA BẤT KỲ HOẠT ĐỘNG BẤT HỢP PHÁP NÀO, CHÚNG TÔI KHÔNG CHỊU BẤT KỲ TRÁCH NHIỆM NÀO VỀ NÓ!
 * BẰNG CÁCH ĐỂ SỬ DỤNG CÁC PHẦN MỀM VÀ CHƯƠNG TRÌNH NÀY, BẠN PHẢI ĐỒNG Ý VỚI CÁC ĐIỀU KHOẢN NÀY. CẢM ƠN!
 * Copyright (C) 2022 | Huỳnh Mai Nhật Minh | All Rights Reserved
 *
 */
"""

import argparse
import sys
import os
import threading
import time
from data import http, socks4, socks5, country

try:
    import pystyle
    import requests
    from rich.console import Console
except (ModuleNotFoundError, ImportError):
    os.system("pip install pystyle -q -q -q --no-input")
    os.system("pip install requests -q -q -q --no-input")
    os.system("pip install rich -q -q -q --no-input")
    os.system("pip install PySocks -q -q -q --no-input")


sys.stdout.reconfigure(encoding='utf-8')
thread_lock = threading.Lock()

list_file_proxy = ['proxy_http.txt', 'proxy_socks4.txt', 'proxy_socks5.txt', 'proxy_socks4_socks5.txt']
console = Console()


def clear():
    if 'linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


def banner():
    console.print('\n\t[bold white]©Copyright By : Huỳnh Mai Nhật Minh')
    banner_logo = """
    
    ███╗   ███╗██╗███╗   ██╗██╗  ██╗
    ████╗ ████║██║████╗  ██║██║  ██║
    ██╔████╔██║██║██╔██╗ ██║███████║
    ██║╚██╔╝██║██║██║╚██╗██║██╔══██║
    ██║ ╚═╝ ██║██║██║ ╚████║██║  ██║
    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                            [bold blue][ 2005 ]
    
    """
    return console.print(pystyle.Center.XCenter(banner_logo), style='bold cyan ')


def check_file():
    for file_proxy in list_file_proxy:
        num_lines = sum(1 for _ in open(file_proxy))
        if file_proxy == 'proxy_http.txt':
            console.print(f'\n[bold][yellow][[red]●[yellow]][white] Number of [yellow]([blue]HTTP[yellow])[white] '
                          f'Proxy : [cyan]{num_lines}[white] Proxy Free [yellow]==> [purple]{file_proxy}')
        elif file_proxy == 'proxy_socks4.txt':
            console.print(f'\n[bold][yellow][[red]●[yellow]][white] Number of [yellow]([blue]SOCKS4[yellow])[white] '
                          f'Proxy : [cyan]{num_lines}[white] Proxy Free [yellow]==> [purple]{file_proxy}')
        elif file_proxy == 'proxy_socks5.txt':
            console.print(f'\n[bold][yellow][[red]●[yellow]][white] Number of [yellow]([blue]SOCKS5[yellow])[white] '
                          f'Proxy : [cyan]{num_lines}[white] Proxy Free [yellow]==> [purple]{file_proxy}')
        else:
            console.print(f'\n[bold][yellow][[red]●[yellow]][white] Number of [yellow]([blue]SOCKS4/5[yellow])[white] '
                          f'Proxy : [cyan]{num_lines}[white] Proxy Free [yellow]==> [purple]{file_proxy}')


def clear_file():
    for file_proxy in list_file_proxy:
        file = open(file_proxy, 'w')
        file.close()


def run_check_country(proxy):
    proxy_http = http.proxy_http(proxy)
    proxy_socks4 = socks4.proxy_socks4(proxy)
    proxy_socks5 = socks5.proxy_socks5(proxy)
    thread_lock.acquire()
    if proxy_http is False and proxy_socks4 is True and proxy_socks5 is True:
        type_proxy = 'socks5'
        country_proxy = country.proxy_country(proxy, type_proxy)
        if country_proxy is False:
            pass
        else:
            console.print(f'     [bold][white]PROXY [cyan]{proxy} [yellow]==> [blue][[green]SOCKS4/5[blue]] [yellow]==> '
                          f'[blue][[green]{country_proxy}[blue]]')
            with open('proxy_socks4_socks5.txt', 'a') as f:
                f.write(proxy + '\n')
    elif proxy_http is True and proxy_socks4 is False and proxy_socks5 is False:
        type_proxy = 'http'
        country_proxy = country.proxy_country(proxy, type_proxy)
        if country_proxy is False:
            pass
        else:
            console.print(f'     [bold][white]PROXY [cyan]{proxy} [yellow]==> [blue][[green]HTTP[blue]] [yellow]==> '
                          f'[blue][[green]{country_proxy}[blue]]')
            with open('proxy_http.txt', 'a') as f:
                f.write(proxy + '\n')
    elif proxy_http is False and proxy_socks4 is True and proxy_socks5 is False:
        type_proxy = 'socks4'
        country_proxy = country.proxy_country(proxy, type_proxy)
        if country_proxy is False:
            pass
        else:
            console.print(f'     [bold][white]PROXY [cyan]{proxy} [yellow]==> [blue][[green]SOCKS4[blue]] [yellow]==> '
                          f'[blue][[green]{country_proxy}[blue]]')
            with open('proxy_socks4.txt', 'a') as f:
                f.write(proxy + '\n')
    elif proxy_http is False and proxy_socks4 is False and proxy_socks5 is True:
        type_proxy = 'socks5'
        country_proxy = country.proxy_country(proxy, type_proxy)
        if country_proxy is False:
            pass
        else:
            console.print(f'     [bold][white]PROXY [cyan]{proxy} [yellow]==> [blue][[green]SOCKS5[blue]] [yellow]==> '
                          f'[blue][[green]{country_proxy}[blue]]')
            with open('proxy_socks5.txt', 'a') as f:
                f.write(proxy + '\n')
    else:
        pass
    thread_lock.release()


def check_country(file_proxy):
    threads = []
    clear_file()
    try:
        file = open(file_proxy, 'r').readlines()
        for proxy in file:
            thread = threading.Thread(target=run_check_country, args=(proxy.strip(),), daemon=True)
            thread.start()
            threads.append(thread)
            time.sleep(.1)
        for thread in threads:
            thread.join()
        check_file()
    except(KeyboardInterrupt,):
        check_file()


def get_proxy(type_proxy):
    list_type = []
    list_proxy = []
    link_http_proxy = [
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
        'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt',
        'https://api.openproxylist.xyz/http.txt',
        'https://www.proxy-list.download/api/v1/get?type=http',
        'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt',
        'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt',
        'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
        'https://api.proxyscrape.com/?request=displayproxies&proxytype=https'
    ]
    link_socks4_proxy = [
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks4.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
        'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt',
        'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt',
        'https://api.openproxylist.xyz/socks4.txt',
        'https://www.proxy-list.download/api/v1/get?type=socks4',
        'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4'

    ]
    link_socks5_proxy = [
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks5.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
        'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt',
        'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt',
        'https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt',
        'https://api.openproxylist.xyz/socks5.txt',
        'https://www.proxy-list.download/api/v1/get?type=socks5',
        'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5'
    ]
    if '/' in type_proxy:
        type_proxy = type_proxy.split('/')
        list_type = [x for x in type_proxy if x]
    else:
        list_type.append(type_proxy)
    for type_proxies in list_type:
        if type_proxies == 'http' or type_proxies == 'HTTP':
            for link_http in link_http_proxy:
                response = requests.get(link_http).text
                response = response.strip().split('\n')
                for proxy in response:
                    list_proxy.append(proxy.strip())
            console.print('\n[bold][yellow][[red]¤[yellow]][purple] Successfully Get Free HTTP Proxy')
        elif type_proxies == 'socks4' or type_proxies == 'SOCKS4':
            for link_socks4 in link_socks4_proxy:
                response = requests.get(link_socks4).text
                response = response.strip().split('\n')
                for proxy in response:
                    list_proxy.append(proxy.strip())
            console.print('\n[bold][yellow][[red]¤[yellow]][purple] Successfully Get Free SOCKS4 Proxy')
        elif type_proxies == 'socks5' or type_proxies == 'SOCKS5':
            for link_socks5 in link_socks5_proxy:
                response = requests.get(link_socks5).text
                response = response.strip().split('\n')
                for proxy in response:
                    list_proxy.append(proxy.strip())
            console.print('\n[bold][yellow][[red]¤[yellow]][purple] Successfully Get Free SOCKS5 Proxy')
        else:
            console.print('\n[bold][yellow]==>[red] Proxy Type To Get Invalid[/]')
            sys.exit()
        response = set(list_proxy)
        list_total_proxy = list(response)
        file = open('proxy.txt', 'w')
        for proxy in list_total_proxy:
            file.write(proxy.strip() + '\n')
        file.close()
        console.print('\n[bold][yellow]==>[green] All Proxy Saved In File [blue]([yellow]proxy.txt[blue])[/]')


def run_check_proxy(proxy):
    proxy_http = http.proxy_http(proxy)
    proxy_socks4 = socks4.proxy_socks4(proxy)
    proxy_socks5 = socks5.proxy_socks5(proxy)
    thread_lock.acquire()
    if proxy_http is False and proxy_socks4 is True and proxy_socks5 is True:
        console.print(f'     [bold][white]PROXY [cyan]{proxy} [yellow]==> [blue][[green]SOCKS4/5[blue]]')
        with open('proxy_socks4_socks5.txt', 'a') as f:
            f.write(proxy + '\n')
    elif proxy_http is True and proxy_socks4 is False and proxy_socks5 is False:
        console.print(f'     [bold][white]PROXY [cyan]{proxy} [yellow]==> [blue][[green]HTTP[blue]]')
        with open('proxy_http.txt', 'a') as f:
            f.write(proxy + '\n')
    elif proxy_http is False and proxy_socks4 is True and proxy_socks5 is False:
        console.print(f'     [bold][white]PROXY [cyan]{proxy} [yellow]==> [blue][[green]SOCKS4[blue]]')
        with open('proxy_socks4.txt', 'a') as f:
            f.write(proxy + '\n')
    elif proxy_http is False and proxy_socks4 is False and proxy_socks5 is True:
        console.print(f'     [bold][white]PROXY [cyan]{proxy} [yellow]==> [blue][[green]SOCKS5[blue]]')
        with open('proxy_socks5.txt', 'a') as f:
            f.write(proxy + '\n')
    else:
        pass
    thread_lock.release()


def check_proxy(file_proxy):
    clear_file()
    try:
        threads = []
        file = open(file_proxy, 'r').readlines()
        for proxy in file:
            thread = threading.Thread(target=run_check_proxy, args=(proxy.strip(), ), daemon=True)
            thread.start()
            threads.append(thread)
            time.sleep(.1)
        for thread in threads:
            thread.join()
        check_file()
    except(KeyboardInterrupt, ):
        check_file()


def main():
    parser = argparse.ArgumentParser(description='\033[1;97mDescription: Tool Supports All Proxy Types. Version 0.0.1',
                                     epilog='\033[1;97mAuthors: Huỳnh Mai Nhật Minh',
                                     add_help=False)
    optional = parser.add_argument_group('optional arguments', '')
    optional.add_argument('-h', '--help',
                          action='help',
                          help='show this help message and exit'
                          )
    optional.add_argument('-v',
                          '--version',
                          action='version',
                          version='%(prog)s 0.0.1'
                          )
    optional.add_argument('-e',
                          '--example',
                          action='store_true',
                          help='Examples of Tools',
                          dest='example',
                          )
    options = parser.add_argument_group('options', '')
    options.add_argument('--file',
                         metavar='',
                         help='Proxy File Name',
                         dest='file_proxy',
                         type=check_proxy,
                         action='store',
                         required=False
                         )
    options.add_argument('--get',
                         metavar='',
                         help='Get Proxy HTTP/SOCKS4/SOCKS5',
                         dest='get_proxy',
                         type=get_proxy,
                         action='store',
                         required=False,
                         )
    options.add_argument('--name',
                         metavar='',
                         help='Proxy Country Name',
                         dest='country_proxy',
                         type=check_country,
                         action='store',
                         required=False,
                         )
    args = parser.parse_args()
    if args.example:
        file_py = sys.argv[0]
        console.print(f'\n- [bold](python or python3) {file_py} --file (file.txt) [yellow]==> [white]Check Proxy. And Filter All Types of Proxy')
        console.print(f'\n- [bold](python or python3) {file_py} --get [yellow]==> [white]Get All Types of Proxy. All Proxy Updated Regularly')
        console.print(f'\n- [bold](python or python3) {file_py} --name [yellow]==> [white]Get All Country Names Proxy Types')


if __name__ == '__main__':
    clear()
    banner()
    main()
