sample_flask_app
================================
    
A sample Python flask application with a non-relational data store and bootstrap framework.

Diretory Structure
-------------------------

The application folder structure is defined below:

    lib/
        <app_name>/
            <version>/
                lib/
                    <object>/
                api/
                    <object>/
    www/
        templates/
            <object>/
        static/
            <object>/
    tests/
        lib_tests/
            <app_name>/
                <version>_tests/
                    lib_tests/
                        <object>_tests/
                    api_tests/
                        <object>_tests/


Quick Start
-------------------------

Execute ./api/main.py to launch the API.

    $ ./lib/sample/v1/api/main.py
    * Running on http://0.0.0.0:8000/
    * Restarting with reloader

Execute ./www/main.py to launch the UI.

    $ ./www/main.py
    * Running on http://0.0.0.0:8080/
    * Restarting with reloader



