class KMP:

    def __init__(self, P, T):
        self.T = T
        self.P = P

        self.pi = [None for _ in range(len(P))]

        self.shifts = []

        self.comp = 0

    def get_shifts(self):

        self.construct_P()

        q = -1
        i = 0
        while(i < len(self.T)):
            
            while(q > -1 and self.P[q + 1] != self.T[i]):
                q = self.pi[q]
                self.comp += 1

            if(self.P[q + 1] == self.T[i]):
                q += 1

            self.comp += 1

            if(q == len(self.P) - 1):
                self.shifts.append(i - len(self.P) + 1)
            
                q = self.pi[q]
            
            i += 1

        return self.shifts, self.comp


    def construct_P(self):
        
        self.pi[0] = -1
        k = -1
        q = 1
        while(q < len(self.P)):

            while(k > -1 and self.P[k + 1] != self.P[q]):    
                k = self.pi[k]

            if(self.P[k + 1] == self.P[q]):
                k += 1

            self.pi[q] = k

            q += 1

def main():
    
    P = input("Enter the pattern : ")
    T = input("Enter text : ")
    obj = KMP(P, T)
    shifts, comp = obj.get_shifts()

    print()
    print("Pattern found at indices : ", end="")
    i = 0
    while(i < len(shifts)):
        
        print(shifts[i], end="")

        if(i != len(shifts) - 1):
            print(", ", end="")
        
        i += 1
    
    print()
    print(f"No. of comparisons : {comp}")

if(__name__ == "__main__"):
    print()
    main()
    print()