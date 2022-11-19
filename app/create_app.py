from flask import Flask
from flask_restful import Api
from app.resources.project import Project, Projects, ProjectPipelines


def create_app(name=__name__):
    app = Flask(name)
    api = Api(app)

    api.add_resource(Projects, "/projects")
    api.add_resource(Project, "/projects/<project_id>")
    api.add_resource(ProjectPipelines, "/projects/<project_id>/pipelines")
    api.init_app(app)
    return app
