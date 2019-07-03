import pexpect
child = pexpect.spawn('bash')
child.expect(r'\$')
child.sendline('sudo killall /usr/bin/omxplayer.bin')
child.expect(r'\$')
child.sendline('nohup omxplayer 1.mp4 --loop --aspect-mode stretch --no-osd')
