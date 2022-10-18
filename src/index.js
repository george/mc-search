const path = require('path')
const { app, BrowserWindow } = require('electron')

const createMainWindow = () => {
    const mainWindow = new BrowserWindow({
        width: 1200,
        height: 720,
    })

    mainWindow.setMenuBarVisibility(false)
    mainWindow.loadFile('./resources/views/index.html')
    mainWindow.setIcon('./resources/icon/logo.png')
}

app.whenReady().then(() => {
    createMainWindow()

    app.on('window-all-closed', () => {
        if (process.platform !== 'darwin') {
            app.quit()
        }
    })
})