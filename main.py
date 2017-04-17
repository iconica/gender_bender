#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

from gender_bender import gender_bend_epub


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True,
                        help='Path of epub to gender bend')
    parser.add_argument('-o', '--output', type=str, required=False,
                        help='Path of epub to gender bend')
    args = parser.parse_args()

    gender_bend_epub(args.input, args.output)