from flask_restful import Resource
import requests
from app.env import GITLAB_BASE_URL


class Project(Resource):
    def get(self, project_id: int):
        return requests.get(f"{GITLAB_BASE_URL}projects/{project_id}").json()
