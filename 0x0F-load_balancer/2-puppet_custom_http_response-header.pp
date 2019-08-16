# install ngnix
ruta = '/etc/nginx/nginx.conf'
linea = "http {\n\tadd_header X-Served-By \"${hostname}\";"
comando = '/usr/sbin/service nginx start'
package {'nginx':
         ensure => 'present',
}
-> file_line { 'http_header':
  path  => $ruta,
  match => 'http {',
  line  => $linea,
}
-> exec {'run2':
  command => $comando,
}
