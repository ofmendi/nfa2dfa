import operator
import pprint


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

    while True:
        try:
            sum_state = int(input("> [+] Kac adet state gireceksiniz : "))
            if sum_state < 1:
                raise ValueError()
            else:
                break
        except ValueError:
            print("[!] Lutfen pozitif bir dogal sayi giriniz.")

    Q = {}
    while True:
        try:
            for i in range(sum_state):
                label = input("> [+] State adini giriniz : ")
                if not label:
                    raise ValueError()
                Q.update({label: State(label)})
            else:
                break
        except ValueError:
            print("[!] Lutfen state adini giriniz.")

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
        try:
            transitions = input("> [+] Transitions(Cikis icin x) : ").split('>')
            if transitions[0] == 'x':
                break
            curr = transitions[0].split(':')[0]
            value = transitions[0].split(':')[1]
            to = transitions[1]
            if value not in sigma or curr not in Q.keys() or to not in Q.keys():
                print("[*] Girilen transition hatali lutfen kontrol ediniz.")
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
        except Exception as e:
            print("[!] Hata : ", e)

    matrix = {}
    for i in Q.keys():
        for j in sigma:
            if i not in matrix.keys():
                matrix[i] = {j: []}
            else:
                matrix[i][j] = []
    new_states = []
    for key, lis in sorted(ro.items(), key=operator.itemgetter(0)):
        for value in lis:
            for s in sigma:
                if value.value == s:
                    matrix[key][s].append(value.to_label)
                    nstate = ','.join(sorted(matrix[key][s]))
                    if nstate not in matrix.keys():
                        new_states.append(nstate)
    else:
        for i in new_states:
            if i not in matrix.keys():
                matrix[i] = {}
                for nsig in sigma:
                    tmp = i.split(',')
                    tmp2 = set()
                    for t in tmp:
                        tmp2 |= set(matrix[t][nsig])
                    tmp2 = sorted(list(tmp2))
                    matrix[i][nsig] = tmp2
                    if ','.join(tmp2) not in matrix.keys():
                        new_states.append(','.join(tmp2))

    pprint.pprint(matrix)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[.] Bye.. Bye...")
