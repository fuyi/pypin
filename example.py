"""client script"""
from pypin import PyPin

client = PyPin('<your access token>')

print client.me()
