import pexpect
child = pexpect.spawn('bash')
child.expect(r'\$')
child.sendline('nohup feh displaypic.png -Z -F -x')
