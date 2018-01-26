from flask import Flask
import os


class Application(Flask):
    def __init__(self, name):
        # Subclass the Flask application
        Flask.__init__(self, name)

        # Debug settings
        if os.environ['FLASK_DEBUG']:
            self.debug = True

        # Register the core blueprint
        from application.views.core import core
        self.register_blueprint(core)

        # Register the api blueprint
        from application.views.api import api
        self.register_blueprint(api)

app = Application(__name__)
