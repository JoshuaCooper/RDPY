from bottle import route, run, template, get, post, request, response, static_file
from filegeneration import fileGeneration

#@route('/<name>')
#def index(name):
#    return template('<b>Hello {{name}}</b>!', name=name)

@get('/') # or @route('/login')
def index():
    return '''
        <form action="/" method="post">
            Username: <input name="username" type="text" />
            <br>
            Domain: <input name="domain" type="domain" />
            <br>
            Hostname: <input name="hostname" type="hostname" />
            <br>
            <input value="Login" type="submit" />
        </form>
    '''

@post('/') # or @route('/rdpy', method='POST')
def output():
    username = request.forms.get('username')
    domain = request.forms.get('domain')
    hostname = request.forms.get('hostname')
    fileLocation = "./dynamic_files/"+hostname+".rdp"
    print(fileLocation)
    f = open(fileLocation, "w")
    f.write(fileGeneration(username, domain, hostname))
    f.close()
    return template("""
        <html>
            <head>
            <title>Your file is freshly baked</title>
            <body>
            <a href="http://localhost:8080/files/{{filename}}.rdp">Here is your custom RDP file</a>
            </body>
            </head>
        </html>
    """, filename=hostname)

@get('/files/<filename>')
def returnfile(filename):
    return static_file(filename, root="./dynamic_files", download=filename)
    

run(host='localhost', port=8080)