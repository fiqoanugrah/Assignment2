release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json'
web: gunicorn Assignment2_M.FiqoAnugrah.wsgi --log-file -