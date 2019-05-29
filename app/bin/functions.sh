#!/bin/sh

function list_files {
  ls -lah
}

function build_and_deploy_image_to_heroku {
  # >> NOTE: env vars should be defined: $HEROKU_LOGIN, $HEROKU_APP_NAME, $HEROKU_API_KEY <<

  # login
  echo $HEROKU_API_KEY | docker login --username=$HEROKU_LOGIN --password-stdin registry.heroku.com

  # build
  docker build --tag registry.heroku.com/$HEROKU_APP_NAME/web .

  # push
  docker push registry.heroku.com/$HEROKU_APP_NAME/web

  # release
  docker-compose --project-name deploy --file docker-compose.deploy.yml run -e HEROKU_API_KEY=$HEROKU_API_KEY --rm heroku container:release web --app $HEROKU_APP_NAME
}
