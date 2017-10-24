# -*- coding=utf-8 -*-
import os
import pymysql

from flask import Flask,request,session,redirect,\
    url_for,abort,render_template,flash,jsonify
from flask_bootstrap import Bootstrap
from sqlalchemy import create_engine
#ORM模型建议使用下面的模块
#from flask_sqlalchemy import SQLAlchemy

#创建引擎,不用关心db的连接专注于业务的编写
engine = create_engine("mysql+pymysql://root@localhost:3306/pystudy",max_overflow=5)
#执行插入操作
#engine.execute("insert into entries (title,text) values ('four','this is the fourth entry')")
#执行查询操作
#result = engine.execute('select * from entries')
#获取查询得到的数据
#res = result.fetchall()
#执行删除操作
#res = engine.execute("delete from entries where id=5")
#print res

app = Flask(__name__)
#使用ORM模型需要配置连接参数
#app.config['SQLALCHEMY_DATABASE_URI']=\
#	'mysql://root@localhost:3306/pystudy'
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
#使用ORM模型需要创建一个db实例，表示程序所使用的数据库，同时还获得了Flask-SQLAlchemy的所有功能
#db = SQLALchemy(app)
bootstrap = Bootstrap(app)
app.secret_key=os.urandom(24)
app.config['USERNAME']='admin'
app.config['PASSWORD']='123456'
@app.route('/')
def show_entries():
	result = engine.execute('select * from entries')
	entries = result.fetchall()
	return render_template('show_entries.html',entries=entries)

@app.route('/add',methods=['POST'])
def add_entries():
	if 'logged_in' not in session:
		return redirect(url_for('login'))

	engine.execute('insert into entries (title,text) values (%s,%s)',(request.form['title'],request.form['text']))

	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method=='POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:	
		        session['logged_in']='logged_in'
			flash('You have logged in!')
			return redirect(url_for('show_entries'))
	
	return render_template('login_in.html',error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash('You are logged out')
	return redirect(url_for('show_entries'))


@app.route('/jsontest',methods=['GET','POST'])
def jsontest():
    data=request.get_json()
    if data['bid'] == 'bid':
   	 return jsonify({'code':1,'msg':'success'})
    else:
	 return jsonify({'code':2,'msg':'failure'})
#数据库实例db为模型提供了一个基类以及一系列辅助类和辅助函数，用于定义模型结构
#class Entry(db.Model):
#	__tablename__ = 'entries'
#	id = db.Column(db.Integer,primary_key=True)
#	title = db.Column(db.String(32))

#	def __repr__(self):
#		return '<Entry %r>' % self.id

#class User(db.Model):
#	__tablename__ = 'user'
#	id = db.Column(db.Integer,primary_key=True)
#	name = db.Column(db.String(32))
#	gender = db.Column(db.Integer)
#	mobile = db.Column(db.Integer)

#	def __repr__(self):
#		return '<User %r>' % self.id
