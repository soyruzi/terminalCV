# terminalCV
A command line CV for sysadmins
This is still WIP, and I am about to add some features.

# watch it live

You can see a live example here(actually mine): http://hauck-daniel.de/cli/

# Usage
terminalCV is a little python script that uses jinja2 to render a html-template with javascript stuff in it.
After it is rendered, you just need to upload it to your webroot or subdirectory.

To use it, clone the repository and install requirements with pip:

	$  git clone git@github.com:hauckd/terminalCV.git && cd terminalCV
	$  sudo pip install -r requirements.txt

Modify the about.yml with your favorite text editor

And finnaly render the stuff:

	$  python render.py

If everything worked you can just upload the directory www:

	rsync -aH www/ user@webhost:/srv/www/terminalCV
  
# Jquery-Terminal
terminalCV makes use of J. Cubics JQuery-Terminal http://terminal.jcubic.pl/ .
Thanks for this!
