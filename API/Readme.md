creating a virual environment
in terminal open cmd
run:
py -3 -m venv <name> e.g. venv
than open command platte:
ctrl shift p
type select interpreter
then type .\venv\Scripts\python.exe
to provide current interpretter path
now in terminal run
venv\Scripts\activate.bat
in terminal (venv) will appear in begining of the path in terminal
this shows the virtual venv is activated.
now install required items
pip install fastapi[all]
to install all the packages at once rather than installing only standard.
this can prove helpfull if you are new to this and do not know how the backend is working and want to avaoid unwanted dependency errors.