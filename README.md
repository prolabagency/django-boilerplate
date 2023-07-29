# django-boilerplate
Django boilerplate by PROlab

### Ngnix
```
server {
    listen 80;
    server_name test2-1.prolab.kg;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static {
        alias /var/www/crm_prolab-back/static/static_root;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
} 
```

### Gunicorn
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/crm_prolab-back
ExecStart=/var/www/crm_prolab-back/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          core.wsgi:application

[Install]
WantedBy=multi-user.target
```
