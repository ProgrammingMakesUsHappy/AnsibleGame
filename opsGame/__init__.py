# -*- endcoding=UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_babelex import Babel

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
babel = Babel(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from opsGame import views, models, dataShowViews
