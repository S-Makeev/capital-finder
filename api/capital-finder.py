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

    
    # https://restcountries.com/v3.1/capital/{capital}
        # response code
        self.send_response(200)

        # headers
        self.headers.add_header("Content-type", "text/plain")
        self.end_headers()

        capital = dic("word", "")

        # create message
        url = "https://restcountries.com/v3.1/capital/"

        response = requests.get(url + capital)
        data = response.json()
        country_res = []
        for capital_data in data:
            country = capital_data["name"][0]["common"][0]["official"]
            country_res.append(country)

        message = str(country_res)

        # respond with the formatted current time?
        self.wfile.write(message.encode())

        return