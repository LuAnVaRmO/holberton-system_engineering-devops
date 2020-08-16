# create task 0 but with puppet
exec {'update':
	command => 'sudo apt-get update',
	provider => shell,
}

package {'nginx':
	ensure => installed,
	require => Exec['update'],
}

file_line {'header'
	ensure => present,
	path => '/etc/nginx/sites-available/default',
	after => 'listen 80 default_server',
	line => "add header X-Served_By ${hostname};",
	require => Package['nginx'],
}

service {'nginx':
	ensure => running,
	require => File_line['header'],
}
