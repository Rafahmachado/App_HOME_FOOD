
import flet as ft
import sqlite3

# Funções para interagir com o banco de dados
def init_db():
    conn = sqlite3.connect('home_food.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_order(name, quantity):
    conn = sqlite3.connect('home_food.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orders (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    conn.close()

def get_orders():
    conn = sqlite3.connect('home_food.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    conn.close()
    return orders

# Funções para as páginas
def delivery_page(page: ft.Page):
    name_field = ft.TextField(label="Nome do Prato")
    quantity_field = ft.TextField(label="Quantidade", keyboard_type=ft.KeyboardType.NUMBER)
    
    def submit_order(e):
        name = name_field.value
        quantity = int(quantity_field.value)
        insert_order(name, quantity)
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

def orders_page(page: ft.Page):
    orders = get_orders()
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

# Função para o layout da página
def layout(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def _top_container():
        return ft.Container(
            width=335 * 0.32,
            height=600 * 0.24,
            bgcolor=ft.colors.WHITE70,
            border_radius=20,
        )

    def _top():
        return ft.Container(
            bgcolor=ft.colors.RED,
            border_radius=20,
            width=335,
            height=600 * 0.35,
            padding=ft.padding.only(top=2, left=8, right=8),
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                value='HOME FOOD',
                                size=15,
                                weight='bold',
                                color=ft.colors.WHITE
                            ),
                            ft.Row(
                                controls=[
                                    ft.Stack(
                                        controls=[
                                            ft.IconButton(
                                                icon=ft.icons.SHOPPING_CART,
                                                icon_size=25,
                                                icon_color=ft.colors.WHITE
                                            ),
                                            ft.Container(
                                                width=40,
                                                height=20,
                                                alignment=ft.alignment.top_right,
                                                content=ft.Text(
                                                    value='9+',
                                                    size=13,
                                                    color=ft.colors.BLUE,
                                                    weight='bold',
                                                )
                                            )
                                        ]
                                    ),
                                    ft.Text(
                                        value='Delivery',
                                        size=10,
                                        weight='bold',
                                        color=ft.colors.WHITE,
                                        italic=True
                                    )
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Row(
                        controls=[_top_container() for _ in range(4)],
                        spacing=3,
                        scroll='auto'
                    )
                ]
            )
        )

    def _bottom():
        return ft.Container(
            width=335,
            height=600 * 0.98,
            padding=ft.padding.only(top=600 * 0.4),
            border_radius=20,
            bgcolor=ft.colors.WHITE,
            content=ft.Column(
                controls=[
                    ft.Tabs(
                        selected_index=0,
                        tabs=[
                            ft.Tab(
                                text='Especial',
                                content=ft.Row(
                                    controls=[
                                        # Adicione os controles desejados aqui
                                    ]
                                )
                            ),
                            ft.Tab(
                                text='Mais',
                                content=ft.Row(
                                    controls=[
                                        # Adicione os controles desejados aqui
                                    ]
                                )
                            )
                        ]
                    )
                ]
            )
        )

    main_layout = ft.Container(
        width=335,
        height=620,
        bgcolor=ft.colors.BLACK,
        border_radius=20,
        content=ft.Column(
            controls=[
                ft.Container(
                    width=335,
                    height=600,
                    bgcolor=ft.colors.RED,
                    border_radius=20,
                    content=ft.Stack(
                        controls=[
                            _bottom(),
                            _top(),
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.add(main_layout)

# Função principal para configurar o aplicativo
def main(page: ft.Page):
    page.title = "Home Food"
    page.route = "/delivery"  # Página inicial

    page.routes = {
        "/delivery": delivery_page,
        "/orders": orders_page,
    }

    layout(page)  # Chama a função de layout
    init_db()  # Inicializa o banco de dados
    
    page.go(page.route)

ft.app(target=main)
