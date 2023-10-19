#!/usr/bin/env python


import bs4
import requests


def get_my_ip_address():
    express_vpn_url = "https://www.expressvpn.com/what-is-my-ip"
    try:
        response = requests.get(
            express_vpn_url,
            timeout=(6, 18))
    except:
        raise Exception(f"HTTP GET to {express_vpn_url} failed!")
    try:
        soup = bs4.BeautifulSoup(response.content, "html.parser")
    except:
        raise Exception("Something went wrong trying to parse the HTML content in the response!")
    try:
        my_ip_address = soup.find("h4", class_="ip-address").text.strip('\n')
    except:
        raise Exception("Something went wrong trying to find the HTML element!")
    return my_ip_address


if __name__ == '__main__':
    print(get_my_ip_address())
