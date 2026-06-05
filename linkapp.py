from flask import Flask, render_template, request, redirect, send_from_directory, url_for, g, make_response
from flask_sqlalchemy import SQLAlchemy
import datetime
from hashids import Hashids
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms import csrf
import appconfig
import os
from flask_bcrypt import Bcrypt
from flask import jsonify
from flask import abort

### APPLICATIO  SETUP ###
application = Flask(__name__) 
bcrypt = Bcrypt(application)

from hashids import Hashids

hashids = Hashids(salt="this is platform")
 
application.config.from_object('appconfig.ProductionConfig')
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI'] if application.config['SQLALCHEMY_DATABASE_URI'] == '' else application.config['SQLALCHEMY_DATABASE_URI']

application.config['DOMAIN'] = os.environ['DOMAIN'] if application.config['DOMAIN'] == '' else application.config['DOMAIN']


#dbo = db.DB()
db = SQLAlchemy(application, session_options={"autoflush": False})

csrf.init_app(application)

# hashids
hashids = Hashids(salt="this is zap.buzz")

login_manager = LoginManager()
login_manager.init_app(application)

DOMAIN = os.environ['DOMAIN'] if appconfig.Domain.DOMAIN == '' else appconfig.Domain.DOMAIN
TABTEXT = os.environ['TABTEXT'] if os.environ['TABTEXT'] else ''
TARGET_DOMAIN = os.environ['TARGET_DOMAIN'] if appconfig.Domain.TARGET_DOMAIN == '' else appconfig.Domain.TARGET_DOMAIN
ZAP_DOMAIN = os.environ['ZAP_DOMAIN'] if appconfig.Domain.ZAP_DOMAIN == '' else appconfig.Domain.ZAP_DOMAIN
### ### ### ### ### ### ###

@application.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@application.route('/get_link', methods=['POST'])
@login_required
@csrf.exempt
def get_link():
    from lib import link
    data = link.Link.get_item(request.form.get('id'))
    return jsonify({'data': data})

@application.route('/delete_link', methods=['POST'])
@login_required
@csrf.exempt
def delete_link():
    from lib import link
    try:
        code = request.form.get('link_code')
        status = link.Link.delete_item(code)
        return jsonify({'data': status})
    except Exception as e:
        return jsonify({'data': str(e)})

@application.route('/save_link', methods=['POST'])
@login_required
@csrf.exempt
def save_link():
    try:
        from lib import link
        url = request.form.get('url')
        network = request.form.get('network')
        publisher = request.form.get('publisher')
        domain = request.form.get('domain')
        code = request.form.get('code', 0)
        status = link.Link.add_item(code, [domain, network, publisher, url])
        return jsonify({'data': status})
    except Exception as e:
        return jsonify({'data': str(e)})

@application.route('/sub/<code>', methods=['GET', 'POST'])
def system(code):
    from lib import link
    item = link.Link.get_item(code)
    if item == -1: # not found
        abort(404)
    referrer = request.referrer
    if not referrer and "adcharriot" not in item[2]:
       abort(404)
    return render_template('load.html', url=link.Link.get_item(code)[3])

@application.route('/load', methods=['POST', 'GET'])
@csrf.exempt
def load():
    if request.method == 'GET':
        abort(404)
    url = request.form.get('url')
    return redirect(url)


@login_manager.user_loader
def load_user(user_id):
    from lib import user
    return user.User.get(int(user_id))

@application.route('/dashboard', methods=['POST', 'GET']) #services
def dashboard():
    if request.method == 'GET' and not current_user.is_active:
        return render_template('dashboard_login.html', page='dashboard_login')
    else:
        if current_user.is_active:
            usero = current_user
        else:
            from lib import user
            usero = user.User.get_user(request.form['email'])
            if usero.check_user(request.form['password']):
                usero.auth_user()
            else:
                return render_template('dashboard_login.html', page='dashboard_login', error="Wrong username or password!")

        login_user(usero)
        from lib import link
        all_data = link.Link.get_all_data()
        return render_template('dashboard.html', page='dashboard', links=all_data, 
                    fields=['Code', 'URL', 'Network', 'Publisher', 'Domain'], count=len(all_data))
   

@application.route('/test', methods=['GET'])
def test():
    return render_template('test.html')

#$2b$12$WF/jLY3gWHFsFdBMrUcytuPaE3E90ClPjxpe0vgAICRJVWYBmJT4S
@application.route("/dashboardLogin", methods=['POST'])
def dashboardLogin():
    from lib import user
    usero = user.User.get_user(request.form['email'])
    if usero:
        if usero.check_user(request.form['password']):
            usero.auth_user()
        else:
            return render_template('dashboard_login.html', page='dashboard_login', error="Wrong username or password!", domain=TABTEXT)
    else:
        return render_template('dashboard_login.html', page='dashboard_login', error="Wrong username or password!", domain=TABTEXT)

    login_user(usero)

    return redirect(url_for('dashboard'))

@application.route("/dashboardLogout")
@login_required
def dashboardLogout():
    logout_user()
    return redirect(url_for('dashboard'))

@application.before_request
def before_request():
    g.user = current_user

@application.route('/robots.txt')
@application.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(application.static_folder, request.path[1:])
        
if __name__ == "__main__":
    application.run()
