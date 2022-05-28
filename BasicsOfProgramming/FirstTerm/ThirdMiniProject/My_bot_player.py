#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

from random import randrange
from logging import DEBUG, debug, getLogger

getLogger().setLevel(DEBUG)

def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    return 1 if "p1 :" in i else 2

def analiz_size():
    """
    Analizes the sizes of the map and of the figure
    """
    str_m = input()[:-1]
    height_m = int(str_m.split()[1])
    width_m = int(str_m.split()[2])
    return height_m, width_m

def matrics_the_board(hei):
    """
    Makes the matrics (list of list) of the situation on the board

    """
    board_sit_array = []
    del_row = input()
    for one_row in range(hei):
        one_row = input()
        temp_lst = []
        for ellem in one_row[4:]:
            temp_lst.append(ellem)
        board_sit_array.append(temp_lst)
    return board_sit_array

def distance_between_2p(poi1, poi2):
    """
    Counts the distance between the two coordinates
    """
    return math.sqrt(((poi1[0]-poi2[0])**2)+((poi1[1]-poi2[1])**2))

def matrics_the_figure(hei):
    """
    Makes the matrics (list of list) of the figure
    """
    figure_array = []
    for one_row in range(hei):
        one_row = input()
        temp_lst = []
        for ellem in one_row:
            temp_lst.append(ellem)
        figure_array.append(temp_lst)
    return figure_array


def slice_the_board(hei_m, wid_m, hei_f, wid_f, board_matr):
    """
    Slices the board on all possible slice which have the the same size as the figure
    """
    las_wid = wid_m-(wid_f-1)
    las_hei = hei_m-(hei_f-1)
    list_opt = []
    for heigg in range(0, las_hei):
        for widd in range(0, las_wid):
            coo_lst = [heigg, widd]
            slic_matrics = []
            for sublist in board_matr[heigg:(heigg + hei_f)]:
                slic_matrics.append(sublist[widd:(widd + wid_f)])
            tuup = (coo_lst, slic_matrics)
            list_opt.append(tuup)
    return list_opt

def analiz_options(fi_mat, lst_opt, hei_f, wid_f, plar):
    """
    From all possible moves chooses the good ones
    """
    res_lst = []
    if plar == 1:
        good_el = "O"
        bad_el = "X"
    else:
        good_el = "X"
        bad_el = "O"
    for tuuup in lst_opt:
        com_lst = tuuup[1]
        points=0
        for heeig in range(0, hei_f):
            for wiiid in range(0, wid_f):
                el_op = com_lst[heeig][wiiid]
                el_fi = fi_mat[heeig][wiiid]
                if el_fi == "*" and el_op.upper() == good_el:
                    points += 1
                elif el_fi == "*" and el_op.upper() == bad_el:
                    points += 2
                else:
                    None
        if points == 1:
            res_lst.append(tuple(tuuup[0]))
    return res_lst


def analiz_best_move(board_mat, player, glist_moves):
    """
    From all good moves chooses the best

    """
    if player == 1:
        enemy = "X"
    elif player == 2:
        enemy = "O"
    all_enemy_coord = []
    for line in board_mat:
        if enemy in line:
            enemy_position=(board_mat.index(line), line.index(enemy))
            all_enemy_coord.append(enemy_position)
    moves_tup = []
    for moves in glist_moves:
        for pos in all_enemy_coord:
            dist = distance_between_2p(moves, pos)
            tupll = (moves, dist)
            moves_tup.append(tupll)
    sorted_m_tupl = sorted(moves_tup, key=lambda x: x[1])
    if len(sorted_m_tupl)>=1:
        best_t = sorted_m_tupl[0]
        b_move = best_t[0]
    else:
        b_move = None
    return b_move


def work_with_one_step(player):
    """
    Analizes the one step and returns the different lists of options
    """
    height_m, width_m = analiz_size()
    board_mat = matrics_the_board(height_m)
    height_f, width_f = analiz_size()
    figure_mat = matrics_the_figure(height_f)
    list_of_all_options = slice_the_board(height_m, width_m, height_f, width_f, board_mat)
    list_of_good_options = analiz_options(figure_mat, list_of_all_options, height_f, width_f, player)
    list_of_bad_options = [item for item in list_of_all_options if item not in list_of_good_options]
    best_move = analiz_best_move(board_mat, player, list_of_good_options)
    return list_of_good_options, list_of_bad_options, best_move


def play(player: int):
    """
    Main game loop. Where we choose the move

    """
    while True:
        glist_moves, blist_moves, best_move = work_with_one_step(player)
        if len(glist_moves)<1:
            ran_in = randrange(len(blist_moves))
            move = blist_moves[ran_in]
        elif best_move != None:
            move = best_move
        else:
            ran_in = randrange(len(blist_moves))
            move = blist_moves[ran_in]
        print(*move)


def main():
    """
    Main function which starts the player
    """
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input.py. Seems that we've lost ):")


if __name__ == "__main__":
    main()
