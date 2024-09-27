aerich init -t settings.orm.tortoise_orm 
aerich init-db
aerich migrate --name 'init'
aerich upgrade
aerich downgrade