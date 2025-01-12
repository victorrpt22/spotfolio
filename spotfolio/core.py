from flask import Flask, render_template
from . import BaseModule
from typing import Dict, List, Any


class SpotFolio:
    def __init__(self, title: str = 'My SpotFolio', description: str = 'My personal portfolio', config: Dict[str, bool] | None = None):
        self.app = Flask(__name__)
        self.modules: Dict[str, BaseModule] = {}
        self.sections: List[Dict[str, Any]] = []
        self.config = config or {}
        self.title = title
        self.description = description
        self._register_routes()

    def register_module(self, name: str, module: BaseModule):
        module.initialize()
        module.register_routes(self.app)
        self.modules[name] = module
        if hasattr(module, 'get_section_metadata'):
            self.sections.append(module.get_section_metadata())

    def _register_routes(self):
        @self.app.route('/')
        def home():  # type: ignore
            return render_template('base.html', title=self.title, description=self.description, sections=self.sections)

    def get_module(self, name: str) -> BaseModule | None:
        return self.modules.get(name)

    def run(self, host: str = "127.0.0.1", port: int = 5000):
        self.app.run(host=host, port=port)
