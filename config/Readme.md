# credentials folder

in this folder you should have this structure :
- credentials
  - apiKey.py
  - databaseConfig.py
  - databaseDescription.py

Each file should follow this structure:

# apiKey.py
```
# you can visit https://console.mistral.ai/home
# create an account and get your API key
MISTRAL_API = "Youe Mistral API Key"
```

# databaseConfig.py
```
# databaseConfig.py

CONFIG = {

    # you need to specify the database engine you want to use
    "engine": "mysql",  # "mysql", "postgresql", "sqlite"

    # then you need to provide the configuration for the database engine
    # you can use one of the following configurations as an example

    "sqlite": {
        "db_path": "path to your sqlite database file"  # e.g., "my_database.db"
    },

    "mysql": {
        "host": "your host",  # e.g., "localhost" 
        "user": "your username", # e.g., "root"
        "password": "your password", 
        "database": "your database name",
        "port": the_port_number  # e.g., 3306
    },

    "postgresql": {
        "host": "your host",  # e.g., "localhost" 
        "user": "your username", # e.g., "postgres"
        "password": "your password", 
        "database": "your database name",
        "port": the_port_number  # e.g., 5432
    }
}
```

# databaseDescription.py

```
# databaseDescription.py

# you need to fill the description dictionnary, the key is the table name,
# and the value is the table description
DESCRIPTION = {
    "table1":'''
        +----+-------+
        | id | name  |
        +----+-------+
        | int| text  |
        +----+-------+
    ''',
    "table2":'''
        +----+-------+
        | id | name  |
        +----+-------+
        | int| text  |
        +----+-------+
    '''
}

# it's good to provide some examples of the tables, you can run the query
# select * from table_name limit 1;
EXAMPLES = {
    "table1":'''
        +----+-------+
        | id | name  |
        +----+-------+
        |  1 | foo   |
        +----+-------+
    ''',
    "table2":'''
        +----+-------+
        | id | name  |
        +----+-------+
        |  1 | bar   |
        +----+-------+
    '''
}
```