# build_files.sh
pip install -r requirements.txt
cd "$(src "$0")" # Change to the directory of the script
python3.9 manage.py collectstatic
