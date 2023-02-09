import discord
from discord.ext import commands
token = input("Введи токен: ")
prefix = input("Введи префикс: ")
appid = input("Введи айди приложения: ")
largeimageid = input("Введи айди изображения: ")
details = input("Введи самый верхний текст: ")
name = input("Введи название(Стримит на): ")
bot = commands.Bot(command_prefix=prefix, selfbot = True)
large_text = input("Введи ссылку при наводке на картинку: ")
@bot.event
async def on_ready():
	await bot.change_presence(
		activity = discord.Activity(
			type=discord.ActivityType.streaming,
			application_id = appid,
			details = details,
			name = name,
			assets = {
			  'large_image' : str(largeimageid),
			  'large_text':large_text
			},
			url = "https://www.twitch.tv/404%27"
			)
		)
	print(f'DiscordRPC успешно запущен на аккаунте {bot.user}!')

bot.run(token, bot = False)
