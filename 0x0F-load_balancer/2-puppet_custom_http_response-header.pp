# install ngnix
$ruta = '/etc/nginx/nginx.conf'
$linea = "http {\n\tadd_header X-Served-By \"${hostname}\";"
$comando = '/usr/sbin/service nginx start'
exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}
package {'nginx':
         ensure => 'present',
         require => Exec['apt-get update'],
}
-> file_line { 'http_header':
  path  => $ruta,
  match => 'http {',
  line  => $linea,
}
->service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
-> exec {'run2':
  command => $comando,
}
