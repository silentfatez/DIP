import pexpect
import time
child = pexpect.spawn('bash')
child.expect('root')
child.sendline('ssh 192.168.43.126')
child.expect('root')
child.sendline('Dreams97')
child.expect('root')
child.sendline('nohup omxplayer /home/pi/21.mp4')
time.sleep(1)
child2 = pexpect.spawn('bash')
child2.expect('root')
child2.sendline('nohup omxplayer 12.mp4')
