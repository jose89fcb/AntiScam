from discord.ext import commands
from AntiScam import AntiScam

whitelist = [] #Aquí puede agregar las identificaciones de los usuarios autorizados
logs_channel  =  None  # Aquí puede agregar el ID del canal donde se enviarán los registros.


bot = commands.Bot(command_prefix='>')
bot.remove_command('help') #Borra el comando por defecto !help

@bot.listen() 
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='Muted', verified_role='Verificados', logs_channel=logs_channel) # Here you can change the names of the roles.
   



@bot.event
async def on_ready():
    print("Bot anti-spammer Listo!")

bot.run('')#OBTEN UN TOKEN EN: https://discord.com/developers/applications
