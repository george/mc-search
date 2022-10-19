const { app, ipcMain, BrowserWindow } = require('electron')
const axios = require('axios')
const isDev = require('electron-is-dev')

let mainWindow
let lastResponse

const createMainWindow = () => {
    mainWindow = new BrowserWindow({
        width: 1200,
        height: 720,

        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        }
    })

    //Disable menu bar
    mainWindow.setMenuBarVisibility(false)

    //Load HTML file into the window
    mainWindow.loadFile('./resources/views/index.html')

    //When the main window is closed, quit the application
    mainWindow.on('closed', () => {
        app.quit()
    })
}

ipcMain.on('search', (event, query) => {
    mainWindow.loadFile('./resources/views/loading.html')

    axios.get((isDev ? 'http://127.0.0.1:3000' : 'https://api.hostile.org') + '/data/' + query)
        .then(response => {
            lastResponse = response.data
        })
})

app.whenReady().then(() => {
    createMainWindow()
})