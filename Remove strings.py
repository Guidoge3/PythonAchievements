s = "Hallo ik ben een string en ik wordt opgegeten"

def eat_me(s):
    ss = s[0:len(s)-1]
    print(ss)
    if ss != "":
        eat_me(ss)
    
#pak alle characters in de string behalve de laatste en sla deze op in ss

eat_me(s)
