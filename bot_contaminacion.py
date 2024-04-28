import discord
from discord.ext import commands
import random
import os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion con {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un {bot.user} y fui creado para dar consejos de la contaminacion!')

consejos = [
    'Usa bolsas reutilizables para tus compras',
    'Evita los productos de un solo uso como sorbetes y cubiertos de plastico',
    'Utiliza el transporte público',
    "Compra productos locales"
]
@bot.command()
async def consejodeldia(ctx):
    consejo = random.choice(consejos)
    await ctx.send(consejo)

# Funcion que explica que es la contaminacion
@bot.command()
async def contaminacion(ctx):
    definicion = "La contaminacion es cuando hay componentes dañinos o que no deberian estar en el entorno, para saber mas, entra aqui: https://www.eafit.edu.co/ninos/reddelaspreguntas/Paginas/que-es-la-contaminacion.aspx"
    await ctx.send(definicion)
@bot.command()
async def mem(ctx):
    todas_las_imagenes = os.listdir("contaminacion")
    img_name = random.choice(todas_las_imagenes)
    with open(f'contaminacion/{img_name}', 'rb') as f:
            picture = discord.File(f)
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run("Token aqui")
