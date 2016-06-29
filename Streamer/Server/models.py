from peewee import *
from werkzeug.security import generate_password_hash, check_password_hash


db = SqliteDatabase('app.db')

class User(Model):
	username = CharField()
	password_hash = CharField()
	
	@property
	def password(self):
		raise AttributeError('password is not a readabl attribute')
		
	
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
		
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
		
		
	class Meta:
		database = db
		

db.create_tables([User],True)
