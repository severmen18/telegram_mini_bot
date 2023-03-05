import sys, os, django
sys.path.append(__file__) #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telegram_bot.settings")
django.setup()

from telegramApp.models import Skills, Students

# skils = Skills.objects.all()
# stu = Students.objects.all()

import telebot
from telebot import types

bot = telebot.TeleBot("6263019067:AAEnyUO5CCku3Uvwwt86H7ZNjWohXRreZ-k")

progress = {}
skills_progress = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	keyboard = telebot.types.InlineKeyboardMarkup()

	button1= telebot.types.InlineKeyboardButton(f'Выбрать школьников по скилам', callback_data='find_student')
	button2 = telebot.types.InlineKeyboardButton(f'Посмотреть все доступные скилы', callback_data='show_skils')
	keyboard.row(button1)
	keyboard.row(button2)
	bot.send_message(message.chat.id, "Я помогу выбрать лучшего", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def query_text(inline_query):
	if inline_query.data == 'find_student':
		progress[inline_query.from_user.id] = 1
		text_skils: str = ""
		for number, skill in enumerate(Skills.objects.all(), start=1):
			text_skils += f"{number}.{skill.skill} \r\n"
		bot.send_message(inline_query.from_user.id, "Напишите через запятую список \
		    скилов среди которых хоттие сделать выбор \r\n" + text_skils)
	if inline_query.data == 'show_skils':
		text_skils: str = ""
		for number, skill in enumerate(Skills.objects.all(), start=1):
			text_skils += f"{number}.{skill.skill} \r\n"
		bot.send_message(inline_query.from_user.id, "На данные помент доступно следующие скилы \r\n "+text_skils)


@bot.chosen_inline_handler(func=lambda chosen_inline_result: True)
def test_chosen(chosen_inline_result):
	a = 6

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.from_user.id in progress.keys():
		if progress[message.from_user.id] == 1:
			result_skils = []
			result_skils_text = ""
			DBskills = [skill_[0].upper() for skill_ in Skills.objects.values_list('skill').all()]
			for skill in message.text.split(","):
				if skill.upper().strip() in DBskills:
					result_skils.append(skill.upper())
					result_skils_text += skill.strip()+" "

			if len(result_skils) == 0:
				bot.send_message(message.chat.id,"Ошибка введите хотябы один скил" )
				return
			skills_progress[message.from_user.id] = result_skils
			progress[message.from_user.id] = 2
			bot.send_message(message.chat.id,"Вы выбрали "+result_skils_text + "\r\n \
			выберите возраст введите два числа через запятую" )
			return
		if progress[message.from_user.id] == 2:
			from_, to_ = message.text.split(",")

			result_text = ""
			for student in Students.objects.all():
				havent_skils = False
				if student.age >= int(from_) and student.age <= int(to_):
					DB_student_skills = [skill_[0].upper() for skill_ in student.skils.values_list('skill').all()]
					for need_skill in skills_progress[message.from_user.id]:
						if not need_skill.upper() in DB_student_skills:
							havent_skils = True
				if not havent_skils == True:
					result_text += f" {student.last_name} {student.first_name} возраст {student.age} \r\n"
			if result_text == "":
				bot.send_message(message.chat.id,"По вашему ничего не найдено\r\n"+ result_text)
			else:
				bot.send_message(message.chat.id,"По вашему запросу были найдено \r\n"+ result_text)
			return	
			


	bot.reply_to(message, message.text)

bot.infinity_polling()