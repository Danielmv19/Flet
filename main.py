import flet as ft
import moviepy as mv
import pytube
from pytube import YouTube


def main(page:ft.Page):

    page.horizontal_alignment = "center"

    #page.vertical_alignment = 'center'
    page.window_width = 320
    page.window_height = 570
    page.window_resizable = False
    page.theme_mode='dark'
    page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(color='BLACK'),
        leading_width=5,
        title=ft.Text("Downloader"),
        center_title=True,
        toolbar_height=30, #tamaño
        color='white', #color de letra
        bgcolor='pink', #color de fondo
        actions=[
            ft.IconButton(icon='SUNNY', icon_size=17)
        ] )
    def textchange(e):
        link = e.control.value
        yt = YouTube(link)
        print(yt)
    def descarga():
        pass
    txt = ft.TextField(
        label='link',
        on_submit=textchange,
        cursor_color='red',
        #prefix_icon='LINK',
        keyboard_type='url',
        color='white',
        border='underline',
        filled=True,
    )
    image = ft.Image(
        #src='https://cdn-icons-png.flaticon.com/512/1383/1383327.png',
        src='https://cdn-icons-png.flaticon.com/512/725/725300.png',
        width=140,
    )
    boton = ft.ElevatedButton(text='Descargar video', on_click=descarga, icon='DOWNLOAD_FOR_OFFLINE')

    page.add(
        image,
        txt,
        boton
    )

ft.app(target=main) #'https://www.youtube.com/watch?v=kNKu1uNBVkU'
