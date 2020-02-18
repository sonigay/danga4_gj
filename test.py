import discord
import asyncio
import random
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Quick-4d4e63a22b80.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/1WzFr_aNi6T_ievrOaVJK3hT2tRQsjltfACC6WL2qXNI')




client = discord.Client()


@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='퀵비용 안내', type=1))




@client.event
async def on_message(message):
	global gc #정산
	global creds	#정산
    
          
	if message.content.startswith('!퀵비'):
		SearchID = message.content[len('!퀵비')+1:]
		gc = gspread.authorize(creds)
		wks = gc.open('퀵비확인시트').worksheet('시트1')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
            
		embed = discord.Embed(
			title = ' :motorcycle: 퀵비 가격비교 ',
			description= '**```css\n' + SearchID + ' 까지 업체별 비용은 ' + result + '입니다. 금액이 다소 차이가 있을수 있습니다. ```**',
			color=0x00ff00
			)
		await client.send_message(message.channel, embed=embed)
            

                        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
