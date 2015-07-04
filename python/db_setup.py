import rethinkdb as r

# connects to localhost:28015 by default
conn = r.connect()

# Create tables
db_name = 'brigadepulse'
statements = (
    r.db_drop(db_name),
    r.db_create(db_name),
    r.db(db_name).table_create('brigades'),
    r.db(db_name).table_create('projects'),
)
for stmt in statements:
    try:
        stmt.run(conn)
    except r.RqlRuntimeError:
        pass

# Gather organization data from CFA api