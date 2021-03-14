"""
This script runs the Ecommerce application using a development server.
"""

from os import environ
from Ecommerce import app

"""
This script runs the Ecommerce application using a development server.
"""

from os import environ
import os
from flask import url_for
import Ecommerce.models as models
import Ecommerce.routes as routes
from Ecommerce import app
from flask import session


if __name__ == '__main__':
    #models.initialize()
    #try:
    #    models.User.create_user(
    #        full_name='Admin',
    #        email='admin@admin.com',
    #        password='1234',
    #        mobile_no='9999999999',
    #        admin=True
    #    )
    #except ValueError:
    #    pass
    app.run(debug = True, host='0.0.0.0', threaded=True)

#if __name__ == '__main__':
#    HOST = environ.get('SERVER_HOST', 'localhost')
#    try:
#        PORT = int(environ.get('SERVER_PORT', '5555'))
#    except ValueError:
#        PORT = 5555
#    application.run(HOST, PORT)
