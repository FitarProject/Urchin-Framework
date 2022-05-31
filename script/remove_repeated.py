#!/usr/bin/env python3
# -*- coding=utf-8 -*-


def deal_data(input_1=any):
###########################上面不要动###########################
    filename = input_1
    with open(filename, "r") as f1:
        lines = f1.readlines()
        list_tmp = {}.fromkeys(lines).keys()
    output_1 = list_tmp

###########################下面不要动###########################
    return output_1
