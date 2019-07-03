import pexpect
child = pexpect.spawn('bash')
child.expect(r'\$')
print('yay')
child.sendline('nohup feh --hide-pointer -x -q -F /home/pi/default.png')
print('done here')
