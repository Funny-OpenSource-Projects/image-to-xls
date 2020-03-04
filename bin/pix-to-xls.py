#!/usr/bin/env python


import argparse
from pix_to_xls import builder

CLI_DESC = "A simple tool to make ascii art from an image using excel colored cells"
EPILOG = ("\033[1;37mThanks for trying pix-to-xls!\033[0m")

PARSER = argparse.ArgumentParser(prog='pix-to-xls', description=CLI_DESC, epilog=EPILOG)
PARSER.add_argument('input_file', type=str, help='input file') 
PARSER.add_argument('output_file', type=str, help='output file')
PARSER.add_argument('-c', '--cols', type=int, default=50, dest='cols', help='cells per row', action='store')


ARGS = PARSER.parse_args()

builder.build(ARGS.input_file, ARGS.output_file, ARGS.cols)
