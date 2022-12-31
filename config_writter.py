from configparser import ConfigParser
fhfhhfh

config = ConfigParser()

config["Window"] = {
    'geometry': '650x350+300+200'
}
config['Font'] = {
    'family': 'Consolas',
    'weight': 'normal',
    'slant': 'roman',
    'size': '14'
}
config['Colors'] = {
    'background': '#7f8c8d',
    'foreground': '#ffffff',
    'selectbackground': '#e67e22',
    'selectforeground': '#ffffff'
}
config['AutoSave'] = {
    'state': False,
    'interval': 2000
}
config['DefaultFont'] = {
    'family': 'Consolas',
    'weight': 'normal',
    'slant': 'roman',
    'size': '14'
}
config['DefaultColors'] = {
    'background': '#7f8c8d',
    'foreground': '#ffffff',
    'selectbackground': '#e67e22',
    'selectforeground': '#ffffff'
}

with open('config.ini', 'w') as file:
    config.write(file)