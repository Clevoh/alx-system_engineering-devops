# Increase the amount of traffic nginx can handle

# Increase the ULIMIT to default value
exec { 'fix -- for nginx':
  # modify the ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # Specify the path for the sed command
  path    => ['/usr/local/bin/', '/bin/'],
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
}

exec { 'nginx_restart':
  # Restart nginx services,
  command => '/etc/init.d/nginx restart',
  # Specify the path for init.d command
  path    => ['/etc/init.d'],
  # Notify the Nginx service to restart when the exec runs
  notify  => Service['nginx'],
}
