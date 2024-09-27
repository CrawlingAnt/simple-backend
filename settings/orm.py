tortoise_orm = {
    'connections': {
        # Dict format for connection
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'leon',
                'password': 'a198man204',
                'database': 'study_system',
                'minsize': 1,
                'maxsize': 10,
                'charset': 'utf8mb4'
            }
        },
    },
    'apps': {
        'models': {
            'models': ['user.models'],
            # If no default_connection specified, defaults to 'default'
            'default_connection': 'default',
        }
    }
}
