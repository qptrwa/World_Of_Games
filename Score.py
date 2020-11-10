from Utils import SCORES_FILE_NAME
import os

def add_score(difficulty):
    points_of_winning = (difficulty*3) + 5
    base_points = 0
    if os.path.exists("./"+SCORES_FILE_NAME):
        f = open("./"+SCORES_FILE_NAME, "r")
        content_of_file = f.read()
        if content_of_file != "" :
            base_points = int(content_of_file)
        f.close()
    f = open("./"+SCORES_FILE_NAME, "w")
    tot_points = base_points + points_of_winning
    f.write(str(tot_points))
    f.close()