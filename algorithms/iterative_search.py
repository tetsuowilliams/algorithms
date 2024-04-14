# Naiive search using iterative approach o(n)

class IterativeSearch:
    def name(self):
        return "Iterative Search"

    def search(self, data, target):
        for i in range(len(data) - 1):
            if target == data[i]:
                return i
            