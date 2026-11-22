# Study Planner

A web application that helps university students organize their study work. A student groups work into **subjects** (courses) and tracks the **tasks** of each subject with a due date and a status.

Built with Django and PostgreSQL as a Software Engineering course project.

## Project Documentation

| Deliverable | Link |
|---|---|
| Requirements (roles, user stories, acceptance criteria, NFRs, MoSCoW, MVP) | [docs/requirements.md](docs/requirements.md) |
| Backlog (one GitHub Issue per user story and NFR) | [Issues](../../issues) |
| Project board (Backlog, To Do, In Progress, Review, Done) | [Study Planner Board](https://github.com/users/Omar-Mokhles/projects/1) |
| Designs: Use Case, Class, Sequence and State diagrams (PlantUML) | [docs/design](docs/design/README.md) |
| UI/UX: wireframes and mockups | [Figma](https://www.figma.com/design/suiieemkPxgXjim7SlsBFo/Untitled?node-id=0-1&t=6B4VYXZhDQUdVbJI-1) |
| Concept, target audience and tech stack | [CONCEPT_AND_TOOLS.md](CONCEPT_AND_TOOLS.md) |

## Tech Stack

Python, Django, PostgreSQL, HTML/CSS (Django templates), Git and GitHub, PlantUML, Figma. Details in [CONCEPT_AND_TOOLS.md](CONCEPT_AND_TOOLS.md).

## Run Locally

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The database settings and secret key are read from a local `.env` file, which is not committed to the repository.