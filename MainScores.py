import os

from Utils import SCORES_FILE_NAME
html_with_score = """<html>
<head>
    <title>Score Game</title>
</head>
<body>
            <h1>The score is <div id="score"> {SCORE}</div></h1>
</body>
</html> """

html_error = """ <html>        
<head>            
    <title>Scores Game</title>
</head>        
<body>        
<body>            
            <h1><div id="score" style="color:red">{ERROR}</div></h1>        
</body></html> """

def score_server():
    if not os.path.exists("./" + SCORES_FILE_NAME):
        return html_error
    score_file = open("./"+SCORES_FILE_NAME, "r")
    score = score_file.read()
    if score == "":
        return html_error
    return html_with_score.format(SCORE=score)
print(score_server())