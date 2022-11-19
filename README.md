# Gitlab APIs
flask restful app

## Setup
open cmd in root folder of this project and run the following command to install dependencies

`pip install -r requirements.txt`


## Run
2 methods to run this project, either use flask run, or execute the run.py file
open cmd in root folder of this project and run either one of the following commands
1. `flask run`
2. `py run.py`

## API
- Projects Pagination
  
  http://localhost:5000/projects
- Get Project by Id

  http://localhost:5000/projects/<project_id>
- Get Project Pipelines by Project Id

  http://localhost:5000/projects/<project_id>/pipelines