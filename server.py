from flask import Flask
import random

run_num = random.randrange(1,10)
        
def random_int_detector(func):
    def decorator(*args, **kwargs):   
        if kwargs['n'] < run_num:
             return"<h1>Higher</h1><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2JpdHYzNDJmcHJ0MHBsaGd6MGYxbmQyM3puZjlocWV5Yjg0dHZyZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/iZGpuaRKdEZoI/giphy.gif' alt='a ufc boxer' width='500' height='500'>"
        if kwargs['n'] > run_num:
            return"<h1>Lower</h1><img src='https://media.giphy.com/media/wyyd8d9IPry3qOBW4W/giphy.gif?cid=790b76117zeik6ljp5mjesr7gxbx5kesjgnu900xl2piko3u&ep=v1_gifs_search&rid=giphy.gif&ct=g' alt='a ufc boxer' width='500' height='500'>"
        else:
            return"<h1>good job</h1><img src='https://media.giphy.com/media/mGK1g88HZRa2FlKGbz/giphy.gif?cid=790b7611lllt7xqnlr35r1avbpwatnkdet33n4umknbvf6z0&ep=v1_gifs_search&rid=giphy.gif&ct=g' alt='a ufc boxer' width='500' height='500'>"
        
    return decorator


app = Flask(__name__)

@app.route("/", endpoint = '0')
def guess():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGxvZzk3N2lxeDFkOGRsbW9nemdvdHZpc3R6bTg5c2V3d2drbGlyMiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/569C9AVb7uPEHXGOLk/giphy.gif' alt='a ufc boxer' width='500' height='500'>"

for n in range(1,10):
    @app.route("/<int:n>", endpoint =f"{str(n)}")
    @random_int_detector
    def guess(n):
        pass

if __name__ == "__main__":
    app.run(debug=True)