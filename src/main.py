import sys
sys.path.append("..")

from GUI.Windows.launchWindow import LaunchWindow
from GUI.Windows.signInWindow import SignInWindow
from GUI.Windows.logInWindow import LogInWindow
from GUI.Windows.mainWindow import MainWindow

from Handler.windows import WindowManager
from Handler.setup import SetUp

class Launch():

    def __init__(self):

        self.windowManager = WindowManager()
        self.windowManager.addWindow(LaunchWindow)
        self.windowManager.addWindow(LogInWindow)
        self.windowManager.addWindow(SignInWindow)
        self.windowManager.addWindow(MainWindow)

        self.launch = SetUp()
        self.launch.WindowManager = self.windowManager
        self.launch.timer.timeout.connect(self.launch.chooseConnection)
        self.launch.timer.start(3000)

        self.windowManager.run()


if __name__ == "__main__":
    Launch()


