"""
Python files within the api directory, containing an handler variable that inherits from the BaseHTTPRequestHandler
"""
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # parse the query from path
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # response code
        self.send_response(200)
        # headers
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        capital = dic.get("capital", "")

        # create message
        url = f"https://restcountries.com/v3.1/capital/{capital}"

        response = requests.get(url)
        data = response.json()
        definitions = []
        for country_data in data:
            try:
                definition = country_data["meanings"][0]["definitions"][0]["definition"]
                definitions.append(definition)
            except (KeyError, IndexError):
                pass

        message = str(definitions)

        self.wfile.write(message.encode())

        return