from flask import Flask, make_response, redirect
import requests

app = Flask(__name__)

def get_cat(error):
    cat = requests.get('https://http.cat/%s' % error)
    print error
    if cat:
        response = make_response(cat.content)
        response.headers['Content-Type'] = 'image/jpeg'
        response.headers['location'] = '/test/'
        return response
    return 'Error downloading cat'

@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(302)
def get_error(error):
    import pdb
    #pdb.set_trace()
    code = getattr(error, 'code', None)
    if code is None:
        code = 500
    return get_cat(code)

@app.route('/')
def index():
    return get_cat(302), 302

if __name__ == '__main__':
    app.run(debug=True)
