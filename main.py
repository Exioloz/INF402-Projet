import sys
from futoshiki import Futoshiki
import logic
import pysat

file_to_load = sys.argv[0]
game = Futoshiki(file_to_load)

print("Game debug")
for i in game:
	print(i)
print(f'{game.inequality=}', end="\n\n")

rule_1 = logic.rule_1(game)
print("Rule 1")
print(rule_1, end="\n\n")

rule_2 = logic.rule_2(game)
print("Rule 2")
print(rule_2, end="\n\n")

rule_3 = logic.rule_3(game)
print("Rule 3")
print(rule_3, end="\n\n")

rule_4 = logic.rule_4(game)
print("Rule 4")
print(rule_4, end="\n\n")

rule_5 = logic.rule_5(game)
print("Rule 5")
print(rule_5, end="\n\n")

rule_6 = logic.rule_6(game)
print("Rule 6")
print(rule_6, end="\n\n")

logic.create_cnf(f"out/{file_to_load}.cnf", game.side, rule_1, rule_2, rule_3, rule_4, rule_5, rule_6)
