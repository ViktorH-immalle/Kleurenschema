import click
import random

def randomgetallen10(min, max):
    return [random.randint(min, max) for i in range(10)]

#makkelijke manier --> lelijke code
#list_a = [random.randint(0,60), random.randint(0,60), random.randint(0,60), random.randint(0,60), random.randint(0,60), random.randint(0,60), random.randint(0,60),random.randint(0,60)]

#verzorgde manier
list_a = randomgetallen10(0,60)
list_b = randomgetallen10(0,60)

#duidelijke manier
kleurenschema = [
    (10, "red"),
    (20, "magenta"),
    (30, "yellow"),
    (40, "bright_yellow"),
    (50, "blue"),
    (60, "bright_green"),  
]
for k in kleurenschema:
    print(k[0], k[1])

for b in list_b:
    color = ""
    for color in kleurenschema:
        if b >=  color:
            continue
        else: 
            click.secho(str(b), fg=color[1])
            print(color)
            break

#moeilijk aanpasbaar
for a in list_a:
    if a <= 10:
        click.secho(click.style(str(a), fg='red'))
    elif a <= 20 and a > 10:
        click.secho(click.style(str(a), fg='magenta'))
    elif a <= 30 and a > 20:
        click.secho(click.style(str(a), fg='yellow'))  
    elif a <= 40 and a > 30:
        click.secho(click.style(str(a), fg='bright_yellow'))
    elif a <= 50 and a > 40:
        click.secho(click.style(str(a), fg='blue'))
    elif a <= 60 and a > 50:
        click.secho(click.style(str(a), fg='bright_green'))

