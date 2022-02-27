# TMask_NIFI_DB_migration
Migracja bazy Postgres wraz z wszystkimi schematami i tabelami, plus kopia w formacie JSON


---------



![2022-02-27_07-49](https://user-images.githubusercontent.com/75216446/155878749-c114b1f3-8a97-4c5a-8e98-8014398cc1f7.png)


Nifi Processor - ListDatabaseTables --> Adventureworks pobieramy schematy, listę tabel, i typy kolumn. 

Następnie tworzymy strukturę JSON



![ColumnTypeToJson](https://user-images.githubusercontent.com/75216446/155878912-8941433e-f861-4284-98b6-91989900f91a.png)


Tworzymy połączenie do bazy zapasowej i za pomocą [skryptu w python](https://github.com/TMaskpl/TMask_NIFI_DB_Postgres_Migration/blob/main/create_postgres_schema_and_tables_with_json.py) tworzymy odpowiednie polecenie SQL.

![finalSqlQuery](https://user-images.githubusercontent.com/75216446/155878950-40dd5ec9-cd03-4e29-98b9-0fb198e611a1.png)


Dodatkowo każda struktura tabeli zapisana jest w pliku JSON


![JsonFiles](https://user-images.githubusercontent.com/75216446/155878966-ad8ce714-a42e-4582-9dbe-0eec93faa8d0.png)
