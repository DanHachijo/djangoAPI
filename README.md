# PostgreSQLのインストール
では自分が使っているPCにPostgresをインストールしましょう。

本番環境ではUbuntuとかのLinuxのサーバーにPostgresを入れなおすことになりますが、テスト環境として入れておいたら後からコードも書き直さなくてよいので準備しておきます。

 

Postgresの公式サイト

https://www.postgresql.org/

 

インストールはここから

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

 

この際にDB名とユーザー名、そのPWを保管しておきましょう。

 

 psycopg2のインストール
ではDjangoがPostgreSQLのデータベースとコミュニケーションを取るためのアダプターをインストールします。

 

pip install psycopg2
 

https://github.com/psycopg/psycopg2


 

Settings.pyの設定
ではSSQLiteの設定をコメントアウトして下記の用に設定していきます。

```
DATABASES = {

   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       
       'NAME': '<database_name>',
       
       'USER': '<database_username>',
       
       'PASSWORD': '<password>',
       
       'HOST': '<database_hostname_or_ip>',
       
       'PORT': '<database_port>',
   }

}
```

あとはいつも通りにDBのマイグレーションを行います。

python manage.py makemigrations

python manage.py migrate



python manage.py createsuperuser



http://127.0.0.1:8000/admin/

