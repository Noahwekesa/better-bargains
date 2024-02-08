# build_files.sh
pip install -r requirements.txt
cd "$(dirname "$0")/src"
python3.9 manage.py collectstatic
