import dis

python_file = open('demo.py').read()
code = compile(python_file, 'demo.py', 'exec')
dis.dis(code)