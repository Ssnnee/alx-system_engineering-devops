# Increase the limit

exec { 'increase_limit':
    command => 'sed -i "s/^ULIMIT=.*/ULIMIT=\"-n 4096\"/" /etc/default/nginx; sudo service nginx restart',
    path    => ['/bin', '/usr/bin', '/usr/sbin']
}
