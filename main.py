import numpy as np


class State(object):
    global sid
    sid = -1

    def __init__(self, label):
        global sid
        sid += 1
        self.sid = sid
        self.label = label
        self.inital = 0
        self.final = 0

    def setInital(self):
        self.inital = 1

    def setFinal(self):
        self.final = 1


class Transitions(object):
    def __init__(self, curr_sid, curr_label, value, to_sid, to_label):
        self.curr_sid = curr_sid
        self.curr_label = curr_label
        self.value = value
        self.to_sid = to_sid
        self.to_label = to_label


def main():
    print("[!] Lutfen alfabenizi ',' ile ayirarak giriniz. Ornegin a,b,c")
    sigma = input("> [+] Alfabe : ").split(',')

    sum_state = int(input("> [+] Kac adet state gireceksiniz : "))
    Q = {}
    for i in range(sum_state):
        label = input("> [+] State adini giriniz : ")
        Q.update({label: State(label)})

    while True:
        inital_state = input("> [+] Inital State : ")
        if inital_state in Q.keys():
            Q[inital_state].setInital()
            break
        else:
            print("[*] Belirtilen state bulunamadi.")

    while True:
        final_state = input("> [+] Final State : ")
        if final_state in Q.keys():
            Q[final_state].setFinal()
            break
        else:
            print("[*] Belirtilen state bulunamadi.")

    ro = {}
    print("[!] Lutfen belirtilen sekilde giriniz. Ornegin q0:a>q1")
    while True:
        transitions = input("> [+] Transitions(Cikis icin x) : ").split('>')
        if transitions[0] == 'x':
            break
        curr = transitions[0].split(':')[0]
        value = transitions[0].split(':')[1]
        to = transitions[1]
        if value not in sigma or curr not in Q.keys() or to not in Q.keys():
            print("[*] Girilen transition hatali lütfen kontrol ediniz.")
            continue
        if curr in ro.keys():
            ro[curr].append(Transitions(
                Q[curr].sid,
                Q[curr].label,
                value,
                Q[to].sid,
                Q[to].label))
        else:
            ro[curr] = [Transitions(
                Q[curr].sid,
                Q[curr].label,
                value,
                Q[to].sid,
                Q[to].label)]
    print(ro)

    matrix = {}
    for i in Q.keys():
        for si, j in enumerate(sigma):
            if i not in matrix.keys():
                matrix[i] = {j: []}
            else:
                matrix[i][j] = []


    """
    for i in Q.keys():
        for si, j in enumerate(sigma):
            for k in ro[i]:
                if k.value == j and i not in matrix.keys():
                    matrix[i] = [{k.to_label}]
                if k.value == j and i in matrix.keys():
                    matrix[i][0] |= {k.to_label}
    """

    """
    else:
        if new_state not in Q.keys():
            Q[new_state] = State(new_state)
    """
    print(matrix)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[.] Bye.. Bye...")
