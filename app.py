import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)
from auctiongrabber import *

@app.route('/')
def index():
   print('Request for index page received')
   

   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()



@app.route('/call', methods=['POST'])
def call():
    content = Auction_housse(["Skin", "Dye", "[Lvl","Mixin","Drill Engine","'Burning Kuudra Core","Plasma","Coffin","◆ Smokey Rune I","Surfboard","Ruby-polished Drill Engine"],1000000,54276615)
    return render_template('index.html', content = content)




