# Execute pkill command

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
