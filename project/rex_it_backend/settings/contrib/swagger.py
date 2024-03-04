from rex_it_backend.settings.environment import env


SPECTACULAR_SETTINGS = {
    'TITLE': 'RexIt Test Task Documentation',
    'VERSION': '1.0.0',
    'SCHEMA_PATH_PREFIX': '/api/v[0-9]',
    'COMPONENT_SPLIT_REQUEST': True,
    'SWAGGER_UI_SETTINGS': {
        'persistAuthorization': True,
    },
}

SWAGGER_URL = env.str('SWAGGER_URL', None)
