with open('formatted past events.txt', 'r') as file:
    data = file.read()
events = eval(data)

import psycopg, re
with psycopg.connect(host="localhost", dbname="postgres", user="postgres", password="mypsql", port=5432) as conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS event_links (
                id text PRIMARY KEY,
                event_url text,
                scraped bool)
            """)

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        for i in events:
            event_id = re.search('/events/\d+/', i)
            event_id = event_id.group().split('/')[2]
            cur.execute("""INSERT INTO event_links (id, event_url) 
                        VALUES (%s, %s) ON CONFLICT (id) DO NOTHING""", 
                        [event_id, i])

        conn.commit()
