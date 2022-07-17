import sys
import matching_alg
#array will be [file,game,choice,lst]
fil_game = matching_alg.game_matches(sys.argv[3],sys.argv[1])
fil_choice = matching_alg.comp_match(fil_game,sys.argv[2])
fil_rand = matching_alg.rand_pick(fil_choice)
lst = sys.argv[3]
print(lst[fil_rand])
pass


