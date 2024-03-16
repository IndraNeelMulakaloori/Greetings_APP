from flask import Flask
import json
app = Flask(__name__)

# Parse greetings.json file once globally
with open('static/greetings.json') as fileptr:
    greet_dict = json.load(fileptr)

@app.route('/',methods = ['GET','POST'])
def hello_world():
    print("Entered into Hello world method")
    return 'Hello World'

@app.route('/greet/<language>',methods = ['GET','POST'])
def greet(language):

    try:
        greet = greet_dict[language]['greetings'][0]
    except:
        print("Something Went wrong, defaulting to English")
        greet = greet_dict['English']['greetings'][0]
    finally:
        return '<h1>%s</h1>' % greet
        
if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000
    app.run(host = host,port = port,debug=True)