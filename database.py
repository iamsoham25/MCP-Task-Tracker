import sqlite3

# Database file name
DATABASE_NAME = "intern_tracker.db"


def get_connection():
    """
    Create and return a connection to the SQLite database.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Create the Daily Work Log table if it does not already exist.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_work_log (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            work_date TEXT NOT NULL,

            day TEXT NOT NULL,

            task_description TEXT NOT NULL,

            deliverables TEXT,

            blockers TEXT,

            hours_spent REAL,

            status TEXT DEFAULT 'To Do',

            notes TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()
    connection.close()


def reset_database():
    """
    Delete the existing table and recreate it.
    Use only during development/testing.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS daily_work_log
    """)

    connection.commit()
    connection.close()

    initialize_database()


if __name__ == "__main__":

    initialize_database()

    print("=" * 50)
    print("Intern Tracker Database Initialized Successfully")
    print("=" * 50)