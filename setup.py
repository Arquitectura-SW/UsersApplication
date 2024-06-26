from setuptools import setup, find_packages

setup(
    name="AppClient",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "asgiref==3.8.1",
        "astroid==3.1.0",
        "dill==0.3.8",
        "Django==4.2.11",
        "djangorestframework==3.15.1",
        "isort==5.13.2",
        "mccabe==0.7.0",
        "pika==1.3.2",
        "platformdirs==4.2.0",
        "psycopg==3.1.18",
        "pylint==3.1.0",
        "sqlparse==0.4.4",
        "tomli==2.0.1",
        "tomlkit==0.12.4",
        "typing_extensions==4.11.0"
    ],


)
