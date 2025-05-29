1.	Ma,First we have to store captive portal page in “/var/www/index.html”
2.	Now stop network manager
 
3.	Flash iptables
 
4.	Now we have  to run dnsmasq and hostapd from files:
 
5.	Now we have to modify apache2 configuration files in rewrite rules file :
 
 
6.	Now we have to enable ip and netmask:
 
7.	Now we have to enable apache rewrite:
 
8.	Restart apache
 
9.	Turn apache on:
 
Now you have to use to capture traffic:
 
Use wire shark to read post request to get password:
 
