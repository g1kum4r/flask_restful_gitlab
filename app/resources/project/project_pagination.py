from flask_restful import Resource
import requests
from app.env import GITLAB_BASE_URL
from .utils import parser


class Projects(Resource):
    def get(self):
        response = requests.get(f"{GITLAB_BASE_URL}projects", params=parser.parse_args())
        return response.json(), 200, {
            'page': response.headers.get('x-page'),
            'per-page': response.headers.get('x-per-page'),
            'next-page': response.headers.get('x-next-page'),
            'prev-page': response.headers.get('x-prev-page'),
            'total': response.headers.get('x-total'),
            'total-pages': response.headers.get('x-total-pages'),
        }