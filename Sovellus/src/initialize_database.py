

def delete_database(connection):
    """Deletes event log"""

    cursor = connection.cursor()
    cursor.execute("""
        drop table if exists playerevents;
    """)

    connection.commit()


def create_database(connection):
    """Creates event log"""

    cursor = connection.cursor()
    cursor.execute("""
        create table playerevents (
            eventlog text primary key
        );
    """)

    connection.commit()


def add_to_database(connection, eventname: str):
    cursor = connection.cursor()

    cursor.execute(f"""
        INSERT INTO playerevents VALUES
            ('{eventname}')
    """)


def initialize_database(connection):
    """Initialize database"""
    delete_database(connection)
    create_database(connection)
