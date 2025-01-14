with open('all past mracx events.txt', 'r') as file:
    data = file.read()
events = eval(data)

# Note: the module name is psycopg, not psycopg3
import psycopg, re

# Connect to an existing database
with psycopg.connect(host="localhost", dbname="postgres", user="postgres", password="mypsql", port=5432) as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS event_links (
                id text PRIMARY KEY,
                event_url text,
                scraped bool)
            """)

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        for i in events[0:20]:

            event_id = re.search('/events/\d+/', i)
            event_id = event_id.group().split('/')[2]

            cur.execute("INSERT INTO event_links (id, event_url) VALUES (%s, %s)", [event_id, i])

        conn.commit()
