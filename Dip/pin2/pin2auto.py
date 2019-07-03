import pexpect
child = pexpect.spawn('bash')
child.expect(r'\$')
child.sendline('nohup feh kayleec.png -Z -F -x')
child2 = pexpect.spawn('bash')
child2.expect(r'\$')
child2.sendline('nohup omxplayer kaylee.mp4 --loop --aspect-mode stretch --no-osd')
