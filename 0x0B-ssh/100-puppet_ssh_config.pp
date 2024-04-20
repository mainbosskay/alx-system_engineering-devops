# Puppet to make changes to our configuration file
exec { 'Configure SSH sethings':
  command => 'bash -c "echo PasswordAuthentication no >> /etc/ssh/ssh_config && echo IdentityFile \'~/.ssh/school\' >> /etc/ssh/ssh_config && echo PubkeyAuthentication yes >> /etc/ssh/ssh_config"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
