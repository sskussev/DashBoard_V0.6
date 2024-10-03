import datetime
import io
import json
import mimetypes
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
import pandas as pd
from django.conf import settings

from .models import DownloadFiles


@login_required
# @permission_required('users.vpn_performance')
def index(request):
    df = pd.read_json(settings.STATICFILES_DIRS[0] + '/board/data/HCi.json')
    df_line = pd.read_json(settings.STATICFILES_DIRS[0] + '/board/data/for_line.json')
    # df_bar = pd.read_json(settings.STATICFILES_DIRS[0] + '/board/data/bar.json')

    print(df_line[df_line['Месяц'] == 'Январь'].iloc[0]['Не заблокированно'])
    month_for_tablet = {
        'Январь': 'yanvar',
        'Февраль': 'fevral',
        'Март': 'mart',
        'Апрель': 'aprel',
        'Май': 'may',
        'Июнь': 'iyun',
        'Июль': 'iyul',
        'Август': 'avgust',
        'Сентябрь': 'sentyabr',
        'Октябрь': 'oktyabr',
        'Ноябрь': 'noyabr',
        'Декабрь': 'dekabr',
        'Итог 2023': 'itog_23',
        'Январь 2024': 'yanvar_24',
        'Февраль 2024': 'fevral_24',
        'Март 2024': 'mart_24',
        '1й квартал 2024': '1-quarter_24',
        'Апрель 2024': 'aprel_24'
    }
    month_for_table_nezabl = {
        'Январь': 'yanvar',
        'Февраль': 'fevral',
        'Март': 'mart',
        'Апрель': 'aprel',
        'Май': 'may',
        'Июнь': 'iyun',
        'Июль': 'iyul',
        'Август': 'avgust',
        'Сентябрь': 'sentyabr',
        'Октябрь': 'oktyabr',
        'Ноябрь': 'noyabr',
        'Декабрь': 'dekabr',
        'Итог 2023': 'itog_23',
        'Январь 2024': 'yanvar_24',
        'Февраль 2024': 'fevral_24',
        'Март 2024': 'mart_24',
        'Апрель 2024': 'aprel_24'
    }

    # with io.open(settings.STATICFILES_DIRS[0] + '/board/data/bar.json', 'r', encoding='utf-8-sig') as file:
    #     data = json.load(file)
    #
    # date_unic = []
    # for i in range(len(data)):
    #     if (data[i]['created'] not in date_unic) and (
    #             datetime.datetime.strptime(data[i]['created'], "%Y-%m-%d").date().year == 2023) and (
    #             datetime.datetime.strptime(data[i]['created'], "%Y-%m-%d").date().month <= 5):
    #         date_unic.append(data[i]['created'])
    # final_data = []
    # for j in range(len(date_unic)):
    #     final_data.append(
    #         {
    #             'created': date_unic[j],
    #             'status_facebook_app': 0,
    #             'status_facebook_web': 0,
    #             'status_instagram_app': 0,
    #             'status_instagram_web': 0,
    #         }
    #     )
    #     for k in range(len(data)):
    #         if data[k]['created'] == final_data[-1]['created']:
    #             final_data[-1]['status_facebook_app'] += data[k]['status_facebook_app']
    #             final_data[-1]['status_facebook_web'] += data[k]['status_facebook_web']
    #             final_data[-1]['status_instagram_app'] += data[k]['status_instagram_app']
    #             final_data[-1]['status_instagram_web'] += data[k]['status_instagram_web']
    #     for k in range(len(final_data)):
    #         if final_data[k]['status_facebook_app'] != 0:
    #             final_data[k]['status_facebook_app'] = 1
    #         if final_data[k]['status_facebook_web'] != 0:
    #             final_data[k]['status_facebook_web'] = 1
    #         if final_data[k]['status_instagram_app'] != 0:
    #             final_data[k]['status_instagram_app'] = 1
    #         if final_data[k]['status_instagram_web'] != 0:
    #             final_data[k]['status_instagram_web'] = 1

    d = {
        'point_number': '',
        'city': '',
        'os': '',
        'operator': '',
        'date': '',
        'f_w': '',
        'f_a': '',
        'i_w': '',
        'i_a': '',
    }


    context = {
        'circle_allowed_present_n': df[(df['Тип'] == 'Незаблокированные') & (df['Относительное время'] == 'Текущий')].iloc[0]['Недоступно'],
        'circle_allowed_present_w': df[(df['Тип'] == 'Незаблокированные') & (df['Относительное время'] == 'Текущий')].iloc[0]['Доступно'],
        'circle_allowed_last_n': df[(df['Тип'] == 'Незаблокированные') & (df['Относительное время'] == 'Предыдущий')].iloc[0]['Недоступно'],
        'circle_allowed_last_w': df[(df['Тип'] == 'Незаблокированные') & (df['Относительное время'] == 'Предыдущий')].iloc[0]['Доступно'],
        'circle_allowed_before_last_n': df[(df['Тип'] == 'Незаблокированные') & (df['Относительное время'] == 'Позапрошлый')].iloc[0]['Недоступно'],
        'circle_allowed_before_last_w': df[(df['Тип'] == 'Незаблокированные') & (df['Относительное время'] == 'Позапрошлый')].iloc[0]['Доступно'],

        'circle_blocked_present_n': df[(df['Тип'] == 'Заблокированные') & (df['Относительное время'] == 'Текущий')].iloc[0]['Недоступно'],
        'circle_blocked_present_w': df[(df['Тип'] == 'Заблокированные') & (df['Относительное время'] == 'Текущий')].iloc[0]['Доступно'],
        'circle_blocked_last_n': df[(df['Тип'] == 'Заблокированные') & (df['Относительное время'] == 'Предыдущий')].iloc[0]['Недоступно'],
        'circle_blocked_last_w': df[(df['Тип'] == 'Заблокированные') & (df['Относительное время'] == 'Предыдущий')].iloc[0]['Доступно'],
        'circle_blocked_before_last_n': df[(df['Тип'] == 'Заблокированные') & (df['Относительное время'] == 'Позапрошлый')].iloc[0]['Недоступно'],
        'circle_blocked_before_last_w': df[(df['Тип'] == 'Заблокированные') & (df['Относительное время'] == 'Позапрошлый')].iloc[0]['Доступно'],

        'circle_all_present_n': df[(df['Тип'] == 'Все') & (df['Относительное время'] == 'Текущий')].iloc[0]['Недоступно'],
        'circle_all_present_w': df[(df['Тип'] == 'Все') & (df['Относительное время'] == 'Текущий')].iloc[0]['Доступно'],
        'circle_all_last_n': df[(df['Тип'] == 'Все') & (df['Относительное время'] == 'Предыдущий')].iloc[0]['Недоступно'],
        'circle_all_last_w': df[(df['Тип'] == 'Все') & (df['Относительное время'] == 'Предыдущий')].iloc[0]['Доступно'],
        'circle_all_before_last_n': df[(df['Тип'] == 'Все') & (df['Относительное время'] == 'Позапрошлый')].iloc[0]['Недоступно'],
        'circle_all_before_last_w': df[(df['Тип'] == 'Все') & (df['Относительное время'] == 'Позапрошлый')].iloc[0]['Доступно'],

        'circle_present_month' : df[(df['Тип'] == 'Все') & (df['Относительное время'] == 'Текущий')].iloc[0]['Месяц'],
        'circle_last_month': df[(df['Тип'] == 'Все') & (df['Относительное время'] == 'Предыдущий')].iloc[0]['Месяц'],
        'circle_before_last_month': df[(df['Тип'] == 'Все') & (df['Относительное время'] == 'Позапрошлый')].iloc[0]['Месяц'],

        # 'line_all': [df_line[df_line['Месяц'] == i].iloc[0]['Не заблокированно'] for i in month],
        # 'line_blocked': [df_line[df_line['Месяц'] == i].iloc[1]['Не заблокированно'] for i in month],
        # 'line_allowed': [df_line[df_line['Месяц'] == i].iloc[2]['Не заблокированно'] for i in month],

# ....................................
        'line_all': [52, 45, 42, 42, 37, 31, 30, 26, 24, 28, 32, 26, 23, 17, 18, 21, ],
        'line_blocked': [41, 38, 34, 34, 32, 26, 23, 20, 19, 24, 27, 22, 20, 15, 16, 19, ],
        'line_allowed': [64, 62, 63, 63, 56, 48, 54, 48, 41, 42, 48, 42, 33, 26, 24, 26, ],


        'month_for_table': month_for_tablet,
        'month_for_table_nezabl': month_for_table_nezabl,

        # 'date_list': [final_data[i]['created'] for i in range(len(final_data))],
        # 'status_facebook_app': [final_data[i]['status_facebook_app'] for i in range(len(final_data))],
        # 'status_facebook_web': [final_data[i]['status_facebook_web'] for i in range(len(final_data))],
        # 'status_instagram_app': [final_data[i]['status_instagram_app'] for i in range(len(final_data))],
        # 'status_instagram_web': [final_data[i]['status_instagram_web'] for i in range(len(final_data))],

    }
    return (render(request, 'board/main.html', context))

@login_required
@permission_required('users.analytics')
def analytics(request):

    return (render(request, 'board/analytics.html'))


@login_required
def download_file(request, filename):
    new_data = DownloadFiles(file_name=filename, author=request.user)
    new_data.save()
    if filename != ' ':
        filepath = os.path.join(settings.MEDIA_ROOT, f'{filename}')
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else:
        return render(request, 'board/file.html')

