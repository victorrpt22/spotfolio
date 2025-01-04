from typing import List, Dict, Any
import logging
from flask import Flask
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BlogModule:
    def __init__(self):
        self.posts = []

    def register_routes(self, app: Flask):
        @app.route('/blog', methods=['GET'])
        def list_posts():  # type: ignore
            return self.list_posts()

        @app.route('/blog/<int:post_id>', methods=['GET'])
        def view_post(post_id: int):
            return self.view_post(post_id)

    def add_post(self, title: str, content: str):
        post_id = len(self.posts) + 1
        self.posts.append(
            {'id': post_id, 'title': title, 'content': content, })

    def list_posts(self):
        return self.posts

    def view_post(self, post_id: int):
        if not isinstance(post_id, int):
            logger.error(f"Post id {post_id} is not an integer")
            return "Post id must be an integer", 400
        post = next(
            (post for post in self.posts if post['id'] == post_id), None)
        if post is None:
            logger.error(f"Post with id {post_id} not found")
            return "Post not found", 404
        return post
