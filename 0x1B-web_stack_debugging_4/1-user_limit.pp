# make changes the limit
exec { 'replace hard':
  cwd     => '/etc/security/',
  command => 'sed -i -e s/holberton hard nofile 5/holberton hard nofile 2048/g limits.conf',
  path    => ['/bin','/usr/bin','/usr/sbin'],
}->
exec { 'replace soft':
  cwd     => '/etc/security/',
  command => 'sed -i -e s/holberton soft nofile 4/holberton soft nofile 2048/g limits.conf',
  path    => ['/bin','/usr/bin','/usr/sbin'],
}->
exec { 'restart':
  command => 'sudo sysctl -p',
  path    => ['/usr/bin', '/usr/sbin','/bin'],
}
