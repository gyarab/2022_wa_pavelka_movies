# 2022_wa_pavelka_movies

Postup spuštění:
1) python -m venv venv
2) venv/scripts/activate.ps1 (pro Powershell) nebo source venv/scripts/activate (pro Gitbash)
3) pip install -r requirements.txt
4) cd gamdb
5) py manage.py loaddata fixtures/*
6) py manage.py makemigrations
7) py manage.py migrate
8) py manage.py runserver
