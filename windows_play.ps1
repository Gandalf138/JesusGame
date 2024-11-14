if(![System.IO.File]::Exists(./venv)){
    py -m venv venv
}
./venv/Scripts/Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
py main.py
