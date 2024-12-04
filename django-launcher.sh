#!/usr/bin/env sh

. /home/vscode/miniconda3/bin/activate
conda activate spas
python3 manage.py collectstatic --noinput
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
