# Setting up Continuous Integration with Jenkins

Tips:
1. How to install Docker:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
1. How to install docker-compose: https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04

1. How to create non-root user:
https://github.com/hjwp/Book-TDD-Web-Dev-Python/blob/master/server-quickstart.md

NOTE: all commands should be done in the server side.

## Installing Jenkins

1. Launch Jenkins app:

        $ docker-compose --file docker-compose-jenkins.yml up

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

### Securing your Jenkins instance

To finish off securing your Jenkins instance, you’ll want to set up HTTPS, by getting nginx HTTPS to use a self-signed cert, and proxy requests from port 443 to port 8080. Then you can even block port 8080 on the firewall.

1. Install Nginx web server:

        $ apt-get update
        $ apt-get install nginx

1. Create the SSL Certificate (under the Nginx conf dir):

        $ mkdir /etc/nginx/ssl

    More info: "How to create a self-signed SSL certificate" https://www.digitalocean.com/community/tutorials/how-to-create-an-ssl-certificate-on-nginx-for-ubuntu-14-04

1. Create the SSL key and certificate files

        $ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt

1. Configure Nginx to Use SSL

1. Create new configuration for Jenkins.

        ## Remove default configuration
        $ cd /etc/nginx/sites-available
        $ sudo rm default ../sites-enabled/default
        ## Create new configuration for Jenkins
        $ sudo touch jenkins
        ## copy-paste `nginx.jenkins.conf` file content to this file

    NOTES:
    - Example config available in `nginx.jenkins.conf` file in this dir.
    - Official Jenkins Ubuntu installation guide: https://wiki.jenkins.io/display/JENKINS/Installing+Jenkins+on+Ubuntu

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

1. Install [Git Plugin](https://plugins.jenkins.io/git)

1. Set up new project and start first build

1. How to run Jenkins build automatically when a change is pushed to GitHub: https://stackoverflow.com/a/30577823
