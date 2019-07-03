import pexpect
import time

child = pexpect.spawn('bash')
child.expect(r'\$')
child.sendline('nohup omxplayer pin4info.mp4 --loop --aspect-mode stretch --no-osd')
time.sleep(17)
child = pexpect.spawn('bash')
child.expect(r'\$')
child.sendline('sudo killall /usr/bin/omxplayer.bin')
