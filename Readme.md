## Simple blog site developed using Django

This blog site has following functionalities:
1. Account registration.
2. Login and logout of Account
3. Creating new post.
4. Editing existing post.
5. View account information.
6. Updating password and or email.

**__Use below config file to debug in vscode__**

```

{
            "name": "Python: Flask (0.11.x or later)",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "run.py",
                "FLASK_ENV": "development",
                "EMAIL_USER": "email@gmail.com",
                "EMAIL_PASS": "password",
                "SECRET_KEY": "5791628bb0b13ce0c676dfde280ba245",
                "SQLALCHEMY_DATABASE_URI": "sqlite:///site.db"
            },
            "args": [
                "run",
                //"--no-debugger",
                //"--no-reload"
            ]
        }
        
    ```
