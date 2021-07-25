from frontend import Main
from backend import PathHolder

if __name__ == '__main__':
    PathHolder.getPath()
    main = Main()
    main.run()
