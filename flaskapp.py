from flask import Flask, render_template, flash, redirect, url_for, session, logging
from mapstate import MapState
from wtforms import Form, validators
from wtforms.fields.html5 import IntegerRangeField

app = Flask(__name__)
ms = MapState('EG.ELC.ACCS.ZS')
ms.set_date('2000')
@app.route("/")
def index():
    return render_template('index.html', ms=ms)



