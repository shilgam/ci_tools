pipeline {
    agent any
    stages {
        stage('check ver') {
            when {
                branch 'ci_jenkins'
            }
            steps {
                sh '''
                    whoami
                    id

                    pwd

                    ls -la .

                    printenv

                    docker image ls | grep tdd-with-python

                    docker-compose --file docker-compose.yml build

                    docker image ls | grep tdd-with-python

                    docker-compose --file docker-compose.yml run --rm web python manage.py test lists

                    docker-compose --file docker-compose.test.yml run --rm web

                    docker-compose --file docker-compose.test.yml down
                   '''
            }
        }
    }
}
