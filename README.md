# Use Django
##Basic API using Django

- **Fedora**
  - Install MariaDB [https://www.if-not-true-then-false.com/2013/install-mariadb-on-fedora-centos-rhel/]
  - To set up MariaDB as Django´s database install:<br />
  ```
    pip install Django mysqlclient
  ```
  To solve "OSError: mysql_config not found"
  ```
    sudo dnf install mysql-devel
  ```
  And run again the first command
  
  **Set up migration**<br />
  - Navigate to UseDJango/TolletAdmin/
  ```
    python3 manage.py makemigrations
    python3 manage.py sqlmigrate boards 0001
    python3 manage.py migrate
  ```
