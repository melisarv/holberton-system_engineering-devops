# fix a server error

exec { 'Sky is the limit':
  command => 'sed -i "s/15/20000/g" /etc/default/nginx; sudo service nginx restart',
  path    => ['/bin', '/usr/sbin', '/usr/bin', '/usr'],
}
