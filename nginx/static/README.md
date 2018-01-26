server {
    listen 80;

    location / {
        proxy_pass http://web:5000;
    }

    location /css/ {
        root /opt/web/static/;
    }

    location /deploy/ {
        root /opt/web/static;
    }

    location /vendor/ {
        root /opt/web/static;
    }

    location /sass/ {
        root /opt/web/static;
    }

    location /img/ {
        root /opt/web/static;
    }

    location /js/ {
        root /opt/web/static;
    }

    location /less/ {
        root /opt/web/static;
    }
}