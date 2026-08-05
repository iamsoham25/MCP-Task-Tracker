# Intern Task Tracker - MCP Server

A Python-based **Model Context Protocol (MCP) Server** developed for tracking daily internship work.

The project uses **FastMCP** to expose task-management tools and **SQLite** to permanently store Daily Work Log information.

---

## Project Overview

The Intern Task Tracker allows internship work details to be managed through MCP tools.

The current system supports:

- Adding Daily Work Logs
- Listing Daily Work Logs
- Updating a work log status to Done
- Deleting Daily Work Logs
- Viewing an overall work summary
- Storing all work log information in SQLite
- Testing MCP tools through MCP Inspector

---

## Technologies Used

- Python
- Model Context Protocol (MCP)
- FastMCP
- SQLite
- MCP Inspector
- VS Code
- Node.js / NPX

---

## Project Structure

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

### server.py

Contains the MCP server and all MCP tools.

### database.py

Handles:

- SQLite connection
- Database initialization
- Table creation
- Database reset functionality

### intern_tracker.db

SQLite database used to permanently store Daily Work Log records.

### requirements.txt

Contains the Python dependencies required by the project.

---

# Daily Work Log Structure

The `daily_work_log` table stores the following information:

| Field | Description |
|---|---|
| id | Unique ID of the work log |
| work_date | Date of work |
| day | Day automatically calculated from date |
| task_description | Work performed / task description |
| deliverables | Deliverables or output |
| blockers | Blockers or dependencies |
| hours_spent | Total working hours |
| status | Current task status |
| notes | Additional comments |
| created_at | Record creation timestamp |
| updated_at | Last update timestamp |

When a new Daily Work Log is created, its status is automatically:

```text
To Do
```

The `update_work_status` MCP tool changes the status to:

```text
Done
```

---

# MCP Tools

The server currently provides five MCP tools.

## 1. add_daily_work_log

Adds a new Daily Work Log to the SQLite database.

Inputs include:

- Work Date
- Task Description
- Deliverables
- Blockers
- Hours Spent
- Notes

The day is automatically calculated from the entered date.

The default status is automatically set to `To Do`.

---

## 2. list_daily_work_logs

Retrieves the Daily Work Logs stored in the database.

Logs can optionally be filtered using their status.

Examples:

```text
To Do
Done
```

---

## 3. update_work_status

Marks an existing Daily Work Log as:

```text
Done
```

The Log ID is required to identify the record.

---

## 4. delete_daily_work_log

Deletes a Daily Work Log using its Log ID.

---

## 5. get_work_summary

Returns a summary containing:

- Total Work Logs
- Completed Logs
- To Do Logs
- Total Hours Spent

---

# Setup Instructions

## 1. Open the Project

Open the project folder in VS Code:

```powershell
cd D:\MCP_Server
```

---

## 2. Activate Virtual Environment

Run:

```powershell
.\venv\Scripts\Activate.ps1
```

The terminal should show:

```text
(venv) PS D:\MCP_Server>
```

### PowerShell Execution Policy Issue

If PowerShell prevents the virtual environment from activating, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# Running the Project

The following commands are used to verify and run the MCP server.

## Step 1 - Check server.py for syntax errors

Run:

```powershell
python -m py_compile server.py
```

If no error appears, the Python file compiled successfully.

---

## Step 2 - Verify the MCP Server

Run:

```powershell
python -c "from server import mcp; print('Server loaded successfully')"
```

Expected output:

```text
Server loaded successfully
```

---

## Step 3 - Initialize the SQLite Database

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

This creates the database/table if it does not already exist.

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

> The port numbers and authentication token can change every time MCP Inspector starts.

The browser should open MCP Inspector automatically.

---

# Quick Run Commands

For normal development, use:

```powershell
cd D:\MCP_Server

.\venv\Scripts\Activate.ps1

python -m py_compile server.py

python database.py

npx @modelcontextprotocol/inspector python server.py
```

For additional server verification, run:

```powershell
python -c "from server import mcp; print('Server loaded successfully')"
```

---

# Using MCP Inspector

After MCP Inspector opens:

1. Open the **Tools** section.
2. Select `add_daily_work_log`.
3. Enter the work log information.
4. Click **Execute Tool**.
5. Select `list_daily_work_logs`.
6. Execute the tool to verify that the record was stored.
7. Use `update_work_status` to mark a work log as Done.
8. Use `delete_daily_work_log` when a record needs to be removed.
9. Use `get_work_summary` to view the overall internship work summary.

---

# Data Flow

```text
    MCP Inspector
          |
          v
      MCP Tool
          |
          v
      server.py
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
User enters Daily Work Log
          |
          v
   add_daily_work_log
          |
          v
    INSERT SQL Query
          |
          v
   intern_tracker.db
          |
          v
  daily_work_log table
```

---

# Viewing Stored Data

The `intern_tracker.db` file is a binary SQLite database file, so it should not be opened as a normal text file.

Use a SQLite viewer/editor extension in VS Code.

Open:

```text
intern_tracker.db
```

Then select:

```text
TABLES
   └── daily_work_log
```

The stored records will be displayed in table format.

You can also verify the data from the terminal:

```powershell
python -c "import sqlite3; con=sqlite3.connect('intern_tracker.db'); rows=con.execute('SELECT * FROM daily_work_log').fetchall(); print(rows); con.close()"
```

---

# Current Project Status

The following functionality has been completed:

- [x] Python MCP server setup
- [x] FastMCP integration
- [x] SQLite database setup
- [x] Daily Work Log table
- [x] Add Daily Work Log
- [x] List Daily Work Logs
- [x] Update Work Status
- [x] Delete Daily Work Log
- [x] Work Summary
- [x] Automatic day calculation
- [x] Default `To Do` status
- [x] MCP Inspector integration
- [x] SQLite data persistence
- [x] End-to-end MCP tool testing

---

## Future Development

Future versions of the project can include:

- MCP Resources
- MCP Prompts
- Additional validation
- Duplicate work-date handling
- Improved reporting and summaries

---

## Developer

**Soham Thoke**

AI Engineering Intern

---

## Project Purpose

This project was developed to understand and implement a Python-based MCP server while building a practical internship Daily Work Log tracking system using MCP tools and SQLite.