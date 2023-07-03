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

        # retrieve the capital from the query parameters
        capital = dic.get("capital", "")

        # create the URL with the capital name
        url = f"https://restcountries.com/v3.1/capital/{capital}"

        # send a GET request to the Restcountries API
        response = requests.get(url)
        data = response.json()

        # response code
        self.send_response(200)
        # headers
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        # write the response body
        self.wfile.write(str(data).encode())

        return
