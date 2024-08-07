import flet as ft
from assets.database import db_manager

def orders_page(page: ft.Page):
    orders = db_manager.get_orders()
    orders_list = [ft.Text(f"{order[1]} - Quantidade: {order[2]}") for order in orders]
    
    page.bgcolor = ft.colors.LIGHT_YELLOW

    page.add(
        ft.Column(
            [
                ft.Text("Pedidos", size=30, weight=ft.FontWeight.BOLD),
                *orders_list
            ]
        )
    )


