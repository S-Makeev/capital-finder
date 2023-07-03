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

        capital = dic.get("capital", "")

        url = f"https://restcountries.com/v3.1/capital/{capital}"

        response = requests.get(url)
        data = response.json()
        message = ""

        for country_data in data:
            name = country_data.get("name", {}).get("common", "")
            message = f"{capital} is the capital of {name}."
            break

        self.wfile.write(message.encode())

        return