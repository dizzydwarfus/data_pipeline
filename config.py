import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '',
            'DB_NAME': '',
            'DB_USER': '', # to externalize, use 'setx or set' command in cmd to set environment variable, and access using 'os.environ.get('source_var_name')'
            'DB_PASS': '' # to externalize, use 'setx or set' command in cmd to set environment variable, and access using 'os.environ.get('source_var_name')'
        },

        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '',
            'DB_NAME': '',
            'DB_USER': '', # to externalize, use 'setx or set' command in cmd to set environment variable, and access using 'os.environ.get('source_var_name')'
            'DB_PASS': '' # to externalize, use 'setx or set' command in cmd to set environment variable, and access using 'os.environ.get('source_var_name')'
        }
    }
}