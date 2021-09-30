# puppet code that fixes a wordpress site running on apache2
exec { 'fix':
  command  => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  provider => 'shell',
  path     => '/bin/',
}
