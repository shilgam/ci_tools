pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker-compose --file docker-compose.yml build'
                sh '''
                    docker image ls
                    whoami
                    id
                    printenv
                    docker system info
                   '''
            }
        }

        stage('Test') {
            parallel {
                stage('Unit') {
                    steps {
                        sh 'docker-compose --project-name unitTest --file docker-compose.yml run --rm web python manage.py test lists'
                        sh 'docker-compose --project-name unitTest --file docker-compose.yml down'
                    }
                }
                stage('Func') {
                    steps {
                        sh 'docker-compose --project-name funcTest --file docker-compose.test.yml run --rm web'
                        sh 'docker-compose --project-name funcTest --file docker-compose.test.yml down'
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                expression { BRANCH_NAME ==~ /(master|jenkins).*/ }
            }
            environment {
                HEROKU_APP_NAME = 'minimylist-acc'
                HEROKU_LOGIN = '_'
                // HEROKU_API_KEY
            }
            steps {
                sh '''
                    # login
                    docker logout
                    echo $HEROKU_API_KEY | docker login --username=$HEROKU_LOGIN --password-stdin registry.heroku.com

                    # build
                    docker build --tag registry.heroku.com/$HEROKU_APP_NAME/web .

                    # push
                    docker push registry.heroku.com/$HEROKU_APP_NAME/web

                    # release
                    docker-compose --project-name deploy --file docker-compose.deploy.yml run -e HEROKU_API_KEY=$HEROKU_API_KEY --rm heroku container:release web --app $HEROKU_APP_NAME
                   '''
            }
        }
        stage('Cleanup') {
            steps {
                sh '''
                    docker container ls

                    # remove dangling images
                    docker image rm $(docker images -q -f dangling=true)

                    docker image ls
                   '''
            }
        }
    }
}
