#!/usr/bin/env python3

"""Local testing for http requests to use in the server."""

import json
import urllib.request

response = urllib.request.urlopen("http://localhost:8088/someJson")
text = response.read()
jsonObj = json.loads(text)
print("Got jsonObj:", jsonObj)

