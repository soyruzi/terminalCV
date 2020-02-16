# terminalCV
A Fun command line CV for IT Professionals and enthusiasts.
Feel free to use it and modify it to suit your needs.

Forked from https://github.com/danielhauck/terminalCV this is probably the only active and up to date fork of this project.


# watch it live

See it in action right here: https://cv.4s3ti.net

# Usage
terminalCV is a little python script that uses jinja2 to render a html-template with javascript stuff in it.
After it is rendered, you just need to upload it to your webroot or subdirectory or build the docker image with the provided Dockerfile.

To use it, clone the repository and install requirements with pip:

	$  git clone git@github.com:4s3ti/terminalCV.git && cd terminalCV
	$  sudo pip install -r requirements.txt

Modify the about.yml with your favorite text editor

And finnaly render the stuff:

	$  python render.py

If everything worked you can just upload the directory www:

	rsync -aH www/ user@webhost:/srv/www/terminalCV

## The docker way

If you want to run it as a docker container, change nginx/

# Jquery-Terminal
terminalCV makes use of J. Cubics JQuery-Terminal http://terminal.jcubic.pl/ .
Thanks for this!
