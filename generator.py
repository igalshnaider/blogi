import os
from flask import Flask , render_template , url_for, abort
from werkzeug import cached_property
import markdown
import yaml

POSTS_FILE_EXTENTION = '.md'
	
			
class Post(object):
	def __init__(self, path):
		self.path = path
		self._initialize_metadata()
		
		
	@cached_property
	def html(self):
		with open(self.path,'r') as fin:
			 content = fin.read().split('\n\n',1)[1].strip()
		return markdown.markdown(content)

	def _initialize_metadata(self):
		content = ''
		with open(self.path,'r') as fin:
			for line in fin:
				if not line.strip():
				 	break
				content += line
		self.__dict__.update(yaml.load(content))

	

app = Flask(__name__)


@app.route('/')
def index():
	return 'Hello world!'

@app.route('/blogi/<path:path>')
def post(path):
	# import ipdb
	# raise
	path = os.path.join('posts', path + POSTS_FILE_EXTENTION)
	# ipdb.set_trace()
	post = Post(path)
	return render_template('post.html', post = post)


if __name__ == '__main__':
	app.run(port=8000, debug=True)
