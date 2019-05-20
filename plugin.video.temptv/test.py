import base64
url = 'server_time=5/20/2019 1:38:55 AM&hash_value=VlIpmhqYthoMCOUNii34Dg==&validminutes=10080&id=0'
url = base64.b64encode(url)
print url