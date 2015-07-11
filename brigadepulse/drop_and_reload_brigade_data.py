# Despite the title we can run this script as often or as little as we want :)
import rethinkdb as r
from cfapi import get_all_organizations, get_organization_projects
from os import environ


def re_create_db_and_tables(conn, db_name, table_names):
    drop_db_if_exists(conn, db_name)

    r.db_create(db_name).run(conn)

    # We build up the object by continuosly calling table_create on it.
    for table_name in table_names:
        r.db(db_name).table_create(table_name).run(conn)

    return


def drop_db_if_exists(conn, db_name):
    try:
        r.db_drop(db_name).run(conn)
    except r.RqlRuntimeError:
        # Thrown if database doesn't exists, do nothing
        pass


def main():
    table_names = ["organizations", "projects"]
    db_name = "cfa_raw"

    # Connect to RethinkDB host bound to RETHINKDB_IP or default to "localhost"
    conn = r.connect(host=environ.get("RETHINKDB_IP", "localhost"))

    re_create_db_and_tables(conn, db_name, table_names)

    organizations = get_all_organizations()
    organizations_projects = {organization["name"]: get_organization_projects(organization["all_projects"])
                              for organization in organizations}

    # Add name as an element in the array so it will be inserted with each document
    for org_name, projects in organizations_projects.iteritems():
        for project in projects:
            project["organization_name"] = org_name

    r.db("cfa_raw").table("organizations").insert(organizations).run(conn)
    # Insert every project as a separate document into the "projects" table
    # (we can get back to it with the "organization_name" property
    for projects in organizations_projects.values():
        r.db("cfa_raw").table("projects").insert(projects).run(conn)


# If we run this module as a script, it deletes and rebuilds the RethinkDB
# db and then re-fetches the data using the Code For America api
# (http://codeforamerica.org/api/)
if __name__ == '__main__':
    main()
