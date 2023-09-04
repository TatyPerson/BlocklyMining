# BlocklyMining
BlocklyMining is a software tool to apply Blockly static code analysis.

The first version of the tool was worked in the https://github.com/TatyPerson/PythonAnalyzerForBKY repository.

# User manual

To run the analysis you must first have the MIT App Inventor projects you want to analyze in a specific directory. Let's call this directory "projects". Then, to launch the BlocklyMining tool analysis to need to execute the following command in the terminal:

```python BlocklyMining.py --source=appinventor --database=none --path=/projects```

In this case, after running the analysis, a .csv file will be generated in the "projects" directory with the results of applying the metrics implemented in BlocklyMining on the given set of MIT App Inventor projects.

If you need to save the data in a MySQL database you must create the database by importing the [BlocklyMiningDatabase.sql](https://github.com/TatyPerson/BlocklyMining/blob/main/database-schema/BlocklyMiningDatabase.sql) and then, you should edit the [ConfigurationParameters.cfg](https://github.com/TatyPerson/BlocklyMining/blob/main/source/ConfigurationParameters.cfg) file to add the parameters related to the MySQL database connection: host, user, password and the database name.

Below, you can see an ConfigurationParameters.cfg example file:

```
[MYSQL_DATABASE]
MYSQL_HOST = localhost
MYSQL_USER = user
MYSQL_PASSWORD = password
MYSQL_DATABASE = BlocklyMiningDatabase
```

Finally, you can launch the analysis executing the next command in the terminal:

```python BlocklyMining.py --source=appinventor --database=mysql --path=/projects```

With the previous command the result of applying all the metrics on the set of MIT App Inventor projects will be stored identifying in which file each code smell is found.

The BlocklyMining tool is designed to support different block-based programming environments as well as different types of database managers. Currently, the supported block programming environment is MIT App Inventor and the supported database manager is MySQL.
