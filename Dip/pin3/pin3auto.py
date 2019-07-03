import pexpect
child = pexpect.spawn('bash')
child.expect(r'\$')
child.sendline('nohup feh gao.png -Z -F -x')
child2 = pexpect.spawn('bash')
child2.expect(r'\$')
child2.sendline('nohup omxplayer tallsky.mp4 --loop --aspect-mode stretch --no-osd')
