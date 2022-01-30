import re
import pyfiglet
from termcolor import cprint
# ======================== *** ========================

message = pyfiglet.figlet_format("SCRIPT")
sm= pyfiglet.figlet_format("success")
cprint(message, 'green')
# ====================user input =======================
cprint('Enter the file path \n', 'red')
file_path = input()
script=''
with open(file_path) as file:
    script = ''.join(file.readlines())
# =====================user input ======================





p = re.compile('((join|from)[ |\n]+)("?[a-z_0-9]+"?)\.("?[a-z_0-9]+"?)\.("?[a-z_0-9]+"?)', re.IGNORECASE)


script = '''hello join "skDa_lkfds"."dsakjj"."dflFFksafd"
join  "sdfk9j".dlkjsdf.ldjkfsd
join  
sdfkj.dlkjsdf.ldjkfsd

join  


sdf0kj.dlkjsdf.ldjkfsd



From  "dkd"."ds"."dsk"
from dfkd.dkfjs.dsksfdlj
hello end string'''
# res = p.findall(script)
# res = p.sub('$$$$', script)
new_script = ''
st = 0
# print(script)
for m in p.finditer(script):
    # print(m)
    # print(m.span()[0])
    # print(script[m.span()[0]:m.span()[1]])
    # print(m.groups())
    # print(f"${script[m.start():(m.start()+len(m.groups()[0]))]}$")
    start_index = m.start()+len(m.groups()[0])
    end_index = m.end()
    database = m.groups()[2]
    schema = (m.groups()[3]).strip('"')
    table = (m.groups()[4]).strip('"')
    jinja_style = f"{{{{source('{schema}', '{table}')}}}}"
    # print(jinja_style)
    new_script +=script[st:start_index]+jinja_style
    st = end_index
new_script+=script[st:]

# print("===============new script===============")
# print(new_script)


parts = file_path.split('.')
new_file_path = parts[0]+"__output."+parts[1]
with open(new_file_path, mode='w') as file:
    file.write(new_script)
    cprint(sm, 'green')
    cprint(f"file writen to: {new_file_path}", 'green')