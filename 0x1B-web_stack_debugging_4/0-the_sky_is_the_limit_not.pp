#make changes the limit
exec { 'replace':
  cwd     => '/etc/default/',
  command => 'sed -i -e s/15/2048/g nginx',
  path    => ['/bin','/usr/bin','/usr/sbin'],
}->
exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/usr/sbin','/bin'],
}
