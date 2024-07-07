# Django Rest Framework and Vue.js Todo App

## Run Project

    - cd todo-drf-vue
    - docker-compose up --build

# Clean Project

    - docker-compose down
    - docker-compose down -v // Cuidado, elimina volumenes y contenedores, preserva las imagenes
    - docker volume prune

## DOCS

    https://drive.google.com/drive/folders/1Z6hnGqmVlOd7GviNV33nso5r9gtGDEdU?usp=sharing

## API

    * Tasks
    - GET /api/tasks/
    - GET /api/tasks/<id>
    - GET /api/tasks/?priority=<High/Low>
    - GET /api/tasks/?completed=<True/False>
    
    * Users
    - GET /api/users/
    - GET /api/users/<id>/

    * Assigns
    - GET /api/assigns/
    - GET /api/assigns/<id>
    - GET /api/assigns/?user=<id>
    - GET /api/assigns/?task=<id>

## CONVENTIONAL COMMITS

        - *feat*: A new feature

        - *fix*: A bug fix

        - *docs*: Documentation only changes

        - *config*: Changes to configuration files

        - *refactor*: A code change that neither fixes a bug nor adds a feature
        
        - *style*: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
        
        - *chore*: Changes to the build process or auxiliary tools and libraries such as documentation generation
