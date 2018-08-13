#!usr/bin/python3

from argparse import ArgumentParser
import logging

#my imports
import formatmessages

def parsing():
    """Parsing the arguments"""
    parser = ArgumentParser(description="Whatsapp chat analyser")
    parser.add_argument("-v", "--verbose", help="print output and log", 
        action="store_true", default=False)        
    return parser.parse_args()

def main():
    args = parsing()

if __name__ == '__main__':
    main()