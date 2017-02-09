
from flask_script import Manager, Command
from flask import Flask

app = Flask(__name__)

manager = Manager(app)

# @manager.command
# def hello():
# 	print 'hello'


class Hello(Command):
	def run(self):
		return 'Hello'

manager.add_command('hello', Hello())

if __name__ == '__main__':
	manager.run()