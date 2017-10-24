# -*- encoding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=\
	'mysql://root@localhost:3306/pystudy'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

class Entry(db.Model):
	__tablename__ = 'entries'
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(32))
	text = db.Column(db.Text)
	
	def __repr__(self):
		return '<Entry %r>' % self.id

if __name__=='__main__':
	print 'db test'
   	#根据模型创建表，没有找到根据数据表创建模型的扩展
 	#db.create_all()
   	
	#根据模型删除表
	#db.drop_all()
   	
	#添加一条记录到数据库中
	#entry = Entry(title='one',text='this is the first entry')
	
	#通过数据库会话管理系统db.session来对数据库做改动
	#db.session.add(entry)
	
	#最后提交才能完成添加
	#db.session.commit()
	
	#查询一行
	#entry = Entry.query.filter_by(id=1).first()
	#对查出的一行作出修改
	#entry.title='one new'
	#db.session.add(entry)
	#db.session.commit()

	#对查询一行作出删除
	#db.session.delete(entry)
	#db.session.commit()

	#根据模型创建数据库后，改了数据表以后还可以通过数据迁移扩展更新数据表
	#需要安装Flask-Migrate
