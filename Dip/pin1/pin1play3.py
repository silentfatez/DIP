import pexpect
import time

child = pexpect.spawn('bash')
child.expect(r'\$')
child.sendline('sudo killall /usr/bin/omxplayer.bin')
child.expect(r'\$')
child.sendline('nohup omxplayer chenggong.mp4 --loop --aspect-mode stretch --no-osd')
time.sleep(11.5)
child = pexpect.spawn('bash')
child.expect(r'\$')
child.sendline('sudo killall /usr/bin/omxplayer.bin')
child.expect(r'\$')
child.sendline('nohup omxplayer ruoyao.mp4 --loop --aspect-mode stretch --no-osd')
