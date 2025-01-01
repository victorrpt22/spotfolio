from flask import Flask, render_template, jsonify
from .blog import BlogModule


class SpotFolio:
    def __init__(self, title: str = 'My SpotFolio', description: str = 'My personal portfolio'):
        self.title = title
        self.description = description
        self.app = Flask(__name__)
        self.blog = BlogModule()
        self._register_routes()

    def _register_routes(self):
        @self.app.route('/')
        def home():
            return render_template('base.html', title=self.title, description=self.description)

        @self.app.route('/blog', methods=['GET'])
        def list_posts():
            return render_template('blog.html', posts=self.blog.list_posts())

        @self.app.route('/blog/<int:post_id>', methods=['GET'])
        def view_post(post_id: int):
            return render_template("post.html", post=self.blog.view_post(post_id))

    def run(self, host: str = "127.0.0.1", port: int = 5000):
        self.app.run(host=host, port=port)
