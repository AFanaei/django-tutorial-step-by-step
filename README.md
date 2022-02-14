## Optimize postgresql performance in django
This is the slide deck and project of my [ir pycon](https://ir.pycon.org/) presentation.

The project is a step by step implementation of [django tutorial](https://github.com/consideratecode/django-tutorial-step-by-step)
in addition to original project following tasks are done:
- migrate project to django 4
- generate docker file and docker compose
- add fixture to load data for each senario

The slides are located in slides folder and are created using [vscode-revealjs](https://marketplace.visualstudio.com/items?itemName=evilz.vscode-reveal) extention.

#### How to execute

you can run the project using docker-compose:
```
docker-compose -f "mysite\docker-compose.yml" up -d --build
```
