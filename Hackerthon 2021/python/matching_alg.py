"""
Matching algorithm built for ReadyPlayerTwo hackerthon

__author__ = "Philip Wen Wei Ooi"
__last_modified__ = 17.07.2022
"""


import store_from_txt
import random

x = store_from_txt.txt_categories('test_txt.txt')
y = store_from_txt.txt_categories('test_txt2.txt')
z = store_from_txt.txt_categories('test_txt3.txt')
lst = [x,y,z]

def game_matches(lst,game):
    """
    Input: Array of user data and a game in the form of string 
    Output: The users that match in game

    Example:
    game_matches(lst,'Overwatch')
    >>> [[['@Arocien Zeldorith'], ['Philip'], ['Ooi'], ['League of legends', 'Overwatch'], ['Interests'], ['Dislikes'], ['Competitive'], ['Skill level']], 
    [['@Sorry Nerds'], ['Sam'], ['Chaw'], ['Overwatch', 'World Of Warcraft'], ['Interests'], ['Dislikes'], ['Competitive'], ['Skill level']], 
    [['@burnz'], ['Ethan'], ['Ng'], ['Minecraft', 'Overwatch', 'World Of Warcraft'], ['Interests'], ['Dislikes'], ['Competitive'], ['Skill level']]]
    """
    game_lst = []
    matches = []
    profiles = []
    for i in range(len(lst)):
        game_lst.append(lst[i][3])
    for j in range(len(game_lst)):
        for k in range(len(game_lst[j])):
            if game_lst[j][k] == game:
                matches.append(j)
    for k in matches:
        profiles.append(lst[k])
    return profiles

    
def comp_match(matches,choice):
    """
    Input: List of matched profiles by game and a choice of either competitive or casual in a string
    Output:The index of the profiles that match the choice
    Example:
    comp_match(Match,'Competitive')
    >>>[0, 1, 2]
    comp_match(Match, 'Casual')
    >>>No matches found
    """
    comp_lst = []
    comp_pick = []
    error = "No matches found"
    for i in range(len(matches)):
        comp_lst.append(lst[i][6])
    for j in range(len(comp_lst)):
        if comp_lst[j] == [choice]:
            comp_pick.append(j)
    if len(comp_pick) <= 1:
        return error
    else:
        return comp_pick
    pass

def rand_pick(lst):
    r1 = random.randint(0,len(lst))
    return r1
    pass


match = game_matches(lst,'Overwatch')
pref = comp_match(match,'Competitive')
rand_match = rand_pick(pref)
print (pref)
print(rand_match)
