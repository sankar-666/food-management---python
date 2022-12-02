from flask import *


from admin import admin
from public import public
from donor import donor
from volunteer import volunteer
from recipient import recipient 

app=Flask(__name__)
app.secret_key="hello"

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(donor,url_prefix='/donor')
app.register_blueprint(volunteer,url_prefix='/volunteer')


app.register_blueprint(recipient,url_prefix='/recipient')

app.run(debug=True,port=5042)