This folder can store any local ML models, embeddings, or pickled objects used by the project.
Currently this project does not require any local models; question generation is deterministic.
cd "C:\Users\VENKATSAI\Desktop\New folder\talentscout-hiring-assistant-main"


python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run app/main.py





