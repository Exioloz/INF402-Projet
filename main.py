import sys
from futoshiki import Futoshiki
import logic
import sat

file_to_load = sys.argv[1]  # Name of the futoshiki file
game = Futoshiki("Futoshiki_in/" + file_to_load)  # Converting the .futoshiki file to data

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

print("")
cnf_file = f"CNF_out/{file_to_load}.cnf"
sat_file = f"SAT_out/{file_to_load}.sat"
sat_out = open(sat_file, "w")
# Using the CNF created file and SAT-solve it
sat_solution = sat.sat_solve(cnf_file, sat_out)
sat_out.close()

file_futoshiki = open("Futoshiki_in/" + file_to_load, "r")
futoshiki_in = file_futoshiki.read()
# Creating a list of integer of the solution using the size of the puzzle and SAT-solved list of booleans
solution = sat.resolution(int(futoshiki_in[0]), sat_solution)
file_futoshiki.close()

futoshiki_out = open("Futoshiki_out/" + file_to_load, "w")
# Making a solved Futoshiki based of the one given to the program using the solution
sat.create_solution(futoshiki_in, futoshiki_out, solution)
futoshiki_out.close()
