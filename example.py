"""client script"""
from pypin import PyPin

API_CLIENT = PyPin('<your access token>')

print API_CLIENT.get_me()
