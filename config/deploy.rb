lock '~> 3.11.0'

set :application, 'timecrowd-django-example'
set :repo_url, 'git@github.com:timecrowd-blog/timecrowd-django-example.git'
set :deploy_to, '/var/www/timecrowd-django-example'

set :project, 'mysite'
append :linked_files, 'mysite/.env' 
append :linked_dirs, 'venv', 'public/static'

set :passenger_restart_with_touch, true
