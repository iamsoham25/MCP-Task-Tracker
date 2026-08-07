# Task Tracker using Model Context Protocol (MCP)

A Python-based **Task Tracker MCP Server** built using the **Model Context Protocol (MCP)**.

The project demonstrates how an MCP server can be used to manage daily work tasks through MCP Tools while storing task information permanently in a **SQLite database**.

The server is built using **FastMCP** and can be tested interactively using the **MCP Inspector**.

---

## Project Overview

The Task Tracker is designed to manage and track daily work activities through an MCP Server.

Users can add work logs, retrieve existing tasks, update task status, delete records, and generate work summaries using MCP Tools.

All task information entered through the MCP interface is stored in:

```text
intern_tracker.db
```

The project currently demonstrates three important components:

```text
MCP Server
   |
   +-- MCP Tools
   |
   +-- MCP Prompts
   |
   +-- SQLite Database
```

---

## Features

The current Task Tracker supports:

- Add Daily Work Logs
- List stored Daily Work Logs
- Filter logs based on status
- Update task status to Done
- Delete Daily Work Logs
- Generate work summary
- Automatically calculate the day from the work date
- Automatically assign `To Do` status to new tasks
- Store all task information permanently in SQLite
- Generate structured Daily Work Log instructions using MCP Prompts
- Test MCP Tools and Prompts through MCP Inspector

---

## Technologies Used

- Python
- Model Context Protocol (MCP)
- FastMCP
- SQLite
- MCP Inspector
- Node.js / NPX
- Visual Studio Code

---

# Project Architecture

```text
                     User / MCP Client
                            |
                            v
                     MCP Inspector
                            |
                            v
                    FastMCP Server
                      (server.py)
                            |
             +--------------+--------------+
             |                             |
             v                             v
        MCP Tools                     MCP Prompts
             |                             |
             |                    Structured Prompt
             |                       Generation
             |
             v
        database.py
             |
             v
          SQLite
             |
             v
     intern_tracker.db
             |
             v
     daily_work_log table
```

---

# Project Structure

```text
MCP_Server/
│
├── server.py
├── database.py
├── intern_tracker.db
├── requirements.txt
├── README.md
│
├── venv/
│
└── __pycache__/
```

### `server.py`

Contains the main FastMCP server.

It includes:

- MCP Tools
- MCP Prompts
- Database operations through `database.py`
- MCP server initialization

### `database.py`

Handles SQLite database functionality including:

- Database connection
- Database initialization
- Table creation
- Database reset functionality

### `intern_tracker.db`

SQLite database used to permanently store Daily Work Log records.

### `requirements.txt`

Contains the Python dependencies required to run the project.

### `README.md`

Contains project documentation, setup instructions, architecture, and usage information.

---

# SQLite Database

The project uses SQLite for persistent task storage.

The database file is:

```text
intern_tracker.db
```

The main table is:

```text
daily_work_log
```

## Daily Work Log Structure

| Field | Description |
|---|---|
| `id` | Unique ID for each work log |
| `work_date` | Date of the task |
| `day` | Day automatically calculated from the date |
| `task_description` | Description of the work performed |
| `deliverables` | Output or deliverables produced |
| `blockers` | Blockers or dependencies |
| `hours_spent` | Total working hours |
| `status` | Current task status |
| `notes` | Additional comments |
| `created_at` | Record creation timestamp |
| `updated_at` | Last update timestamp |

---

# Task Status Workflow

When a new Daily Work Log is created using:

```text
add_daily_work_log
```

the task status is automatically set to:

```text
To Do
```

The status does not need to be entered manually while creating a task.

The task remains:

```text
To Do
```

until the `update_work_status` tool is executed.

After updating the work status, it becomes:

```text
Done
```

Therefore, the basic task lifecycle is:

```text
New Task
   |
   v
 To Do
   |
   | update_work_status
   v
 Done
```

---

# MCP Tools

The server currently provides five main MCP Tools.

## 1. `add_daily_work_log`

Creates a new Daily Work Log and stores it in SQLite.

### Inputs

- Work Date
- Task Description
- Deliverables
- Blockers
- Hours Spent
- Notes

Example:

```text
Work Date:
2026-08-05

Task Description:
Implemented SQLite database integration for the MCP Task Tracker.

Deliverables:
Successfully connected MCP tools with SQLite database storage.

Blockers:
N/A

Hours Spent:
8

Notes:
Database integration completed successfully.
```

The server automatically calculates:

```text
Day
```

and automatically assigns:

```text
Status: To Do
```

---

## 2. `list_daily_work_logs`

Retrieves Daily Work Logs stored inside `intern_tracker.db`.

The tool can return all records or optionally filter them based on status.

Examples:

```text
To Do
```

or:

```text
Done
```

This tool is useful for verifying that information entered through the MCP interface has been successfully stored in SQLite.

---

## 3. `update_work_status`

Updates an existing Daily Work Log to:

```text
Done
```

The tool requires:

```text
Log ID
```

Example:

```text
Log ID: 5
```

After execution:

```text
To Do
   |
   v
Done
```

The `updated_at` timestamp is also updated.

---

## 4. `delete_daily_work_log`

Deletes an existing Daily Work Log from the SQLite database.

The tool requires the:

```text
Log ID
```

Example:

```text
Log ID: 5
```

The corresponding record is permanently removed from the `daily_work_log` table.

---

## 5. `get_work_summary`

Generates an overall summary of the stored work logs.

The summary contains:

- Total Work Logs
- Completed Work Logs
- To Do Work Logs
- Total Hours Spent

Example output:

```json
{
    "total_work_logs": 6,
    "completed": 3,
    "todo": 3,
    "total_hours": 48
}
```

---

# MCP Prompts

The project also demonstrates MCP Prompt functionality.

Prompts are different from Tools.

```text
MCP Tool
   |
   +-- Performs an operation

MCP Prompt
   |
   +-- Provides structured instructions/context
```

For example, a Tool can insert a task into SQLite, while a Prompt can help structure the information that should be used for creating a Daily Work Log.

---

## `create_daily_work_log_prompt`

This prompt accepts basic work information and generates structured instructions for preparing a professional Daily Work Log.

### Inputs

```text
Work Date
Work Done
```

Example:

```text
Work Date:
2026-08-05

Work Done:
Created the SQLite database and connected it with the MCP server.
```

The prompt structures the information around:

```text
Work Date
Day
Task Description
Deliverables
Blockers
Hours Spent
Status
Notes
```

New work is treated as:

```text
Status: To Do
```

> MCP Prompts generate structured instructions. They do not directly insert information into the SQLite database. Database operations are handled by MCP Tools.

---

# Setup Instructions

## 1. Open the Project

Open PowerShell or the VS Code terminal and navigate to the project directory:

```powershell
cd D:\MCP_Server
```

---

## 2. Activate the Virtual Environment

Run:

```powershell
.\venv\Scripts\Activate.ps1
```

The terminal should change to:

```text
(venv) PS D:\MCP_Server>
```

---

## PowerShell Execution Policy Issue

If PowerShell prevents the virtual environment from activating, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# Running the Project

## Step 1 - Check `server.py`

Before starting the MCP server, verify that `server.py` does not contain Python syntax errors.

Run:

```powershell
python -m py_compile server.py
```

If no output appears, the file compiled successfully.

---

## Step 2 - Verify MCP Server Loading

Run:

```powershell
python -c "from server import mcp; print('Server loaded successfully')"
```

Expected output:

```text
Server loaded successfully
```

---

## Step 3 - Initialize SQLite Database

Run:

```powershell
python database.py
```

Expected output:

```text
==================================================
Intern Tracker Database Initialized Successfully
==================================================
```

This creates:

```text
intern_tracker.db
```

and the:

```text
daily_work_log
```

table if they do not already exist.

Existing data is not removed during normal initialization.

---

## Step 4 - Start MCP Inspector

Run:

```powershell
npx @modelcontextprotocol/inspector python server.py
```

Expected output will be similar to:

```text
Starting MCP inspector...

MCP Inspector Web is up and running at:
http://localhost:6274?MCP_INSPECTOR_API_TOKEN=...

Sandbox (MCP Apps):
http://localhost:xxxxx/sandbox

Auth token: ...

Opening browser...
```

MCP Inspector should automatically open in the browser.

> The MCP Inspector authentication token and port numbers may change each time the Inspector is started.

---

# Quick Start

For normal development, the project can be started using:

```powershell
cd D:\MCP_Server

.\venv\Scripts\Activate.ps1

python -m py_compile server.py

python database.py

npx @modelcontextprotocol/inspector python server.py
```

Optional server verification:

```powershell
python -c "from server import mcp; print('Server loaded successfully')"
```

---

# Using MCP Inspector

After MCP Inspector opens, the server can be tested from the browser interface.

### Testing Tools

Open:

```text
Tools
```

Available tools include:

```text
add_daily_work_log
list_daily_work_logs
update_work_status
delete_daily_work_log
get_work_summary
```

To create a task:

```text
Tools
   |
   v
add_daily_work_log
   |
   v
Enter Task Information
   |
   v
Execute Tool
   |
   v
server.py
   |
   v
SQLite
   |
   v
intern_tracker.db
```

After adding a task, execute:

```text
list_daily_work_logs
```

to confirm that the record has been stored.

---

# Using MCP Prompts

Open:

```text
Prompts
```

Select:

```text
create_daily_work_log_prompt
```

Enter:

```text
Work Date
Work Done
```

The MCP server will return the structured prompt that can be used by an MCP-compatible AI client.

---

# Data Flow

The database workflow is:

```text
User
 |
 v
MCP Inspector
 |
 v
MCP Tool
 |
 v
server.py
 |
 v
get_connection()
 |
 v
database.py
 |
 v
     SQLite
        |
        v
intern_tracker.db
        |
        v
  daily_work_log
```

For example:

```text
User enters task information
          |
          v
 add_daily_work_log
          |
          v
      server.py
          |
          v
    SQL INSERT
          |
          v
 intern_tracker.db
          |
          v
 daily_work_log
```

---

# Viewing Stored Data

The `intern_tracker.db` file is a SQLite binary database file.

Therefore, it should not be opened as a normal text file.

Use a SQLite database viewer/editor extension in VS Code.

Open:

```text
intern_tracker.db
```

Then navigate to:

```text
TABLES
   |
   └── daily_work_log
```

The stored task records will appear in table format.

---

## Verify Data Using Terminal

The database can also be checked directly from PowerShell:

```powershell
python -c "import sqlite3; con=sqlite3.connect('intern_tracker.db'); rows=con.execute('SELECT * FROM daily_work_log').fetchall(); print(rows); con.close()"
```

This retrieves all records stored in:

```text
daily_work_log
```

---

# Current Project Status

The following functionality has been implemented:

- [x] Python MCP Server
- [x] FastMCP integration
- [x] SQLite database
- [x] `daily_work_log` table
- [x] Add Daily Work Log Tool
- [x] List Daily Work Logs Tool
- [x] Update Work Status Tool
- [x] Delete Daily Work Log Tool
- [x] Work Summary Tool
- [x] Automatic day calculation
- [x] Automatic `To Do` status
- [x] Update task status to `Done`
- [x] SQLite data persistence
- [x] MCP Inspector integration
- [x] MCP Tool testing
- [x] MCP Prompt implementation
- [x] Daily Work Log Prompt
- [x] End-to-end MCP and SQLite testing

---

# Future Development

The project can be extended with:

- MCP Resources
- Additional MCP Prompts
- Task editing functionality
- Input validation
- Duplicate date handling
- Search functionality
- Date-based filtering
- Weekly work summaries
- Monthly work summaries
- Improved reporting
- Export functionality
- Integration with an MCP-compatible AI client

A future architecture could look like:

```text
                 AI Client
                     |
                     v
                MCP Server
                     |
       +-------------+-------------+
       |             |             |
       v             v             v
     Tools         Prompts      Resources
       |                           |
       +-------------+-------------+
                     |
                     v
                   SQLite
                     |
                     v
              intern_tracker.db
```

---

# Developer

**Soham Thoke**

AI Engineer | GenAI | Prompt Engineering

---

# Project Purpose

The Task Tracker using MCP was developed to understand the practical implementation of the **Model Context Protocol** using Python.

The project demonstrates how an MCP Server can expose Tools and Prompts while integrating with a persistent SQLite database.

It provides hands-on experience with:

- MCP Server development
- FastMCP
- MCP Tools
- MCP Prompts
- SQLite integration
- CRUD operations
- Persistent task storage
- MCP Inspector
- Client-server interaction

The project serves as a practical implementation of an MCP-based task management system.