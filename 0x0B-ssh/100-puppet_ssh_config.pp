# set up ssh config file for connect to a server without typing a password
exec { 'identity':
  command  => 'echo IdentityFile ~/.ssh/holberton >> /etc/ssh/ssh_config',
  provider => 'shell',
  path     => '/usr/bin/',
}
exec { 'no_password':
  command  => 'echo PasswordAuthentication no >> /etc/ssh/ssh_config',
  provider => 'shell',
  path     => '/usr/bin/',
}
