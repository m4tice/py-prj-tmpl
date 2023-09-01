# Introduction
This Git repo serves as a template for a newly started Python Project  

**Commit message**  
Please start the commit message with the following tags:  
```
* Add <message>
* Update <message>
* Remove <messasge>
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
