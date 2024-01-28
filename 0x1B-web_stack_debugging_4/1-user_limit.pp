# Define a user with the name 'holberton'
user { 'holberton':
  ensure      => 'present',
  home        => '/home/holberton',
  managehome  => true,
}
