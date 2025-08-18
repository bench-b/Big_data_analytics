import webbrowser
import os

#dispay map
def showMap(map):
    map.save("map.html")
    filepath = os.getcwd()
    file_url = 'file:///' + filepath + '/map.html'
    webbrowser.open_new_tab(file_url)