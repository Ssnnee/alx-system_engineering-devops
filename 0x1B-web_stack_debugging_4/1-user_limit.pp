# Define a user with the name 'holberton'
user { 'create_holberton':
  ensure      => 'present',
  home        => '/home/holberton',
  managehome  => true,
}
