const { app, BrowserWindow } = require('electron')
const isDev = require('electron-is-dev');

let mainWindow;

const createMainWindow = () => {
    mainWindow = new BrowserWindow({
        width: 1200,
        height: 720,
    })

    //Disable menu bar
    mainWindow.setMenuBarVisibility(false)

    //Load HTML file into the window
    mainWindow.loadFile('./resources/views/index.html')

    //Set the icon for development build
    mainWindow.setIcon('./resources/icon/logo.png')

    //When the main window is closed, quit the application
    mainWindow.on('closed', () => {
        app.quit()
    })
}

app.whenReady().then(() => {
    createMainWindow()
})