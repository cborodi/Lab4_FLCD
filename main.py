

class FiniteAutomata:
    def readFile(self, fileName):
        with open(fileName) as file:
            line = file.readline()
            Q = []
            line_slice = line[3:-2]
            for e in line_slice.split(","):
                Q.append(e)
            line = file.readline()
            E = []
            line_slice = line[3:-2]
            for e in line_slice.split(","):
                E.append(e)
            line = file.readline()
            f = []
            line_slice = line[3:-2]
            for e in line_slice.split(";"):
                f.append(e)
            line = file.readline()
            q0 = line[3:-1]
            line = file.readline()
            F = []
            line_slice = line[3:-1]
            for e in line_slice.split(","):
                F.append(e)
            return Q, E, f, q0, F

fa = FiniteAutomata()
Q, E, f, q0, F = fa.readFile("FA.in")
print("======================================================")
print("Finite set of states> ")
print(Q)
print("Finite alphabet> ")
print(E)
print("Transition function> ")
print(f)
print("Initial state> ")
print(q0)
print("Final states> ")
print(F)
print("======================================================")
