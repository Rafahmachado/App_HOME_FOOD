import flet as ft
from assets.database import db_manager

def delivery_page(page):
    name_field = ft.TextField(label="Nome do Prato")
    quantity_field = ft.TextField(label="Quantidade", keyboard_type=ft.KeyboardType.NUMBER)
    
    def submit_order(e):
        name = name_field.value
        quantity = int(quantity_field.value)
        db_manager.insert_order(name, quantity)
        ft.Toast(page, "Pedido enviado com sucesso!").show()

    page.bgcolor = ft.colors.LIGHT_GREEN

    page.add(
        ft.Column(
            [
                name_field,
                quantity_field,
                ft.ElevatedButton(text="Enviar Pedido", on_click=submit_order),
                ft.ElevatedButton(text="Ver Pedidos", on_click=lambda e: page.go("/orders"))
            ]
        )
    )
