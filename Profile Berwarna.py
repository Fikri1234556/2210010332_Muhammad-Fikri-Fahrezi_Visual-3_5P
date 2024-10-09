import PySimpleGUI as sg
sg.theme("LightGreen8")
sg.theme_text_color("#00ffff")
windos = sg.Window('Profile Berwarna', 
    [[sg.Text('NPM :2210010332'),],
        [sg.Text('Nama :Muhammad Fikri Fahrezi')], 
        [sg.Text('kelas :5P reguler Banjarmasin')],
        [sg.Text('matkul : pempgraman Visual')],
    ],size=(500,200)).read(close=True)
event, values=window.read()
window.close()