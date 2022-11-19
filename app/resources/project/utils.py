from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument("page", location="args")
parser.add_argument("per_page", location="args")