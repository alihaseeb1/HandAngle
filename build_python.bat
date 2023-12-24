@echo off
cd venv/Scripts
call activate
cd ../..

if exist your_app_name.lock (
    echo your_app_name.lock file found. Deleting...
    del your_app_name.lock
) else (
    echo No your_app_name.lock file found.
)

python main.py