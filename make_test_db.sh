rm -rf ./instance;
flask db init;
flask db migrate;
flask db upgrade;
flask seed all;