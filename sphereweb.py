from bottle import Bottle, get, post, request, run, template, static_file, error
import pickle

app=Bottle()

@error(404)
@error(403)
def mistake(code):
    return 'There is something wrong!'

@app.route('/static/<filename>', name='static')
def server_static(filename):
    return static_file(filename, root='static')

@app.get('/') # or @route('/login')
def search():
    output = template('index', data=data, get_url=app.get_url)
    return output

@app.post('/')
def do_search():
    phrase = request.forms.get('phrase')
    count, results = search(data,phrase)
    if phrase:
        output = template('make_table', phrase=phrase, count=count, results=results, get_url=app.get_url)
        return output
    else:
        return "<p>Search failed.</p>"

@app.route('/stakeholder/<name>')
def show_stakeholder(name='sph-pri-fpr-biome'):
    # output = template('Hello {{name}}, how are you?', name=name)
    count, results = show_stakeholder(data, name)
    output = template('make_table', phrase=name, count=count, results=results, get_url=app.get_url)
    return output

data = pickle.load( open('alldata.pickle', 'rb') )

questions = ['1a', '1b', '2a', '2b', '3', '4a', '4b', '4c', '4d', '4e', '4f', '5a', '5b', '6a', '6b', '6c', '6d', '7a',
'7b', '7c', '7d', '8a', '8b', '8c', '8d', '8e', '9a', '9b', '10a', '10b', '10c', '10d', '10e', '10f', '11a', '11b', '11c',
'12a', '12b', '12c', '13a', '13b', '13c', '13d', '13e', '13f', '13g', '13h', '13i', '14a', '14b']

def show_stakeholder(data, stakeholder):
    results = []
    count = 0
    for question in questions:
        code_count = 0
        for response in data[stakeholder][question]:
            code_count += 1
            code = stakeholder+'-'+question+'-'+str(code_count)
            results.append([code, response])
            count += 1
    return(count, results)

def search(data, phrase):
    results = []
    count = 0
    for stakeholder in data:
        for question in questions:
            code_count = 0
            for response in data[stakeholder][question]:
                if all(word in response.lower() for word in phrase.lower().split()):
                    code_count += 1
                    code = stakeholder+'-'+question+'-'+str(code_count)
                    results.append([code, response])
                    count += 1
    return(count, results)

run(app, host='localhost', port=8080, reloader=True)
