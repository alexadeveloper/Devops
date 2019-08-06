#make changes to our configuration file
file { '/etc/ssh/ssh_config':
  ensure => present
}->
file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  ensure => present,
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}->
file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  ensure => present,
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => '^IdentityFile',
}
