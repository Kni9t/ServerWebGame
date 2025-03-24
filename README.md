# v 0.1.2

# Preparing for start
To start the server, you must first install the python dependencies. To do this, run the following command in the project directory:

```cmd
pip install -r requirements.txt
```
Then you need to host the web part of the project (**index.html** and **asset/**) to the **web/** directory

And the last step, you need to specify the address of your database server. In the file main.py find the next line at the beginning and correct it:

```Python
databaseController = DBcontroller.db_controller("mongodb://192.168.1.13:27017/")
```

# How to start server
To start the server, simply run the following command:

```cmd
python main.py
```