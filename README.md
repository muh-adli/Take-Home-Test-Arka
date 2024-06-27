# Take Home Test Arka

## How to run

make sure you have Python 3.8 or latest to run the following repo

### install python environment 

run this command on Powershell / terminal:

```powershell
python -m venv .venv
```

this code will make virtual environment to make sure its dependencies separated with your computer environment

### activate environment and install requirements.txt

to activate the virtual environment use this command on your powershell, or you can alternatively activate with activate scripts in scripts folder under .venv

```powershell
.venv\scripts\activate
```

after activating virtual environment, you can continue to install the requirements with this command

```python
pip install -r requirements.txt
```

wait for some time because without a dependencies the program might found some trouble

## Inventory API

### User, Product, Clients table

to build the table as assignment needs, i'm building model at models.py on API django app

so first building models, tables, column, and its options that meets the requirement, then run migration to make django apply to database.

you could run the migration by run `manage.py migrate` command

```py
python InventoryAPI/manage.py migrate
```

### JSON, REST, and XML APIs

for the API you can run django by run manage.py with runserver command

```python
python InventoryAPI/manage.py runserver
```

wait while system checking is running, after chekcing the server will start. By default the server will start at
```http://127.0.0.1:8000/```

then you can open the homepage by opening the web then you can choose which API you'd like to see. or alternatively, you can use this links
|   |   |   |
|:---:|:---:|:---:|
|__[JSON](http://127.0.0.1:8000/api/v1/inventory/json/)__| __[REST](http://127.0.0.1:8000/api/v1/inventory/rest/)__ | __[XML](http://127.0.0.1:8000/api/v1/inventory/xml/)__ |

for exit/quiting the server, you can use `CTRL + C` with your keyboard. The server will be terminated and back into default terminal.

### Integration Test
for the integration test, you could run by change `runserver` into `test [module]` . or in this case is
```python
python InventoryAPI/manage.py test API
```
and the output test will be printed on terminal

## Python Function

for the Python Function you could see RemoveDuplicate.py for the function.

### Unit Test

for the unit test you could run the RD_Test.py, or alternatively use this command under PythonFunction folder

```powershell
python -m unittest PythonFunction/RD_Test.py
```
