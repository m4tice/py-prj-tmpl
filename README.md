# Introduction  
This Git repo serves as a template for a newly started Python Project  


**Git commit message**  
Please start the commit message with the following tags:  

* Create new file 
```
create: <message>  
```
* Add new code 
```
add: <message>  
```
* Update file / code
```
update: <message>
```
* Remove file / code
```
remove: <messasge>
```  


**Environment handling**  
* Command to create new python virtual environment
```
python<version> -m venv <virtual-environment-name>
```  

* Command to activate created virtual environment
```
.venv\Scripts\activate.bat
```  

* Command to install libraries listed in requirements.txt
```
pip install -r requirements.txt
```  

* Command to export existing libraries to requirements.txt
```
pip freeze > requirements.txt
```  


**Pytest**  
Command to run pytest
```
pytest -vv
```  


**SQL Database handling**  
Reference: [m4tice-python-sqlite3](https://github.com/m4tice/python-sqlite3)  


**Web Development**  
Command to run flask application
```
flask run
```
or in debug mode
```
flask run --debug
```  

Command to run fastapi application
with fastapi[standard]
```
fastapi dev main.py
```
or
```
uvicorn main:app --reload
```  


**Pylint**  
Github's commitment to this project is managed with Pylint.  
Pylint warnings will prevent the commit until all the warnings are resolved.  
In case you cannot resolve the warning, leave the following comment at the end of the same line  

    # pylint: disable=<pylint-warning-1>, <pylint-warning-2>, etc.

For example:  
* Pylint warning:  
    ```
    Line too long (145/100) Pylint(C0301:line-too-long)  
    ```  

* To disable it:  
    ```
    # pylint: disable=line-too-long  
    ```  

In case you want to disable pylint check with the whole file, put the following comment at the beginning of the *.py module:  

* Pylint < 0.25:  
    ```
    # pylint: disable-all  
    ```  

* Pylint 0.26.1 ->:  
    ```
    # pylint: skip-file  
    ```

You might not like it, but that's my preference to keep things in place ;)
