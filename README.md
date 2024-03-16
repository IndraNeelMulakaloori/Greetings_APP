# Flask Greetings App

This is a simple Flask web application that greets users in different languages based on the language specified in the URL.

## Features

- Greets users in different languages.
- Parses greetings from a JSON file.
- Handles cases where the specified language is not available.

## Setup

1. Make sure you have Python installed on your system

2. Clone this repository

3. Install the required dependencies using pip:
 `pip install -r requirements.txt`

4. Run the Flask Application : `python3 server.py`


5. Open your web browser and visit http://localhost:5000 to see the application in action.

## Usage
### HTTP PROTOCOL METHOD (Preferred)
- Fire up the terminal and establish a TCP connection between machine and server using `netcat URL PORT`.<br>
In our case, it's `netcat localhost 8000`.<br>
- Pass in the methods (`GET`,`POST`) followed by route and HTTP Protocol.<br>
`GET /greet/<language> HTTP/1.1`

#### Demonstration:
![Terminal Demonstration](/static/Terminal.png)
### GUI Method

- Visit the root URL (http://localhost:5000) to see a simple "Hello World" message.
- Visit http://localhost:5000/greet/language to get a greeting in the specified language. Replace `<language>` with the desired language code.

**Example**:<br>
http://localhost:5000/greet/English <br>
http://localhost:5000/greet/French


## Dependencies

- Flask: A lightweight WSGI web application framework for Python.

## Citation
- Thanks [@Mohamed Suhaib](https://github.com/subbe) for [subbe/greetings.json](https://gist.github.com/subbe/94ba128e4560b50484eb6aa2556b7559)
- Thanks [@Arpit Bhayani](https://github.com/arpitbbhayani) for [HTTP Implementation](https://www.youtube.com/watch?v=SzwjnoPI--M)

## License

This project is licensed under the [MIT License](LICENSE).