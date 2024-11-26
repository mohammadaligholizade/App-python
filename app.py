# pip install eel
import eel

ell.init('Gui') # folder name

@eel.expose
def App():  # app main funcition
    print('App is a running')

App()

eel.start('index.html', size=(500,600)) # run app window
