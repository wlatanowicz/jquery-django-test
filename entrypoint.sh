#!/usr/bin/env sh

set -x

devserver()
{
    echo "Starting dev server"
    python manage.py runserver 0.0.0.0:8000 || exit $?
}

migrate() {
    echo "Running migrations"
    python manage.py migrate --noinput || exit $?
}

init_createsuperuser() {
    if [ ! -f ./.status/admin ]
    then
        echo "Creating Superuser"

        export ADMIN_USER=${ADMIN_USER:-admin}
        export ADMIN_PASSWORD=${ADMIN_USER:-admin}
        export ADMIN_EMAIL=${ADMIN_USER:-admin@example.org}

        echo "from os import environ; \
         from django.contrib.auth.models import User; \
         User.objects.filter(username=environ.get('ADMIN_USER')).delete(); \
         User.objects.create_superuser(environ.get('ADMIN_USER'), environ.get('ADMIN_EMAIL'), environ.get('ADMIN_PASSWORD'))" \
         | python manage.py shell || exit $?

        mkdir -p ./.status
        date > ./.status/admin
        echo "done"
    else
        echo "Superuser already created"
    fi
}


init_install_local_repos() {
    if [ ! -f /tmp/.status_local_repos ]
    then
        echo "Installing local repos"

        BASE_PATH=/root/repos
        for repo in `ls $BASE_PATH`
        do
            pip install --no-cache-dir --upgrade -e $BASE_PATH/$repo || exit $?
        done

        mkdir -p ./.status
        date > /tmp/.status_local_repos
        echo "done"
    fi
}

start() {
    for cmd in $@
    do
       ${cmd} || exit $?
    done
}

"$@" || exit $?
