# Change the extension of php to phpp in wp-settings.php

exec { 'change-extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
