import logging
from typing import Any, List, Dict
from . import BaseModule
from flask import render_template
from uuid import uuid4

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Post:
    def __init__(self, title: str, content: str, id: str):
        self.id = id
        self.title = title
        self.content = content

    def to_dict(self) -> Dict[str, Any]:
        return {'id': self.id, 'title': self.title, 'content': self.content}


class BlogModule(BaseModule):
    def __init__(self):
        self.posts: List[Post] = []  # type: ignore

    def initialize(self):
        print("Initializing BlogModule")

    def register_routes(self, app: Any):
        @app.route('/blog', methods=['GET'])
        def list_posts():  # type: ignore
            posts = self.list_posts()
            return render_template('blog/list.html', posts=posts)

        @app.route('/blog/<string:post_id>', methods=['GET'])
        def view_post(post_id: str):  # type: ignore
            post = self.view_post(post_id)
            if isinstance(post, tuple):
                return post
            return render_template('blog/view.html', post=post)

    def add_post(self, title: str, content: str, id: str | None = None,):
        post_id = id if id else str(uuid4())
        self.posts.append(Post(title, content, post_id))

    def list_posts(self):
        return self.posts

    def view_post(self, post_id: str):
        post = next(
            (post for post in self.posts if post.id == post_id), None)
        if post is None:
            logger.error(f"Post with id {post_id} not found")
            return "Post not found", 404
        return post
