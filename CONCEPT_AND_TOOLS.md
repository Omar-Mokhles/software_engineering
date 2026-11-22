# Concept and Tools: Study Planner

## Concept

### Problem
- University students handle many courses at once, each with its own assignments, labs and exams.
- Deadlines are scattered across notes, chat messages and memory, so tasks are forgotten or noticed too late.
- General-purpose to-do apps do not group work by course, so it is hard to see what is pending in each subject.
- Many planners are too complex (calendars, reminders, collaboration) for a student who only needs a clear list.

### Solution
- A simple web application where each student has a private account.
- The student creates **subjects** (courses) with a name, description and color.
- Inside each subject the student adds **tasks** with a title, description and due date.
- Each task has a status (Pending, In Progress, Completed, Cancelled) so progress is always visible.
- A dashboard shows the subjects and the next tasks by due date, so the student knows what to do next.
- Every student sees only their own data; an administrator can manage all data from the admin panel.

### Target audience
- **Primary:** university students who want a lightweight way to organize their study work.
- **Secondary:** administrators who maintain accounts and data.

### Scope (MVP)
- Sign up, log in and log out.
- Create and view subjects.
- Add tasks, view them sorted by due date, and update their status.
- Private data per student.
- Full list: see [docs/requirements.md](docs/requirements.md).

## Tech Stack

| Area | Tool | Use in the project |
|---|---|---|
| Language | Python 3 | Application code |
| Web framework | Django 6.1 | Models, views, forms, URL routing, templates, authentication, admin panel |
| Database | PostgreSQL | Stores users, subjects and tasks (via `psycopg`) |
| Configuration | python-dotenv | Loads secrets (secret key, database credentials) from a `.env` file that is not committed |
| Front end | HTML and CSS in Django templates | User interface rendered on the server |
| Testing | Django test framework | Automated tests for models, forms and views |

## Development Tools

| Area | Tool | Use in the project |
|---|---|---|
| Version control | Git and GitHub | Branches, commits and reviewed pull requests |
| Project management | GitHub Issues and GitHub Projects | Backlog of user stories and NFRs, and the Kanban board |
| Requirements | Markdown | [docs/requirements.md](docs/requirements.md) |
| Modelling | PlantUML | Use case, class, sequence and state diagrams in [docs/design](docs/design) |
| UI/UX design | Figma | Wireframes and mockups (link in the project README) |
| Editor | Visual Studio Code | Development and Markdown preview |
