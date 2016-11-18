import urllib.request

santa = Actor('santa')

WIDTH = 800
HEIGHT = 400

def draw():
    screen.blit('map',(0,0))
    santa.draw()

def santa_loc(c_day, c_hour, c_minute):
    if c_day == 24:
        location1 = (WIDTH/27)*(c_hour - 10)
        location2 = ((WIDTH/27)/60)*(c_minute)
    else:
        location1 = (WIDTH/27)*(c_hour + 14)
        location2 = ((WIDTH/27)/60)*(c_minute)
    santa.pos = (WIDTH - (location1 + location2)), (HEIGHT/2)


def update():
    response = urllib.request.urlopen('http://just-the-time.appspot.com/')
    web_time = (response.read()).decode('utf-8')
    c_day = web_time[0:2]
    c_month = web_time[3:5]
    c_hour = int(web_time[11:13])
    c_minute = int(web_time[14:16])
    
    if c_month == 12 and c_day == 24:
        if c_hour >= 10:
            santa_loc(c_day, c_hour, c_minute)
        else:
            santa.pos = (WIDTH), (HEIGHT/2)
    elif c_month == 12 and c_day == 25:
        if c_hour <= 12:
            santa_loc(c_day, c_hour, c_minute)
        else:
            santa.pos = (WIDTH-WIDTH), (HEIGHT/2)
    else:
        santa.pos = (WIDTH), (HEIGHT/2)
