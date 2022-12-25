import flet as ft
import moviepy as mv
from pytube import YouTube


def main(page:ft.Page):

    page.horizontal_alignment = "center"

    #page.vertical_alignment = 'center'
    page.window_width = 320
    page.window_height = 570
    page.window_resizable = False
    page.theme_mode='light'
    page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(color='BLACK'),
        leading_width=5,
        title=ft.Text("Downloader :v"),
        center_title=True,
        toolbar_height=35, #tamaño
        color='black', #color de letra
        bgcolor='white', #color de fondo
        actions=[
            ft.IconButton(icon='SUNNY')
        ] )
    def textchange(e):
        try:
            video_details=YouTube(url=e.control.value)
            print(video_details)
            print(video_details.title)
        except:
            print(txt)

    txt = ft.TextField(
        label='link', on_change=textchange, cursor_color='red', prefix_icon='LINK', keyboard_type='url', color='black', border='underline'
    )
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

ft.app(target=main) #'https://www.youtube.com/watch?v=kNKu1uNBVkU'
