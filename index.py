# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 08:51:23 2019

@author: HECTOR
"""

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form> 
</body>
</html>
"""

print(html)