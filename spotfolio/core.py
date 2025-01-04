from flask import Flask, render_template
from . import BlogModule, ResumeModule
from typing import List, Dict, Any


class SpotFolio:
    def __init__(self, title: str = 'My SpotFolio', description: str = 'My personal portfolio', config: Dict[str, bool] = None):
        self.modules: List[object] = []
        self.config = config or {}
        self.title = title
        self.description = description
        self.app = Flask(__name__)
        self._register_routes()
        self._load_modules()

    def _load_modules(self):
        available_modules: Dict[str, Any] = {
            'blog': BlogModule,
            'resume': ResumeModule,
        }
        for module_name, enabled in self.config.items():
            if enabled and module_name in available_modules:
                module = available_modules[module_name]()
                self.register_module(module)

    def _register_routes(self):
        @self.app.route('/')
        def home():
            return render_template('base.html', title=self.title, description=self.description)

    def run(self, host: str = "127.0.0.1", port: int = 5000):
        for module in self.modules:
            module.register_routes(self.app)
        self.app.run(host=host, port=port)
