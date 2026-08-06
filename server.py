from mcp.server.fastmcp import FastMCP
from typing import Optional
from datetime import datetime

from database import (
    get_connection,
    initialize_database
)


# ---------------------------------------------------------
# Initialize Database
# ---------------------------------------------------------

initialize_database()


# ---------------------------------------------------------
# Create MCP Server
# ---------------------------------------------------------

mcp = FastMCP("TaskTracker")


# =========================================================
# TOOL 1 : Add Daily Work Log
# =========================================================

@mcp.tool()
def add_daily_work_log(
    work_date: str,
    task_description: str,
    deliverables: Optional[str] = "",
    blockers: Optional[str] = "",
    hours_spent: float = 8,
    notes: Optional[str] = ""
) -> str:
    """
    Add a new Daily Work Log entry.

    Args:
        work_date:
            Date in YYYY-MM-DD format.

        task_description:
            Work performed on that day.

        deliverables:
            Output produced.

        blockers:
            Any blockers or dependencies.

        hours_spent:
            Total working hours.

        notes:
            Additional comments.
    """

    # Automatically calculate day
    day = datetime.strptime(
        work_date,
        "%Y-%m-%d"
    ).strftime("%A")

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO daily_work_log(

            work_date,
            day,
            task_description,
            deliverables,
            blockers,
            hours_spent,
            status,
            notes

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            work_date,
            day,
            task_description,
            deliverables,
            blockers,
            hours_spent,
            "To Do",
            notes
        )
    )

    log_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return (
        f"""
            Daily Work Log Added Successfully

            Log ID : {log_id}

            Date : {work_date}

            Day : {day}

            Status : To Do
"""
    )


# =========================================================
# TOOL 2 : List Daily Work Logs
# =========================================================

@mcp.tool()
def list_daily_work_logs(
    status: Optional[str] = None
) -> list:
    """
    Retrieve Daily Work Logs.

    Args:
        status:
            Optional filter.

            Example:
            Done

            In Progress

            To Do
    """

    connection = get_connection()

    cursor = connection.cursor()

    if status:

        cursor.execute(
            """
            SELECT *

            FROM daily_work_log

            WHERE LOWER(status)=LOWER(?)

            ORDER BY work_date DESC
            """,
            (status,)
        )

    else:

        cursor.execute(
            """
            SELECT *

            FROM daily_work_log

            ORDER BY work_date DESC
            """
        )

    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]

# =========================================================
# TOOL 3 : Update Work Status
# =========================================================

@mcp.tool()
def update_work_status(
    log_id: int
) -> str:
    """
    Mark a Daily Work Log as Done.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE daily_work_log
        SET status = 'Done',
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (log_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        return f"No work log found with ID {log_id}"

    connection.close()

    return f"Work Log #{log_id} marked as Done."


# =========================================================
# TOOL 4 : Delete Daily Work Log
# =========================================================

@mcp.tool()
def delete_daily_work_log(
    log_id: int
) -> str:
    """
    Delete a Daily Work Log.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT task_description
        FROM daily_work_log
        WHERE id = ?
        """,
        (log_id,)
    )

    row = cursor.fetchone()

    if not row:
        connection.close()
        return f"No work log found with ID {log_id}"

    cursor.execute(
        """
        DELETE
        FROM daily_work_log
        WHERE id = ?
        """,
        (log_id,)
    )

    connection.commit()
    connection.close()

    return (
        f"Daily Work Log #{log_id} deleted successfully."
    )



# =========================================================
# TOOL 5 : Get Work Summary
# =========================================================

@mcp.tool()
def get_work_summary() -> dict:
    """
    Return a summary of internship work.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM daily_work_log"
    )

    total_logs = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM daily_work_log
        WHERE LOWER(status)='done'
        """
    )

    completed = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM daily_work_log
        WHERE LOWER(status)='to do'
        """
    )

    todo = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT IFNULL(SUM(hours_spent),0)
        FROM daily_work_log
        """
    )

    total_hours = cursor.fetchone()[0]

    connection.close()

    return {
        "total_work_logs": total_logs,
        "completed": completed,
        "todo": todo,
        "total_hours": total_hours
    }


# ---------------------------------------------------------
# Start MCP Server
# ---------------------------------------------------------

if __name__ == "__main__":
    mcp.run(transport="stdio")