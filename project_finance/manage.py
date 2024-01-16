#!/usr/bin/env python
import os
import sys
import os
from django.core.management import call_command

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_finance.settings')
    try:
        # Define as configurações do Django
        import django
        django.setup()

        # Carrega dados antes de executar a aplicação
        call_command('loaddata', 'profile_data.json')

        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
