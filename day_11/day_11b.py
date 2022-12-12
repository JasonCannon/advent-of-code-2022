import sys, re, math
from dataclasses import dataclass

pattern = "Monkey (\d+):\n  Starting items: (\d+[, \d+]*)\n  Operation: new = (.*)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)"
L = re.findall(pattern, sys.stdin.read())

@dataclass
class Monkey:
    idx: int
    Items: list
    op: str
    div: int
    throw_t: int
    throw_f: int
    cnt: int = 0

    def convert(self):
        self.Items = [[I % P for P in Primes] for I in self.Items]

    def turn(self):
        self.cnt += len(self.Items)
        for I in self.Items:
            Item = [(eval(self.op)) % Primes[i] for i, old in enumerate(I)]
            Monkeys[self.throw_t if Item[self.idx] % self.div == 0 else self.throw_f].Items.append(Item)
        self.Items = []

Monkeys = [Monkey(int(i), list(map(int, I.split(','))), op, int(div), int(tt), int(tf)) for i, I, op, div, tt, tf in L]
Primes = [M.div for M in Monkeys]

for M in Monkeys: M.convert()

for i in range(10000): 
    for M in Monkeys: M.turn()

print(math.prod(sorted([M.cnt for M in Monkeys])[-2:]))