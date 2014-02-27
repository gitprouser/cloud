import urllib
import urllib2

url = 'http://localhost:8080/myapp/myresource/receive-task-status'
params = urllib.urlencode({'firstName': 'John'})
response = urllib2.urlopen(url, params)