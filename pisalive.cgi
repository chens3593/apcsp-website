#!/bin/bash


echo -e "Content-type: text/html\n\n"

echo "<h1>Raspberry Pi Status: $(hostname)</h1>"

echo "<h2>Host Info</h2>"
echo "<li>Host name : $(hostname)</li>"
echo "<li>IP Address: $(hostname -I)</li>"
echo "<li>OS name:    $(grep PRETTY_NAME /etc/os-release | sed 's/.*"\(.*\)"/\1/')</li>"

echo "<h2>Who is logged in</h2>"
echo "<pre>$(./pisalive)</pre>"
