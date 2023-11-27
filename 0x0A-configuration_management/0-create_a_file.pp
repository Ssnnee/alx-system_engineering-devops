# Creates a file with the specified  owner, group, mode and content.

file { '/tmp/school':
  owner   => 'www.data',
  group   => 'www.data',
  mode    => '0744',
  content => 'I love Puppet',
}
