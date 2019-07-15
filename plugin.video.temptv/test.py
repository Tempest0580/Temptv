import base64
url = 'aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2pld2JteC94bWwvbWFzdGVyL2xpc3RzLzFtZW51LnR4dA=='
url = base64.b64decode(url)
print(url)