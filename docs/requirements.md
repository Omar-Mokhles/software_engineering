# Requirements: Study Planner

> **GitHub Project board:** <https://github.com/users/Omar-Mokhles/projects/1>  
> **Backlog:** GitHub Issues of this repository (one Issue per user story and per NFR)

## 0. Project context and stakeholders

Study Planner is a web application that helps university students organize their study work. A student groups work into **subjects** (courses) and tracks the **tasks** of each subject with a due date and a status.

| Stakeholder | Interest | Influence |
|---|---|---|
| Students (end users) | Plan and track their own study work | Decide which features are useful |
| Administrator | Keep data and accounts healthy | Can change and delete any data |
| Course instructor / TA | Evaluate the engineering process and deliverables | Grades the project |
| Development team | Deliver a working MVP in the available weeks | Decide scope and priorities |

## 1. Roles

| Role | Description |
|---|---|
| Visitor | A person who is not logged in. Can only reach the sign-up and login pages. |
| Student | A registered user who owns subjects and tasks and manages their own study plan. |
| Administrator | A staff/superuser who manages all data through the Django admin panel. |

## 2. User stories

Priorities follow MoSCoW. Every story was checked against INVEST.

| ID | Story | Priority | Area |
|---|---|---|---|
| US-01 | As a visitor, I want to create an account with a username and password so that I can have my own private study planner. | Must | auth |
| US-02 | As a visitor, I want to log in with my username and password so that I can access my subjects and tasks. | Must | auth |
| US-03 | As a student, I want to log out of my account so that nobody else using my device can see my data. | Must | auth |
| US-04 | As a student, I want to add a subject with a name, description and color so that I can organize my study material by course. | Must | subjects |
| US-05 | As a student, I want to view the list of my subjects so that I can see all my courses at a glance. | Must | subjects |
| US-06 | As a student, I want to edit a subject's name, description or color so that I can fix mistakes or update its details. | Should | subjects |
| US-07 | As a student, I want to delete a subject after a confirmation page so that I can remove courses I am no longer taking without deleting them by accident. | Should | subjects |
| US-08 | As a student, I want to add a task to one of my subjects with a title, description and due date so that I can track everything I have to do. | Must | tasks |
| US-09 | As a student, I want to view all my tasks sorted by due date so that I can see what is most urgent. | Must | tasks |
| US-10 | As a student, I want to change a task's status (Pending, In Progress, Completed, Cancelled) so that I can track my progress. | Must | tasks |
| US-11 | As a student, I want to edit a task's details (title, description, due date, subject) so that I can correct mistakes or reschedule work. | Should | tasks |
| US-12 | As a student, I want to delete a task after a confirmation page so that my task list stays clean. | Should | tasks |
| US-13 | As a student, I want to see a dashboard with my subjects and my next 5 tasks by due date so that I know what to work on next as soon as I log in. | Should | dashboard |
| US-14 | As a student, I want to open a subject's page and see only the tasks of that subject so that I can focus on one course at a time. | Should | subjects |
| US-15 | As a student, I want to be sure that my subjects and tasks are visible only to me so that my study information stays private. | Must | security |
| US-16 | As a student, I want to filter my tasks by status so that I can see only what is still pending or in progress. | Could | tasks |
| US-17 | As a student, I want to see overdue tasks highlighted so that I notice immediately what I have missed. | Could | tasks |
| US-18 | As an administrator, I want to manage users, subjects and tasks from the admin panel so that I can fix data problems and support students. | Should | admin |
| US-19 | As an administrator, I want to search and filter tasks by status and due date in the admin panel so that I can investigate problems quickly. | Could | admin |

## 3. Acceptance criteria (Gherkin)

Written for the five most important stories, each with at least one failure scenario.

### US-01 - Create an account with a username and password

```gherkin
Feature: Create an account with a username and password

  Scenario: Visitor registers with valid data
    Given a visitor on the sign-up page
    And the username "omar" is not taken
    When the visitor submits the username "omar" and the password "Str0ng!Pass2026" twice
    Then an account is created
    And the visitor is logged in and redirected to the dashboard

  Scenario: Username already taken
    Given a user named "omar" already exists
    When a visitor tries to register with the username "omar"
    Then no new account is created
    And the message "A user with that username already exists." is shown

  Scenario: Password too common
    Given a visitor on the sign-up page
    When the visitor submits the password "12345678"
    Then no account is created
    And the message "This password is too common." is shown
```

### US-02 - Log in with my username and password

```gherkin
Feature: Log in with my username and password

  Scenario: Successful login
    Given a registered student "omar" with the password "Str0ng!Pass2026"
    When the student submits these credentials on the login page
    Then the student is redirected to the dashboard

  Scenario: Wrong password
    Given a registered student "omar"
    When the student submits the password "wrong-pass"
    Then the student stays on the login page
    And the message "Please enter a correct username and password." is shown
```

### US-08 - Add a task to one of my subjects with a title, description and due date

```gherkin
Feature: Add a task to one of my subjects with a title, description and due date

  Scenario: Student adds a valid task
    Given a logged-in student who owns the subject "Databases"
    When the student adds the task "Finish ER diagram" with the due date 2026-12-01 under "Databases"
    Then the task is saved with the status "Pending"
    And it appears in the student's task list

  Scenario: Missing title
    Given a logged-in student on the add-task form
    When the student submits the form with an empty title
    Then the task is not created
    And the message "This field is required." is shown

  Scenario: Invalid due date
    Given a logged-in student on the add-task form
    When the student enters the due date "2026-13-40"
    Then the task is not created
    And a date validation error is shown
```

### US-10 - Change a task's status (Pending, In Progress, Completed, Cancelled)

```gherkin
Feature: Change a task's status (Pending, In Progress, Completed, Cancelled)

  Scenario: Mark a task as completed
    Given a task "Finish ER diagram" with the status "Pending"
    When the student edits the task and sets the status to "Completed"
    Then the task is saved with the status "Completed"
    And the task list shows "Completed" for that task

  Scenario: Invalid status
    Given a task "Finish ER diagram"
    When a request sets the status to "archived"
    Then the change is rejected
    And the message "Select a valid choice. archived is not one of the available choices." is shown
    And the task keeps its old status
```

### US-15 - Be sure that my subjects and tasks are visible only to me

```gherkin
Feature: Be sure that my subjects and tasks are visible only to me

  Scenario: Another student's subject is not accessible
    Given the students "omar" and "sara"
    And "sara" owns the subject "Networks" with id 7
    When "omar" is logged in and requests /subjects/7/
    Then the system responds with 404 Not Found
    And no data of that subject is shown

  Scenario: Visitor is redirected to login
    Given a visitor who is not logged in
    When the visitor requests /tasks/
    Then the visitor is redirected to the login page

  Scenario: Task list shows only own tasks
    Given "omar" has 3 tasks and "sara" has 2 tasks
    When "omar" opens the task list
    Then exactly 3 tasks are shown
```

## 4. Non-functional requirements

| ID | Type | Requirement |
|---|---|---|
| NFR-01 | Performance | The task list and the dashboard return their response in under 2 seconds for a student with 500 tasks while 50 users are connected at the same time. |
| NFR-02 | Security | Passwords are stored only as salted hashes using Django's password hasher (PBKDF2-SHA256 or stronger); a database inspection must show no plain-text password. |
| NFR-03 | Security | 100% of subject and task pages require login (a visitor gets a redirect to the login page), and a request for another user's object returns 404; verified by automated tests. |
| NFR-04 | Security | No secret (SECRET_KEY, database password) is committed to the repository; all of them are read from environment variables, verified by scanning the repo history with zero findings. |
| NFR-05 | Usability | At least 90% of 5 test users create an account, a first subject and a first task in under 3 minutes without any instructions. |
| NFR-06 | Usability | All pages stay usable (no horizontal scrolling, no overlapping elements) at screen widths from 360 px to 1920 px in the latest versions of Chrome, Firefox and Edge. |
| NFR-07 | Availability | The deployed application is available at least 99% of the time during the semester demo period, measured weekly. |
| NFR-08 | Maintainability | Automated tests cover at least 70% of the code in the models, forms and views, and all tests pass before each merge to main. |

## 5. MoSCoW summary and MVP scope

- **Must:** US-01, US-02, US-03, US-04, US-05, US-08, US-09, US-10, US-15
- **Should:** US-06, US-07, US-11, US-12, US-13, US-14, US-18
- **Could:** US-16, US-17, US-19
- **Won't (this release):**
  - Native mobile application
  - Two-way sync with Google Calendar or other calendars
  - Sharing subjects or tasks with classmates (collaboration)
  - File attachments on tasks
  - Push or e-mail reminders (may return as a Could story in a later release)

### MVP scope

**MVP = all Must stories:** US-01, US-02, US-03, US-04, US-05, US-08, US-09, US-10, US-15.

**Statement:** Students can register, log in, create subjects, add tasks with due dates, see all their tasks sorted by due date, update task status, and log out, with every student's data fully private.

**Reason:** These stories form the smallest end-to-end flow that gives a student real value (plan and track work) and is realistic for the team's time. Edit/delete, the dashboard, filtering, highlighting and admin conveniences stay in the backlog.