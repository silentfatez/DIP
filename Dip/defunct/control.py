import pexpect
import time

def control1():
    print('1 inputted')
    child = pexpect.spawn('bash')
    child.expect(r'\$')
    child.sendline('ssh 192.168.43.233')
    child.expect(r'password')
    child.sendline('Dreams97')
    child.expect(r'\$')
    child.sendline('nohup python3 pin2playvid.py')
    time.sleep(1)
    child2 = pexpect.spawn('bash')
    child2.expect(r'\$')
    child2.sendline('nohup python3 pin1play2.py')
def control2():
    print('2 inputted')
    child = pexpect.spawn('bash')
    child.expect(r'\$')
    child.sendline('ssh 192.168.43.58')
    child.expect(r'\$')
    child.sendline('Dreams97')
    child.expect(r'\$')
    child.sendline('python3 pin4playvid.py')
    time.sleep(1)
    child2 = pexpect.spawn('bash')
    child2.expect(r'\$')
    child2.sendline('python3 pin1play4.py')
def control3():
    print('3 inputted')
    child2 = pexpect.spawn('bash')
    child2.expect(r'\$')
    child2.sendline('python3 pin1play3.py')
    print(child2.read())

while True:
    answer=input('Type the number for input here:')
    if answer=='1':
        control1()
    elif answer=='2':
        control2()
    elif answer=='3':
        control3()
    else:
        print('wrong input only numbers from 1 to 3')
