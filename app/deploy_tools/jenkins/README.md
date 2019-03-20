# Setting up Continuous Integration with Jenkins

Detailed instructions: https://www.obeythetestinggoat.com/book/chapter_CI.html

## Installing Jenkins

NOTE: all commands should be done in the server side.

1. install the latest version from the official Jenkins apt repo:

        $ wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key \
          | apt-key add -
        $ echo deb http://pkg.jenkins.io/debian-stable binary/ | tee \
          /etc/apt/sources.list.d/jenkins.list
        $ apt update
        $ apt install jenkins

        ## NOTE: last step was failed w/ an error "Failed to start LSB: Start Jenkins at boot time"
        ## Solution: install java8: https://stackoverflow.com/a/49937744

1. Install a few other dependencies:

        $ add-apt-repository ppa:deadsnakes/ppa
        $ apt update
        $ apt install firefox python3.6-venv python3.6-dev xvfb
        ## and, to build fabric3:
        $ apt install build-essential libssl-dev libffi-dev

1. Download, unzip, and install geckodriver too (it was v0.24   at the time of writing, but substitute the latest version as you read this):

        $ wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
        $ tar -xvzf geckodriver-v0.24.0-linux64.tar.gz
        $ mv geckodriver /usr/local/bin
        $ geckodriver --version
        geckodriver 0.24.0

### Adding Some Swap

1. Jenkins is quite memory-hungry, and if you’re running this on a small VM with less than a couple of gigs for RAM, you’ll probably find it gets OOM-killed unless you add some swap:

        $ fallocate -l 4G /swapfile
        $ mkswap /swapfile
        $ chmod 600 /swapfile
        $ swapon /swapfile



## Configuring Jenkins

1. You should now be able to visit Jenkins at the URL/IP for your server on port 8080, and see something like Jenkins unlock screen.
    - For instance: `http://server_IP:8080/`

1. Unlock the server for first-time use:

        $ cat /var/lib/jenkins/secrets/initialAdminPassword

### Adding Plugins

1. Follow the links for Manage Jenkins → Manage Plugins → Available.
1. Add plugins: ShiningPanda, Xvfb

### Telling Jenkins Where to Find Python 3 and Xvfb

We need to tell the ShiningPanda plugin where Python 3 is installed (usually /usr/bin/python3, but you can check with a which python3).

1. Manage Jenkins → Global Tool Configuration

1. Python → Python installations → Add Python (see Where did I leave that Python?; it’s safe to ignore the warning message)

1. Xvfb installation → Add Xvfb installation; enter `/usr/bin` as the installation directory

### Securing your Jenkins instance

To finish off securing your Jenkins instance, you’ll want to set up HTTPS, by getting nginx HTTPS to use a self-signed cert, and proxy requests from port 443 to port 8080. Then you can even block port 8080 on the firewall. I won’t go into detail on that now, but here are a few links to instructions which I found useful:

- How to create a self-signed SSL certificate: https://www.digitalocean.com/community/tutorials/how-to-create-an-ssl-certificate-on-nginx-for-ubuntu-14-04


1. Install Nginx web server:

        $ apt-get update
        $ apt-get install nginx

1.  Create the SSL Certificate (under the Nginx conf dir):

        $ mkdir /etc/nginx/ssl

1. Create the SSL key and certificate files

        $ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt

1. Configure Nginx to Use SSL:

1. Create new configuration for Jenkins. File [available here](app/deploy_tools/jenkins/nginx.jenkins.conf)

1. Link your configuration from `sites-available` to `sites-enabled`:

        $ ln -s /etc/nginx/sites-available/jenkins /etc/nginx/sites-enabled/

1. restart Nginx to use new settings:

        $ service nginx restart

1. Test your setup:

    1. make sure we can still access the site with using normal HTTP:

            http://server_domain_or_IP

    1. check whether our server can use SSL to communicate. Do this by specifying the https protocol instead of the http protocol.

            https://server_domain_or_IP


## Setting Up Project

1. Install Docker and docker-compose:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04


1. Install [Git Plugin](https://plugins.jenkins.io/git)

1. Set up new project and start first build:

        $ docker-compose --file docker-compose.test.yml build
        $ docker-compose --file docker-compose.test.yml run --rm web sh -c 'STAGING_SERVER=minimylist-staging.herokuapp.com python ./manage.py test functional_tests'
