# build_files.sh
pip install -r requirements.txt
cd "$(dirname "$0")"
cd "src"
python3.9 manage.py collectstatic
