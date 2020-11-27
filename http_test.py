import urllib.request

# access the flight gear webserver and send it the value we want.
urllib.request.urlopen("http://127.0.0.1:5555/instrumentation/nd/range?value=10&submit=update").read()


