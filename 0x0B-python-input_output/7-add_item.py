#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1:]
args_list = []

if args:
    args_list.extend(args)

try:
    list = load_from_json_file("add_item.json")
    list.extend(args_list)
    save_to_json_file(list, "add_item.json")

except FileNotFoundError:
    save_to_json_file(args_list, "add_item.json")
