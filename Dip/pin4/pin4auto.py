import pexpect
child = pexpect.spawn('bash')
child.expect(r'\$')
child.sendline('nohup feh black.png -Z -F -x')
