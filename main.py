import sys
from futoshiki import Futoshiki
import logic
import sat

file_to_load = sys.argv[1]
game = Futoshiki("Futoshiki_in/" + file_to_load)

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

logic.create_cnf(f"CNF_out/{file_to_load}.cnf", game.side, rule_1, rule_2, rule_3, rule_4, rule_5, rule_6)

# WIP
# Use SAT file to make a finished futoshiki grid
# TODO
cnf_file = f"CNF_out/{file_to_load}.cnf"
sat.sat_solve(cnf_file, f"SAT_out/{file_to_load}.sat")

sat_file = f"SAT_out/{file_to_load}.sat"
file_futoshiki = open("Futoshiki_in/" + file_to_load, "r")
futoshiki = file_futoshiki.read()
size = int(futoshiki[0])
solution = sat.resolution(size, sat_file)

sat.create_solution("Futoshiki_in/" + file_to_load, "Futoshiki_in/" + file_to_load, solution)
