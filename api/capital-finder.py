"""
Python files within the api directory, containing an handler variable that inherits from the BaseHTTPRequestHandler
"""
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
       def do_GET(self):
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        country = dic.get("country")
        capital = dic.get("capital")
        
        if country:
            url = "https://restcountries.com/v3.1/name/"
            message = ""
            response = requests.get(url + country)
            country_data = response.json()
            country_object = country_data[0]['capital'][0]
            message = str(f"The capital of {country} is {country_object}.")
            self.wfile.write(message.encode())

            return
        
        elif capital:
            url = "https://restcountries.com/v3.1/capital/"
            message = ""
            response = requests.get(url + capital)
            capital_data = response.json()
            capital_object = capital_data[0]['name']['common']
            message = str(f"{capital} is the capital of {capital_object}.")
            self.wfile.write(message.encode())

            return