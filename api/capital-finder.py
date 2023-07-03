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
            url = f"https://restcountries.com/v3.1/name/"
            response = requests.get(url + country)
            data = response.json()
            message = ""
            for country_data in data:
                name = country_data["name"][0]["official"]
                message = f"{capital} is the capital of {name}."
                break
            # for capital in data:
            # definition = capital["meanings"][0]["definitions"][0]["definition"]
            # definitions.append(definition)
        elif capital:
            url = f"https://restcountries.com/v3.1/capital/" 
            response = requests.get(url + capital)
            data = response.json()
            message = ""
            for capital in data:
                name = capital.get("name", {}).get("common", "")
                message = f"The capital of {name} is {capital}."
                break

        self.wfile.write(message.encode())

        return