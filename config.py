import os
    
DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '139.99.209.131',
            'DB_NAME': 'retail_db',
            'DB_USER': 'retail_user', # to externalize, use 'setx or set' command in cmd to set environment variable, and access using 'os.environ.get('source_var_name')'
            'DB_PASS': 'itversity' # to externalize, use 'setx or set' command in cmd to set environment variable, and access using 'os.environ.get('source_var_name')'
        },

        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '139.99.209.131',
            'DB_NAME': 'retail_db',
            'DB_USER': 'retail_user', # to externalize, use 'setx or set' command in cmd to set environment variable, and access using 'os.environ.get('source_var_name')'
            'DB_PASS': 'itversity' # to externalize, use 'setx or set' command in cmd to set environment variable, and access using 'os.environ.get('source_var_name')'
        }
    }
}