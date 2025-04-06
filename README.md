## Example SQL Lite DB with Python Client

To build and run queries with the SQLite Python client, change into the `python_sql_lite` directory:

```
cd python_sql_lite
```
Then run the build script build the database and create the tables:
```
python3 build.py
```
This command creates the file `pythonssqlite.db`

Finally, to execute query run this command:
```
python3 query.py --query "{your query goes here}"

```
*Note: for the full table schema definitions, see `schema.py`*
