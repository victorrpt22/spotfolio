from typing import List, Dict
from flask import Flask


class ResumeModule:
    name: str
    email: str
    phone: str
    summary: str
    skills: List[str]
    experience: List[Dict[str, str]]
    education: List[Dict[str, str]]
    projects: List[Dict[str, str]]
    certifications: List[Dict[str, str]]
    languages: List[Dict[str, str]]
    interests: List[str]

    def register_routes(self, app: Flask):
        @app.route('/resume', methods=['GET'])
        def view_resume():  # type: ignore
            return self.model_dump()
