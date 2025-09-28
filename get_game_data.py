import os 
import json
import shutil
from subprocess import PIPE, run
import sys


GAME_DIR_PATTERN = "game"

'''Look all the files and directories and then match any directories that have this game in them'''
def find_all_game_paths(source): 
    game_paths = []
    for root, dirs, files in os.walk(source):  # walk recursively through whatever the source directory is we pass the walk command
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.joing(source, directory)
                game_paths.append(path)
                
        break
    
def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)   # join better than string concatenation
    target_path = os.path.join(cwd, target)
    
    game_paths = find_all_game_paths(source_path)
    print(game_paths)
    
    
# Find all game directories from /data
if __name__ == "__main__": 
    args = sys.argv 
    print(args)
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")
    
    source, target = args[1:]
    main(source,target)