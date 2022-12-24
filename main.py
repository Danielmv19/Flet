import flet as ft
import moviepy as mv
from pytube import YouTube
def main(page:ft.Page):
    page.horizontal_alignment = "center"
    #page.vertical_alignment = 'center'
    page.window_width = 350
    page.window_height = 550
    page.window_resizable = False
    page.update()
    page.appbar = ft.AppBar(
        leading=ft.Icon(color='BLACK'),
        leading_width=5,
        title=ft.Text("Downloader :v"),
        center_title=True,
        toolbar_height=35, #tamaño
        color='white', #color de letra
        bgcolor='pink') #color de fondo

    def textchange(e):
        try:
            yt = YouTube(url=e.control.value)
            print(yt)
            print(yt.title)
        except:
            print('error')

    txt = ft.TextField(hint_text='ingresa el link de yt prro/a', on_change=textchange)
    image = ft.Image(
        src='https://cdn-icons-png.flaticon.com/512/725/725300.png',
        width=140,
    )
    boton = ft.ElevatedButton(text='Descargar video')

    page.add(
        image,
        txt,
        boton
    )

ft.app(target=main)
