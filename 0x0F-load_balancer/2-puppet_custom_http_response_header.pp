# 2-puppet_custom_http_response_header.pp
# task2

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Add custom HTTP header to Nginx configuration
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "add_header X-Served-By ${hostname};\n",
  notify  => Service['nginx'],
}

# Create a simple index page
file { '/usr/share/nginx/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
  notify  => Service['nginx'],
}
