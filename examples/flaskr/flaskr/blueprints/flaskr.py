# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from sqlite3 import dbapi2 as sqlite3

from cache.redisutils import RedisUtils
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app
import MySQLdb

# create our blueprint :)
bp = Blueprint('flaskr', __name__)

redis_utils = RedisUtils()

username = ''


def connect_db2():
    """Connects to the specific database."""
    rv = sqlite3.connect(current_app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def connect_db():
    """Connects to the specific database."""
    db = MySQLdb.connect(user="root", db="dev")
    return db


def init_db():
    """Initializes the database."""
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def get_db2():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'mysql_cursor'):
        g.sqlite_cursor = connect_db()
    return g.sqlite_cursor


@bp.route('/')
def show_entries():
    #return "Hello World !!~~"

    cur = get_db().cursor()
    cur.execute('select title, text, user from entries order by id desc')
    entries = cur.fetchall()
    rows = [item for item in entries]
    return render_template('show_entries.html', entries=rows)


@bp.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.cursor().execute("""insert into entries (title, text, user) values (%s, %s, %s)""",
                   [request.form['title'], request.form['text'], session['username']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('flaskr.show_entries'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not redis_utils.is_user_exist(request.form['username']):
            error = 'user does not exist'
        else:
            if request.form['password'] == redis_utils.get_user(request.form['username']):
                session['logged_in'] = True
                session['username'] = request.form['username']
                flash('You were logged in')
                return redirect(url_for('flaskr.show_entries'))
            else:
                error = 'username & password does not match'

        if request.form['username'] != current_app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != current_app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            session['username'] = request.form['username']
            flash('You were logged in')
            return redirect(url_for('flaskr.show_entries'))
    return render_template('login.html', error=error)


@bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('flaskr.show_entries'))
