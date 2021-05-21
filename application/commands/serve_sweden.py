"""Module for serving an API."""
from application.commands.Test2 import get_total_cases
from application.commands.Test2 import get_new_cases
from application.commands.Test2 import get_data, get_data2, get_sweden_data


from flask import Flask, send_file, redirect, url_for, render_template, request

def serve(options):
    """Serve an API."""

    # Create a Flask application
    app = Flask(__name__)

    @app.route("/")
    def index():
        """Return the index page of the website."""
        return render_template("index.html")

    @app.route("/totalcases")
    def totalcasesyeet():
        return render_template("totalcase.html", content= get_data())

    @app.route("/newcases")
    def newcasesyeet():
        return render_template("newcase.html", content= get_data2())

    @app.route("/swedencases")
    def swedencasesyeet():
        return render_template("newcase.html", content= get_data2())

    @app.route("/greeting/<name>")
    def greeting(name):
        """Return a greeting for the user."""
        return "Hello, {}!".format(name)
        
    @app.route("/", methods=["POST", "GET"])
    def totalc():
        
        data = request.form["choose-data"]
        date = request.form["date"]
        date2 = request.form["date2"]
        if data == "total":
            get_total_cases(date)
            return totalcasesyeet()
        elif data == "new":
            get_new_cases(date, date2)
            return newcasesyeet()
        else:
            get_sweden_cases(date)
            return swedencasesyeet()
        

    @app.route("/", methods=["POST", "GET"])
    def newc(date):
        date1 = request.form["date1"]
        date2 = request.form["date2"]
        
        get_new_cases(date1, date2)
            
        return newcasesyeet()


    app.run(host=options.address, port=options.port, debug=True)

def create_parser(subparsers):
    """Create an argument parser for the "serve" command."""
    parser = subparsers.add_parser("serve")
    parser.set_defaults(command=serve)
    # Add optional parameters to control the server configuration
    parser.add_argument("-p", "--port", default=8080, type=int, help="The port to listen on")
    parser.add_argument("--address", default="0.0.0.0", help="The address to listen on")


