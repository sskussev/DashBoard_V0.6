from dash import Dash, html, dcc, Input, Output, dash_table
import plotly.graph_objs as go
import pandas as pd
from django.conf import settings
import random
    
vpn_info_dictionary = [
    {
    'Номер':1,
    'Название на Android':'AdGuard VPN',
    'Название на IOS':'AdGuard VPN – Unlimited & Fast',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['AdGuard VPN'],
    'Названия в базе на IOS':['AdGuard VPN – Unlimited & Fast']
    },
    {
    'Номер':2,
    'Название на Android':'Антивирус - очиститель + ВПН',
    'Название на IOS':'Antivirus - Cleaner + VPN',
    'Другие названия на Android':['Antivirus - Cleaner + VPN'],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Антивирус - очиститель + ВПН', 'Antivirus - Cleaner + VPN'],
    'Названия в базе на IOS':['Antivirus - Cleaner + VPN']
    },
    {
    'Номер':3,
    'Название на Android':'Atlas VPN: ВПН для мобильного',
    'Название на IOS':'Atlas ВПН:быстрый и безопасный',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Atlas VPN: ВПН для мобильного'],
    'Названия в базе на IOS':['Atlas ВПН:быстрый и безопасный']
    },
    {
    'Номер': 4,
    'Название на Android':'Betternet VPN - Hotspot Proxy',
    'Название на IOS':'VPN/ВПН прокси Betternet',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Betternet VPN - Hotspot Proxy'],
    'Названия в базе на IOS':['VPN/ВПН прокси Betternet']
    },
    {
    'Номер': 5,
    'Название на Android':'BigMama - VPN',
    'Название на IOS':'BigMama VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['BigMama - VPN'],
    'Названия в базе на IOS':['BigMama VPN']
    },
    {
    'Номер': 6,
    'Название на Android':'1.1.1.1: Faster&Safer Internet',
    'Название на IOS':'1.1.1.1: Faster Internet',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['1.1.1.1: Faster&Safer Internet'],
    'Названия в базе на IOS':['1.1.1.1: Faster Internet']
    },
    {
    'Номер': 7,
    'Название на Android':'VPN Express VPN - Быстрый ВПН',
    'Название на IOS':'VPN ExpressVPN - Быстрый ВПН',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Express VPN - Быстрый ВПН'],
    'Названия в базе на IOS':['VPN ExpressVPN - Быстрый ВПН']
    },
    {
    'Номер': 8,
    'Название на Android':'Free VPN by Free VPN .org',
    'Название на IOS':'Free VPN by Free VPN .org',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Free VPN by Free VPN .org'],
    'Названия в базе на IOS':['Free VPN by Free VPN .org']
    },
    {
    'Номер':9,
    'Название на Android':'GeckoVPN Unlimited Proxy VPN',
    'Название на IOS':'Gecko VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['GeckoVPN Unlimited Proxy VPN'],
    'Названия в базе на IOS':['Gecko VPN']
    },
    {
    'Номер':10 ,
    'Название на Android':'VPN быстро и безопасно GoVPN',
    'Название на IOS':'Go VPN - Super Fast VPN Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN быстро и безопасно GoVPN'],
    'Названия в базе на IOS':['Go VPN - Super Fast VPN Proxy']
    },
    {
    'Номер': 11,
    'Название на Android':'HideMyAss VPN',
    'Название на IOS':'HideMyAss VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['HideMyAss VPN'],
    'Названия в базе на IOS':['HideMyAss VPN']
    },
    {
    'Номер': 12,
    'Название на Android':'Hola VPN',
    'Название на IOS':'Hola VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Hola VPN'],
    'Названия в базе на IOS':['Hola VPN']
    },
    {
    'Номер': 13,
    'Название на Android':'HotBot VPN Быстро и безопасно',
    'Название на IOS':'HotBot VPN | Прокси.',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['HotBot VPN Быстро и безопасно'],
    'Названия в базе на IOS':['HotBot VPN | Прокси.']
    },
    {
    'Номер': 14,
    'Название на Android':'IPVanish VPN: The Fastest VPN',
    'Название на IOS':'IPVanish VPN: The Fastest VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['IPVanish VPN: The Fastest VPN'],
    'Названия в базе на IOS':['IPVanish VPN: The Fastest VPN']
    },
# 15-й номер (KeepSolid VPN) удален
    {
    'Номер':16,
    'Название на Android':'KeyVPN AppLock - Бесплатный VPN',
    'Название на IOS':'Key VPN',
    'Другие названия на Android':['KeyVPN AppLock - Бесплатный VPN'],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['KeyVPN AppLock - Бесплатный VP', 'KeyVPN AppLock - Бесплатный VPN'],
    'Названия в базе на IOS':['Key VPN']
    },
    {
    'Номер': 17,
    'Название на Android':'Krot.io VPN',
    'Название на IOS':'Krot.io VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Krot.io VPN'],
    'Названия в базе на IOS':['Krot.io VPN']
    },
    {
    'Номер': 18,
    'Название на Android':'KUTO VPN - Очень быстрый VPN',
    'Название на IOS':'Kuto VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['KUTO VPN - Очень быстрый VPN'],
    'Названия в базе на IOS':['Kuto VPN']
    },
    {
    'Номер':19,
    'Название на Android':'Lantern: Лучше, чем VPN',
    'Название на IOS':'Lantern VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Lantern: Лучше, чем VPN'],
    'Названия в базе на IOS':['Lantern VPN']
    },
    {
    'Номер': 20,
    'Название на Android':'Near VPN',
    'Название на IOS':'NearVPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Near VPN'],
    'Названия в базе на IOS':['NearVPN']
    },
    {
    'Номер': 21,
    'Название на Android':'Nord VPN: VPN без ограничений',
    'Название на IOS':'Nord VPN: быстрый и лучший ВПН',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Nord VPN: VPN без ограничений'],
    'Названия в базе на IOS':['Nord VPN: быстрый и лучший ВПН']
    },
    {
    'Номер': 22,
    'Название на Android':'OpenVPN Connect - OpenVPN App (Vypr VPN)',
    'Название на IOS':'OpenVPN Connect (Vypr VPN)',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['OpenVPN Connect - OpenVPN App (Vypr VPN)', 'OpenVPN Connect - OpenVPN App'],
    'Названия в базе на IOS':['OpenVPN Connect (Vypr VPN)', 'OpenVPN Connect - OpenVPN App']
    },
    {
    'Номер':23,
    'Название на Android':'Opera VPN',
    'Название на IOS':'Opera VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Opera VPN'],
    'Названия в базе на IOS':['Opera VPN']
    },
    {
    'Номер':24,
    'Название на Android':'Private Tunnel VPN - Fast & Secure Cloud VPN',
    'Название на IOS':'Private Tunnel VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Private Tunnel VPN - Fast & Secure Cloud VPN'],
    'Названия в базе на IOS':['Private Tunnel VPN']
    },
    {
    'Номер':25,
    'Название на Android':'Psiphon Pro',
    'Название на IOS':'Psiphon',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Psiphon Pro'],
    'Названия в базе на IOS':['Psiphon']
    },
    {
    'Номер': 26,
    'Название на Android':'RavoVPN-Secure&Fast Proxy',
    'Название на IOS':'Ravo VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['RavoVPN-Secure&Fast Proxy'],
    'Названия в базе на IOS':['Ravo VPN']
    },
    {
    'Номер':27,
    'Название на Android':'Red Shield VPN',
    'Название на IOS':'Red Shield VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Red Shield VPN'],
    'Названия в базе на IOS':['Red Shield VPN']
    },
    {
    'Номер': 28,
    'Название на Android':'RiseupVPN',
    'Название на IOS':'Riseup VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['RiseupVPN'],
    'Названия в базе на IOS':['Riseup VPN']
    },
    {
    'Номер': 29,
    'Название на Android':'Secure VPN - Безопаснее, быстрее',
    'Название на IOS':'SecureVPN - Защита Данных',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Secure VPN - Безопаснее, быстрее'],
    'Названия в базе на IOS':['SecureVPN - Защита Данных']
    },
    {
    'Номер': 30,
    'Название на Android':'Security Master',
    'Название на IOS':'Security Master',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Security Master'],
    'Названия в базе на IOS':['Security Master']
    },
    {
    'Номер': 31,
    'Название на Android':'Sky VPN - быстрый безопасныйVPN',
    'Название на IOS':'Sky VPN: Безлимитный VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Sky VPN - быстрый безопасныйVPN'],
    'Названия в базе на IOS':['Sky VPN: Безлимитный VPN']
    },
    {
    'Номер': 32,
    'Название на Android':'Отсутствует',
    'Название на IOS':'Solo VPN- Proxy Betternet',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['Solo VPN- Proxy Betternet']
    },
    {
    'Номер': 33,
    'Название на Android':'Speedify - Live Streaming VPN',
    'Название на IOS':'Speedify',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Speedify - Live Streaming VPN'],
    'Названия в базе на IOS':['Speedify']
    },
    {
    'Номер': 34,
    'Название на Android':'SuperVPN - Unlimited Proxy',
    'Название на IOS':'Super VPN - Secure VPN Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['SuperVPN - Unlimited Proxy'],
    'Названия в базе на IOS':['Super VPN - Secure VPN Proxy']
    },
    {
    'Номер':35,
    'Название на Android':'Tachyon VPN - Private Proxy',
    'Название на IOS':'Tachyon VPN - Private Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Tachyon VPN - Private Proxy'],
    'Названия в базе на IOS':['Tachyon VPN - Private Proxy']
    },
    {
    'Номер': 36,
    'Название на Android':'Thunder VPN: Более быстрый VPN',
    'Название на IOS':'Thunder VPN - VPN for iPhone',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Thunder VPN: Более быстрый VPN'],
    'Названия в базе на IOS':['Thunder VPN - VPN for iPhone']
    },
    {
    'Номер':37,
    'Название на Android':'Tik VPN: быстрый и безлимитный',
    'Название на IOS':'TikVPN-Безлимитный прокси ВПН',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Tik VPN: быстрый и безлимитный'],
    'Названия в базе на IOS':['TikVPN-Безлимитный прокси ВПН']
    },
    {
    'Номер':38,
    'Название на Android':'Tiny VPN',
    'Название на IOS':'Tiny VPN - Ultra Fast',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Tiny VPN'],
    'Названия в базе на IOS':['Tiny VPN - Ultra Fast']
    },
    {
    'Номер':39,
    'Название на Android':'Private & Secure VPN: TorGuard',
    'Название на IOS':'Private & Secure VPN: TorGuard',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Private & Secure VPN: TorGuard'],
    'Названия в базе на IOS':['Private & Secure VPN: TorGuard']
    },
    {
    'Номер': 40,
    'Название на Android':'Touch VPN - VPN Proxy & Privacy',
    'Название на IOS':'TouchVPN – Безграничный Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Touch VPN - VPN Proxy & Privacy'],
    'Названия в базе на IOS':['TouchVPN – Безграничный Proxy']
    },
    {
    'Номер': 41,
    'Название на Android':'Trust.Zone VPN - Anonymous VPN',
    'Название на IOS':'Trust.Zone VPN - Anonymous VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Trust.Zone VPN - Anonymous VPN'],
    'Названия в базе на IOS':['Trust.Zone VPN - Anonymous VPN']
    },
    {
    'Номер': 42,
    'Название на Android':'Tube VPN-Secure&Fast&Stable',
    'Название на IOS':'Tube VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Tube VPN-Secure&Fast&Stable'],
    'Названия в базе на IOS':['Tube VPN']
    },
    {
    'Номер': 43,
    'Название на Android':'TunnelBear: Secure VPN & Wifi',
    'Название на IOS':'TunnelBear: Secure VPN & Wifi',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['TunnelBear: Secure VPN & Wifi'],
    'Названия в базе на IOS':['TunnelBear: Secure VPN & Wifi']
    },
    {
    'Номер':44,
    'Название на Android':'Turbo VPN - безопасный ВПН',
    'Название на IOS':'Turbo VPN приватный браузер',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Turbo VPN - безопасный ВПН'],
    'Названия в базе на IOS':['Turbo VPN приватный браузер']
    },
    {
    'Номер':45,
    'Название на Android':'UFO VPN',
    'Название на IOS':'UFO VPN - Супер VPN-Сервис',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['UFO VPN'],
    'Названия в базе на IOS':['UFO VPN - Супер VPN-Сервис']
    },
    {
    'Номер':46,
    'Название на Android':'Ultimate VPN',
    'Название на IOS':'Ultimate VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Ultimate VPN'],
    'Названия в базе на IOS':['Ultimate VPN']
    },
    {
    'Номер': 47,
    'Название на Android':'베일덕 VPN - 빠르고 안전한 VPN',
    'Название на IOS':'VeilDuck VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['베일덕 VPN - 빠르고 안전한 VPN'],
    'Названия в базе на IOS':['VeilDuck VPN']
    },
    {
    'Номер': 48,
    'Название на Android':'VPN GO - Private Net Access',
    'Название на IOS':'VPN GO - Private VPN for Net',
    'Другие названия на Android':['NetGO - Private Net Access'],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['NetGO - Private Net Access', 'VPN GO - Private Net Access'],
    'Названия в базе на IOS':['VPN GO - Private VPN for Net']
    },
    {
    'Номер':49,
    'Название на Android':'VPN Proxy Master: Super Vpn',
    'Название на IOS':'VPN Master Неограниченный прокси',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Proxy Master: Super Vpn'],
    'Названия в базе на IOS':['VPN Master Неограниченный прокси']
    },
    {
    'Номер':50,
    'Название на Android':'VPN.lat: Unlimited and Secure',
    'Название на IOS':'VPN_Lat',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN.lat: Unlimited and Secure'],
    'Названия в базе на IOS':['VPN_Lat']
    },
    {
    'Номер': 51,
    'Название на Android':'VPN Private - Fast VPN Master',
    'Название на IOS':'VPN Private',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Private - Fast VPN Master'],
    'Названия в базе на IOS':['VPN Private']
    },
    {
    'Номер':52,
    'Название на Android':'vpnify',
    'Название на IOS':'VPNIFY - Unlimited VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['vpnify'],
    'Названия в базе на IOS':['VPNIFY - Unlimited VPN']
    },
    {
    'Номер':53,
    'Название на Android':'Vypr VPN: VPN и приватность',
    'Название на IOS':'Vypr VPN: VPN и приватность',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Vypr VPN: VPN и приватность'],
    'Названия в базе на IOS':['Vypr VPN: VPN и приватность']
    },
    {
    'Номер':54,
    'Название на Android':'Windscribe VPN',
    'Название на IOS':'Windscribe VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Windscribe VPN'],
    'Названия в базе на IOS':['Windscribe VPN']
    },
    {
    'Номер':55,
    'Название на Android':'X-VPN - Private Browser VPN',
    'Название на IOS':'X-VPN - Best VPN Proxy master',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['X-VPN - Private Browser VPN'],
    'Названия в базе на IOS':['X-VPN - Best VPN Proxy master']
    },
    {
    'Номер': 56,
    'Название на Android':'Vast VPN - Fast & Secure',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['Vast VPN - Fast & Secure'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 57,
    'Название на Android':'WiFi Map®: Find Internet, VPN',
    'Название на IOS':'WiFi Map: Internet, eSIM, VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['WiFi Map®: Find Internet, VPN'],
    'Названия в базе на IOS':['WiFi Map: Internet, eSIM, VPN']
    },
    {
    'Номер': 58,
    'Название на Android':'VPN PotatoVPN - WiFi Proxy',
    'Название на IOS':'VPN PotatoVPN -Fast WiFi Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['VPN PotatoVPN - WiFi Proxy'],
    'Названия в базе на IOS':['VPN PotatoVPN -Fast WiFi Proxy']
    },
    {
    'Номер':59,
    'Название на Android':'VPN Бобер сервис ВПН',
    'Название на IOS':'VPN Мастер – ВПН прокси',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Бобер сервис ВПН'],
    'Названия в базе на IOS':['VPN Мастер – ВПН прокси']
    },
    {
    'Номер':60,
    'Название на Android':'hidemy.name VPN',
    'Название на IOS':'hidemy.name VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['hidemy.name VPN'],
    'Названия в базе на IOS':['hidemy.name VPN']
    },
    {
    'Номер':61,
    'Название на Android':'Star VPN: Unlimited WiFi Proxy',
    'Название на IOS':'Star VPN: Unlimited WiFi Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['Star VPN: Unlimited WiFi Proxy'],
    'Названия в базе на IOS':['Star VPN: Unlimited WiFi Proxy']
    },
    {
    'Номер':62,
    'Название на Android':'Surfshark VPN - мобильный ВПН',
    'Название на IOS':'VPN Surfshark - ВПН прокси',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['Surfshark VPN - мобильный ВПН'],
    'Названия в базе на IOS':['VPN Surfshark - ВПН прокси']
    },
    {
    'Номер':63,
    'Название на Android':'Melon VPN - Прокси-VPN',
    'Название на IOS':'Melon VPN - Easy Fast VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['Melon VPN - Прокси-VPN'],
    'Названия в базе на IOS':['Melon VPN - Easy Fast VPN']
    },
    {
    'Номер':64,
    'Название на Android':'Proton VPN: Private, secure',
    'Название на IOS':'OpenVPN Connect (Proton VPN)',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['Proton VPN: Private, secure'],
    'Названия в базе на IOS':['Proton VPN: Fast & Secure', 'OpenVPN Connect (Proton VPN)'],
    },
    {
    'Номер':65,
    'Название на Android':'Tomato VPN | VPN Proxy',
    'Название на IOS':'VPN Tomato Pro - Fast & Secure',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Tomato VPN | VPN Proxy'],
    'Названия в базе на IOS':['VPN Tomato - Unlimited Proxy', 'VPN Tomato Pro - Fast & Secure']
    },
    {
    'Номер': 66,
    'Название на Android':'VPN сервис от VPN Monster',
    'Название на IOS':'OpenVPN Connect (VPN Monster)',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['VPN сервис от VPN Monster'],
    'Названия в базе на IOS':['OpenVPN Connect (VPN Monster)']
    },
    {
    'Номер': 67,
    'Название на Android':'McAfee Security: Antivirus VPN',
    'Название на IOS':'McAfee Security: VPN и защита',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['McAfee Security: Antivirus VPN'],
    'Названия в базе на IOS':['McAfee Security: VPN и защита']
    },
    {
    'Номер': 68,
    'Название на Android':'Aloha Браузер + Private VPN',
    'Название на IOS':'Aloha Browser: браузер VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['Aloha Браузер + Private VPN'],
    'Названия в базе на IOS':['Aloha Browser: браузер VPN']
    },
    {
    'Номер':69,
    'Название на Android':'ZenMate VPN - быстрый и безопасный',
    'Название на IOS':'ZenMate ВПН и прокси-сервер',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['ZenMate VPN - быстрый и безопа', 'ZenMate VPN - быстрый и безопасный'],
    'Названия в базе на IOS':['ZenMate ВПН и прокси-сервер']
    },
    {
    'Номер': 70,
    'Название на Android':'Ultrasurf - Fast Unlimited VPN',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['Ultrasurf - Fast Unlimited VPN'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 72,
    'Название на Android':'GreenNet: Hotspot VPN Proxy',
    'Название на IOS':'GreenNet VPN Proxy & Unlimited',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['GreenNet: Hotspot VPN Proxy'],
    'Названия в базе на IOS':['GreenNet VPN Proxy & Unlimited']
    },
    {
    'Номер': 73,
    'Название на Android':'VPNhub: безлимитно и безопасно',
    'Название на IOS':'VPNHUB - Лучший прокси VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['VPNhub: безлимитно и безопасно'],
    'Названия в базе на IOS':['VPNHUB - Лучший прокси VPN']
    },
    {
    'Номер': 74,
    'Название на Android':'Browsec VPN: ВПН, анонимайзер',
    'Название на IOS':'Browsec VPN: Безлимитный ВПН',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Browsec VPN: ВПН, анонимайзер'],
    'Названия в базе на IOS':['Browsec VPN: Безлимитный ВПН']
    },
    {
    'Номер': 75,
    'Название на Android':'VPN – Super Unlimited Proxy',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN – Super Unlimited Proxy'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 76,
    'Название на Android':'VPN Россия (VPN RedCat)',
    'Название на IOS':'VPN RedCat быстрый ВНП сервис',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Россия - ВПН Сервис безлим', 'VPN Россия (VPN RedCat)'],
    'Названия в базе на IOS':['VPN RedCat быстрый ВНП сервис']
    },
    {
    'Номер': 77,
    'Название на Android':'SecVPN Proxy Tool',
    'Название на IOS':'SecVPN: Trusted Secure VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['SecVPN Proxy Tool'],
    'Названия в базе на IOS':['SecVPN: Trusted Secure VPN']
    },
    {
    'Номер': 78,
    'Название на Android':'VPN by CyberGhost: Secure Wi-fi',
    'Название на IOS':'CyberGhost VPN/ВПН прокси',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN by CyberGhost: Secure Wi-fi'],
    'Названия в базе на IOS':['CyberGhost VPN/ВПН прокси']
    },
    {
    'Номер': 79,
    'Название на Android':'Urban VPN Proxy Unlocker',
    'Название на IOS':'Urban VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Urban VPN Proxy Unlocker'],
    'Названия в базе на IOS':['Urban VPN']
    },
    {
    'Номер': 80,
    'Название на Android':'Speedy Quark VPN - VPN Master',
    'Название на IOS':'Speedy Quark VPN - VPN Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Speedy Quark VPN - VPN Master'],
    'Названия в базе на IOS':['Speedy Quark VPN - VPN Proxy']
    },
    {
    'Номер':81,
    'Название на Android':'впн инстаграм - Proxy Master',
    'Название на IOS':'Мастер VPN – Супер быстрый VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['впн инстаграм - Proxy Master'],
    'Названия в базе на IOS':['Мастер VPN – Супер быстрый VPN']
    },
    {
    'Номер': 82,
    'Название на Android':'VPN Fast - супер впн россия',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Fast - супер впн россия'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 83,
    'Название на Android':'VPN Pro: безопасно и быстро',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Pro: безопасно и быстро'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 84,
    'Название на Android':'Fast VPN - Fast & Secure Proxy',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['Fast VPN - Fast & Secure Proxy'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 85,
    'Название на Android':'VPN Master Pro - Fast & Secure',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Master Pro - Fast & Secure'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 86,
    'Название на Android':'VPN Ukraine - Get Ukrainian IP',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Ukraine - Get Ukrainian IP'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 87,
    'Название на Android':'VPN Master - Hotspot VPN Proxy',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Master - Hotspot VPN Proxy'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 88,
    'Название на Android':'iTop VPN Proxy & Game Booster',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['iTop VPN Proxy & Game Booster'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 89,
    'Название на Android':'Snap VPN: Super Fast VPN Proxy',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['Snap VPN: Super Fast VPN Proxy'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':90,
    'Название на Android':'Отсутствует',
    'Название на IOS':'RayVPN Lite: Unlimited Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['RayVPN Lite: Unlimited Proxy']
    },
    {
    'Номер':91,
    'Название на Android':'Отсутствует',
    'Название на IOS':'ТОР БРАУЗЕР: TOR Browser + VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['ТОР БРАУЗЕР: TOR Browser + VPN']
    },
    {
    'Номер':92,
    'Название на Android':'Отсутствует',
    'Название на IOS':'Тор браузер: OrNET онион + впн',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['Тор браузер: OrNET онион + впн']
    },
    {
    'Номер':93,
    'Название на Android':'Отсутствует',
    'Название на IOS':'ВПН Мастер: VPN Прокси',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['ВПН Мастер: VPN Прокси']
    },
    {
    'Номер':94,
    'Название на Android':'Отсутствует',
    'Название на IOS':'Wirevpn – безлимитный VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['Wirevpn – безлимитный VPN']
    },
    {
    'Номер':95,
    'Название на Android':'Отсутствует',
    'Название на IOS':'VPN-AmanVPN / ВПН прокси',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['VPN-AmanVPN / ВПН прокси']
    },
    {
    'Номер':96,
    'Название на Android':'Отсутствует',
    'Название на IOS':'VPN Speed-Fast Unlimited Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['VPN Speed-Fast Unlimited Proxy']
    },
    {
    'Номер':97,
    'Название на Android':'Отсутствует',
    'Название на IOS':'VPN Proxy Master – ВПН прокси',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['VPN Proxy Master – ВПН прокси']
    },
    {
    'Номер':98,
    'Название на Android':'VPN Proxy - Secure VPN',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['VPN Proxy - Secure VPN'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':99,
    'Название на Android':'VPN Master - fast proxy VPN',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['VPN Master - fast proxy VPN'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':100,
    'Название на Android':'Отсутствует',
    'Название на IOS':'VPN Master – Fast Proxy Server',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['VPN Master – Fast Proxy Server']
    },
    {
    'Номер':101,
    'Название на Android':'Отсутствует',
    'Название на IOS':'VPN Bucks – лучший впн прокси',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['VPN Bucks – лучший впн прокси']
    },
    {
    'Номер':102,
    'Название на Android':'Отсутствует',
    'Название на IOS':'VPN - Secure Super Fast VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['VPN - Secure Super Fast VPN']
    },
    {
    'Номер':103,
    'Название на Android':'Отсутствует',
    'Название на IOS':'VPN - Master VPN/ВПН прокси',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['VPN - Master VPN/ВПН прокси']
    },
    {
    'Номер':104,
    'Название на Android':'Unblock Websites - VPN Proxy A',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['Unblock Websites - VPN Proxy A'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':105,
    'Название на Android':'SuperVPN Fast VPN Client',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['SuperVPN Fast VPN Client'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':106,
    'Название на Android':'SuperNet VPN - Fast VPN Proxy',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['SuperNet VPN - Fast VPN Proxy'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':107,
    'Название на Android':'Signal Secure VPN -Fast VPN',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Signal Secure VPN -Fast VPN'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':108,
    'Название на Android':'Отсутствует',
    'Название на IOS':'Secure VPN Proxy – Fast Server',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['Secure VPN Proxy – Fast Server']
    },
    {
    'Номер':109,
    'Название на Android':'Planet VPN: быстро и безопасно',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['Planet VPN: быстро и безопасно'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':110,
    'Название на Android':'Phone Guardian',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['Phone Guardian'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':111,
    'Название на Android':'Отсутствует',
    'Название на IOS':'PandaVPN Lite - лучший VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['PandaVPN Lite - лучший VPN']
    },
    {
    'Номер':112,
    'Название на Android':'Отсутствует',
    'Название на IOS':'nthLink',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['nthLink']
    },
    {
    'Номер':113,
    'Название на Android':'Master VPN - ВПН для Андроид',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['Master VPN - ВПН для Андроид'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':114,
    'Название на Android':'Отсутствует',
    'Название на IOS':'Master Lite – Proxy Server',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['Master Lite – Proxy Server']
    },
    {
    'Номер':115,
    'Название на Android':'Kiwi VPN Connection IP Changer',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['Kiwi VPN Connection IP Changer'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':116,
    'Название на Android':'HotspotShield VPN & Wifi Proxy',
    'Название на IOS':'HotspotShield VPN & Wifi Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['HotspotShield VPN & Wifi Proxy'],
    'Названия в базе на IOS':['HotspotShield VPN & Wifi Proxy']
    },
    {
    'Номер':117,
    'Название на Android':'Отсутствует',
    'Название на IOS':'hide.me VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['hide.me VPN']
    },
    {
    'Номер':118,
    'Название на Android':'Отсутствует',
    'Название на IOS':'HaloVPN: Fast Secure VPN Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['HaloVPN: Fast Secure VPN Proxy']
    },
    {
    'Номер':119,
    'Название на Android':'Goat VPN - Super Fast&Safe VPN',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':['Goat VPN - Super Fast&Safe VPN'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':120,
    'Название на Android':'Отсутствует',
    'Название на IOS':'Fast VPN: Best Proxy Master',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['Fast VPN: Best Proxy Master']
    },
    {
    'Номер':121,
    'Название на Android':'Daily VPN - безопасный VPN',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Daily VPN - безопасный VPN'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':122,
    'Название на Android':'Отсутствует',
    'Название на IOS':'360 VPN - Privacy & Security',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': False,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['360 VPN - Privacy & Security']
    },
    {
    'Номер':123,
    'Название на Android':'VPN Master - Fast Secure Proxy',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Master - Fast Secure Proxy'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 124,
    'Название на Android':'VPN Russia - Unblock VPN Proxy',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Russia - Unblock VPN Proxy'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер':125,
    'Название на Android':'Tomato VPN - Hotspot VPN Proxy',
    'Название на IOS':'Tomato VPN - Hotspot VPN Proxy',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['Tomato VPN - Hotspot VPN Proxy'],
    'Названия в базе на IOS':['Tomato VPN - Hotspot VPN Proxy']
    },
    {
    'Номер': 126,
    'Название на Android':'SoloVPN - One Tap Proxy',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':['SoloVPN - One Tap Proxy'],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 127,
    'Название на Android':'Отсутствует',
    'Название на IOS':'Ultrasurf VPN',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['Ultrasurf VPN']
    },
    {
    'Номер': 128,
    'Название на Android':'Отсутствует',
    'Название на IOS':'VPN - Super VPN/ВПН прокси',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'01.10.2022',
    'Блокируется': True,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':['VPN - Super VPN/ВПН прокси']
    },
    {
    'Номер':129,
    'Название на Android':'VPN Unlimited – Proxy Shield',
    'Название на IOS':'VPN Unlimited - Proxy Master',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений':'21.03.2023',
    'Блокируется': True,
    'Названия в базе на Android':['VPN Unlimited – Proxy Shield'],
    'Названия в базе на IOS':['VPN Unlimited - Proxy Master']
    },
    {
    'Номер': 130,
    'Название на Android': 'VPN Proxy - Super VPN Master',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.02.2023',
    'Блокируется': True,
    'Названия в базе на Android': [],
    'Названия в базе на IOS': [],
    },
    # новая партия от 01.05.2023
    {
    'Номер': 131,
    'Название на Android':'AnonymoX VPN',
    'Название на IOS':'Отсутствует',
    'Другие названия на Android':[],
    'Другие названия на IOS':[],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android':[],
    'Названия в базе на IOS':[]
    },
    {
    'Номер': 132,
    'Название на Android': 'Avira Phantom VPN',
    'Название на IOS': 'Avira Phantom VPN & Wifi Proxy',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': [],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 133,
    'Название на Android': 'CandyLink VPN',
    'Название на IOS': 'Candylink VPN',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['CandyLink VPN',],
    'Названия в базе на IOS': ['Candylink VPN',]
    },
    {
    'Номер': 134,
    'Название на Android': 'FishVPN - Безопасность Прокси',
    'Название на IOS': 'FishVPN - Безопасность Прокси',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': [],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 135,
    'Название на Android': 'Freedom VPN',
    'Название на IOS': 'Freedom-VPN',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['Freedom VPN',],
    'Названия в базе на IOS': ['Freedom-VPN',]
    },
    {
    'Номер': 136,
    'Название на Android': 'Garuda VPN',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': [],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 137,
    'Название на Android': 'Hoxx VPN',
    'Название на IOS': 'Hoxx VPN',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['Hoxx VPN',],
    'Названия в базе на IOS': ['Hoxx VPN',]
    },
    {
    'Номер': 138,
    'Название на Android': 'Отсутствует',
    'Название на IOS': 'iCloud private relay',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': [],
    'Названия в базе на IOS': ['iCloud private relay',]
    },
    {
    'Номер': 139,
    'Название на Android': 'Insta VPN - Fast Private VPN',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['Insta VPN - Fast Private VPN',],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 140,
    'Название на Android': 'LomVPN',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['LomVPN',],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 141,
    'Название на Android': 'metaVPN – надежен и безлимитен',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['metaVPN – надежен и безлимитен',],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 142,
    'Название на Android': 'Mullvad VPN',
    'Название на IOS': 'Mullvad VPN',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['Mullvad VPN',],
    'Названия в базе на IOS': ['Mullvad VPN',]
    },
    {
    'Номер': 143,
    'Название на Android': 'Steganos VPN Online Shield',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['Steganos VPN Online Shield'],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 144,
    'Название на Android': 'Seed4.Me VPN Proxy',
    'Название на IOS': 'VPN Proxy by Seed4.Me VPN',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['Seed4.Me VPN Proxy',],
    'Названия в базе на IOS': ['VPN Proxy by Seed4.Me VPN',]
    },
    {
    'Номер': 145,
    'Название на Android': 'Отсутствует',
    'Название на IOS': 'Snap VPN - Super VPN Browser',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': [],
    'Названия в базе на IOS': ['Snap VPN - Super VPN Browser',]
    },
    {
    'Номер': 146,
    'Название на Android': 'Unblock Websites - VPN by uVPN',
    'Название на IOS': 'uVPN: Super Fast Secure VPN',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['Unblock Websites - VPN by uVPN',],
    'Названия в базе на IOS': ['uVPN: Super Fast Secure VPN',]
    },
    {
    'Номер': 147,
    'Название на Android': 'VPN - Super VPN Proxy Master',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['VPN - Super VPN Proxy Master',],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 148,
    'Название на Android': 'OpenVPN Connect (VPN Gate)',
    'Название на IOS': 'OpenVPN Connect (VPN Gate)',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['OpenVPN Connect (VPN Gate)',],
    'Названия в базе на IOS': ['OpenVPN Connect (VPN Gate)',]
    },
    {
    'Номер': 149,
    'Название на Android': 'VPN Proxy Speed - Super VPN',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['VPN Proxy Speed - Super VPN',],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 150,
    'Название на Android': 'VPN Super Proxy - Proxy Master',
    'Название на IOS': 'VPN Super Proxy - Proxy Master',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': [],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 151,
    'Название на Android': 'Отсутствует',
    'Название на IOS': 'RelyVPN - WiFi Proxy Master',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': [],
    'Названия в базе на IOS': ['RelyVPN - WiFi Proxy Master',]
    },
    {
    'Номер': 152,
    'Название на Android': 'Yoga VPN - безопасный прокси',
    'Название на IOS': 'Yoga VPN - Protect Security',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['Yoga VPN - безопасный прокси',],
    'Названия в базе на IOS': ['Yoga VPN - Protect Security',]
    },
    {
    'Номер': 153,
    'Название на Android': 'PrivateVPN',
    'Название на IOS': 'PrivateVPN',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': True,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['PrivateVPN',],
    'Названия в базе на IOS': ['PrivateVPN',]
    },
    {
    'Номер': 154,
    'Название на Android': 'FlashVPN Fast VPN Proxy',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['FlashVPN Fast VPN Proxy',],
    'Названия в базе на IOS': []
    },
    {
    'Номер':155,
    'Название на Android': 'VPN Bucks - Fast VPN Proxy',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': True,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['VPN Bucks - Fast VPN Proxy',],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 156,
    'Название на Android': 'VPN Turkey - VPN в Турции',
    'Название на IOS': 'Отсутствует',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': ['VPN Turkey - VPN в Турции'],
    'Названия в базе на IOS': []
    },
    {
    'Номер': 157,
    'Название на Android': 'VPN - Super VPN Proxy',
    'Название на IOS': 'VPN - Super VPN Proxy',
    'Другие названия на Android': [],
    'Другие названия на IOS': [],
    'Наличие в магазине Android': False,
    'Наличие в магазине IOS': False,
    'Дата начала измерений': '01.05.2023',
    'Блокируется': True,
    'Названия в базе на Android': [],
    'Названия в базе на IOS': []
    },

]



 	


    # ,
    # {
    # 'Номер':,
    # 'Название на Android':'',
    # 'Название на IOS':'',
    # 'Другие названия на Android':[],
    # 'Другие названия на IOS':[],
    # 'Наличие в магазине Android': ,
    # 'Наличие в магазине IOS': ,
    # 'Дата начала измерений':'',
    # 'Блокируется': ,
    # 'Названия в базе на Android':[],
    # 'Названия в базе на IOS':[]
    # }


























from django_plotly_dash import DjangoDash
df = pd.read_json(settings.STATICFILES_DIRS[0] + '/board/data/weeked.json') #
app = DjangoDash('dynamic_graph')

# df = pd.read_json('Z:/Work_Projects_Dir/DashBoard_V0.3 — копия/dash_board/static/board/data/weeked.json') # settings.STATICFILES_DIRS[0] + '/board/data/weeked.json'
# app = Dash(__name__)



df = df.groupby(['operator_names', 'os_names', 'vpn_android', 'vpn_ios', 'sorting_date', 'created']).agg({'mean_web': ['mean'], 'mean_app': ['mean'], 'mean_all': ['mean']}). reset_index() 
# Переименование колонок, иехническая необходимость
df.columns = ['operator_names', 'os_names', 'vpn_android', 'vpn_ios', 'sorting_date', 'created', 'mean_web', 'mean_app', 'mean_all']
# print(df)
df.sort_values(by='sorting_date', inplace=True)
df.reset_index(drop=True, inplace=True)
# print(df)


def df_names_remaker(df1):
    df_names_to_change = df1[(df1['Наличие в магазине Android'] == False) & (df1['Наличие в магазине IOS'] == False)]
    android_names = df_names_to_change['Название на Android'].values.tolist()
    ios_names = df_names_to_change['Название на IOS'].values.tolist()
    df2 = df1[(~df1['Название на Android'].isin(android_names)) & (~df1['Название на IOS'].isin(ios_names))]
    df3 = df1[(df1['Название на Android'].isin(android_names)) & (df1['Название на IOS'].isin(ios_names))]
    df2.reset_index(drop=True, inplace=True)
    df3.reset_index(drop=True, inplace=True)
    for i in range(df3.shape[0]):
        df1.replace(df3.iloc[i]['Название на Android'], df3.iloc[i]['Название на Android'] + ' (Недоступен для скачивания)', inplace=True) 
    # print(df1[(df1['Наличие в магазине Android'] == False) & (df1['Наличие в магазине IOS'] == False)])
    df1.insert(0, 'Название на IOS красивое', "-/-", True)
    df1.insert(0, 'Название на Android красивое', "-/-", True)
    for j in range(df1.shape[0]):
        if df1.iloc[j]['Наличие в магазине Android'] and df1.iloc[j]['Наличие в магазине IOS']:
            df1.at[j, 'Название на IOS красивое'] = df1.iloc[j]['Название на IOS'] + ' (A/I)'
            df1.at[j, 'Название на Android красивое'] = df1.iloc[j]['Название на Android'] + ' (A/I)'
        elif df1.iloc[j]['Наличие в магазине Android'] and not df1.iloc[j]['Наличие в магазине IOS']:
            df1.at[j, 'Название на IOS красивое'] = df1.iloc[j]['Название на IOS'] + ' (A/-)'
            df1.at[j, 'Название на Android красивое'] = df1.iloc[j]['Название на Android'] + ' (A/-)'
        elif not df1.iloc[j]['Наличие в магазине Android'] and df1.iloc[j]['Наличие в магазине IOS']:
            df1.at[j, 'Название на IOS красивое'] = df1.iloc[j]['Название на IOS'] + ' (-/I)'
            df1.at[j, 'Название на Android красивое'] = df1.iloc[j]['Название на Android'] + ' (-/I)'
        elif not df1.iloc[j]['Наличие в магазине Android'] and not df1.iloc[j]['Наличие в магазине IOS']:
            df1.at[j, 'Название на IOS красивое'] = df1.iloc[j]['Название на IOS'] + ' (-/-)'
            df1.at[j, 'Название на Android красивое'] = df1.iloc[j]['Название на Android'] + ' (-/-)'
    # print(df1)
    return df1



def form_vpn_list(kind):
    if kind == 1:
        vp = []
        df = pd.DataFrame(vpn_info_dictionary)
        df = df_names_remaker(df)
        for i in range(df.shape[0]):
            if df.iloc[i]['Название на Android'] != 'Отсутствует':
                vp.append(df.iloc[i]['Название на Android красивое'])
            else:
                vp.append(df.iloc[i]['Название на IOS красивое'])
        # print(vp)
        return vp
    elif kind == 2:
        vp = []
        df = pd.DataFrame(vpn_info_dictionary)
        df = df_names_remaker(df)
        df = df[df['Блокируется'] == True]
        for i in range(df.shape[0]):
            if df.iloc[i]['Название на Android'] != 'Отсутствует':
                vp.append(df.iloc[i]['Название на Android красивое'])
            else:
                vp.append(df.iloc[i]['Название на IOS красивое'])
        # print(vp)
        return vp
    elif kind == 3:
        vp = []
        df = pd.DataFrame(vpn_info_dictionary)
        df = df_names_remaker(df)
        df = df[df['Блокируется'] == False]
        for i in range(df.shape[0]):
            if df.iloc[i]['Название на Android'] != 'Отсутствует':
                vp.append(df.iloc[i]['Название на Android красивое'])
            else:
                vp.append(df.iloc[i]['Название на IOS красивое'])
        # print(vp)
        return vp


paper_bg_color = 'rgba(0,0,0,0)'
bg_color = 'rgba(0,0,0,0)'
text_color = '#ffffff'

mts_counter = 0
tele2_counter = 0
megafon_counter = 0
beeline_counter = 0
mgts_counter = 0
rostelecom_mobile_counter = 0
rostelecom_counter = 0

def rand_color():
    col = ['#'+''.join([random.choice('123456789ABCDEF') for i in range(6)])]
    # print(col)
    return col

def color_picker(str, arr):
    if str == 'МТС':
        if arr[0] == 0:
            arr[0] = arr[0] + 1
            # print(arr[0])
            return ['red', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'Теле2':
        if arr[1] == 0:
            # print(arr[1])
            arr[1] = arr[1] + 1
            return ['black', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'Мегафон':
        if arr[2] == 0:
            # print(arr[2])
            arr[2] = arr[2] + 1
            return ['green', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'Билайн':
        if arr[3] == 0:
            # print(arr[3])
            arr[3] = arr[3] + 1
            return ['orange', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'МГТС':
        if arr[4] == 0:
            # print(arr[4])
            arr[4] = arr[4] + 1
            return ['darkblue', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'Ростелеком(мобильный)':
        if arr[5] == 0:
            # print(arr[5])
            arr[5] = arr[5] + 1
            return ['darkviolet', arr]
        else:
            return [rand_color()[0], arr]
    if str == 'Ростелеком':
        if arr[6] == 0:
            # print(arr[6])
            arr[6] = arr[6] + 1
            return ['violet', arr]
        else:
            return [rand_color()[0], arr]

# vp = form_vpn_list(1)

df_type = pd.Series(['Любой', 'Заблокированные', 'Незаблокированные'])

text_style = {'font-size': '28px', 'padding-left': '5px', 'text-align': 'center', 'font-family': 'Montserrat, sans-serif', 'color': 'white'}

dropdown_style = {'font-size': '20px', 'padding-left': '5px', 'padding-right': '5px', 'text-align': 'center', 'font-family': 'Montserrat, sans-serif', 'color': '#adcce9', 'margin-bottom': '10px'}
dropdown_inside_style = {'background-color':'white', 'color': 'black', 'text-align': 'left', 'font-family': 'Montserrat, sans-serif', 'border-radius': '5px'}
dropdown_as_is_style = {'flex-basis': 'auto', 'background-color':bg_color, 'margin-bottom': '15px'} # , 'width': '24vw'

style_all_filters = {'background-color':bg_color, 'display': 'flex', 'flex-direction': 'column', 'border-color': '#1f2630', 'font-family': 'Montserrat, sans-serif', 'color': 'white', 'margin-top': '2px'} # ,'width': '99vw'

app.layout = html.Div([
    html.Div(
        children=[
            html.Div([
                html.Div(
                    children=[
                        html.Div('Тип сервиса: ', style=dropdown_style),
                        dcc.Dropdown(df_type.unique(), df_type.unique()[0], multi=False, id='Type', clearable=False, style=dropdown_inside_style),
                    ], style=dropdown_as_is_style),

                html.Div(
                    children=[
                        html.Div('Сервисы: ', style=dropdown_style),
                        dcc.Dropdown(multi=True, id='VPN', searchable=True, clearable=True, optionHeight=50, style=dropdown_inside_style), # vp, vp[0],
                    ], style=dropdown_as_is_style),

                html.Div(
                    children=[
                        html.Div('ОC: ', style=dropdown_style),
                        dcc.Dropdown(df['os_names'].unique(), df['os_names'].unique()[0], multi=True, id='OS', clearable=True, style=dropdown_inside_style),
                    ], style=dropdown_as_is_style),

                html.Div(
                    children=[
                        html.Div('Операторы: ', style=dropdown_style),
                        dcc.Dropdown(df['operator_names'].unique(), df['operator_names'].unique()[0], multi=True, id='Oper', clearable=True, style=dropdown_inside_style),
                    ], style=dropdown_as_is_style),
            ], style=style_all_filters)
    ], style={'padding': 10, 'width': '35vh'}),
    html.Div(
        children=[
            html.Div('Результаты тестирования: ', style=text_style),
            dcc.Graph(id = 'x-time-series')
        ], style={'padding': 10, 'width': '169vh', 'margin-left': '20px'})
], style={'display': 'flex', 'flex-direction': 'row', 'border-bottom': '10px', 'border-color': 'white'}  )#


def create_time_series(dff, VPN, OS, Oper): #City,
    dff.sort_values(by='sorting_date', inplace=True)
    categoryarray_to_push = dff['created'].unique()
    arr = [
        mts_counter,
        tele2_counter,
        megafon_counter,
        beeline_counter ,
        mgts_counter,
        rostelecom_mobile_counter ,
        rostelecom_counter,
    ]
    fig = go.Figure()
    for v in VPN:
        dff_v = dff[((dff['vpn_android'] == v[0:len(v)-6]) | (dff['vpn_ios'] == v[0:len(v)-6]))]
        # for c in City:
        #     dff_v_c = dff_v[dff_v['city'] == c]
        for o in Oper:
            dff_v_c_o = dff_v[dff_v['operator_names'] == o]
            for os in OS:
                dff_v_c_o_os = dff_v_c_o[dff_v_c_o['os_names'] == os]
                col = color_picker(o, arr)
                arr = col[1]
                fig.add_trace(go.Scatter(
                            x=dff_v_c_o_os['created'], 
                            y=dff_v_c_o_os['mean_all'], 
                            mode='lines+markers',
                            marker=dict(color=col[0], size=8),
                            line=dict(color=col[0], width=3, shape='spline', smoothing = 0),
                            name=v+' - '+ '<br>'+os+' - '+ '<br>'+o, # +c+' - '+ '<br>'
                            textfont=dict(
                            family="Montserrat, sans-serif",
                            size=16,
                            color=text_color)
                            ))
    if len(VPN) > 1 or len(Oper) > 1 or len(OS) > 1:
        new_vpn = []
        for ik in range(len(VPN)):
            new_vpn.append(VPN[ik][0:len(VPN[ik])-6])
        print(VPN)
        VPN = new_vpn
        print(VPN)
        df_for_mean = dff[((dff['vpn_android'].isin(VPN)) | (dff['vpn_ios'].isin(VPN))) & (dff['operator_names'].isin(Oper)) & (dff['os_names'].isin(OS))]
        # print(VPN)
        df_for_mean = df_for_mean.groupby(['sorting_date', 'created']).agg({'mean_web': ['mean'], 'mean_app': ['mean'], 'mean_all': ['mean']}). reset_index() 
        # print(df_for_mean)
        df_for_mean.columns = ['sorting_date', 'created', 'mean_web', 'mean_app', 'mean_all']
        df_for_mean.insert(0, 'operator_names', "Среднее", True)
        # print(df_for_mean)
        fig.add_trace(go.Scatter(
            x=df_for_mean['created'], 
            y=df_for_mean['mean_all'], 
            mode='lines+markers',
            marker=dict(color='#D8D8D8', size=10),
            line=dict(color='#D8D8D8', width=5, shape='spline', dash = 'longdash', smoothing = 0.5),
            name= 'Среднее',
            textfont=dict(
            family='Montserrat, sans-serif',
            size=16,
            color=text_color)
            ))
    fig.update_layout(
        hovermode="y unified",
        paper_bgcolor=paper_bg_color,
        plot_bgcolor=bg_color,
        font=dict(
            family='Montserrat, sans-serif',
            size=12,
            color=text_color
        ),
        height=700,
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),
        modebar_add=[
            'drawline',
            'drawopenpath',
            'drawclosedpath',
            'drawcircle',
            'drawrect',
            'eraseshape'
        ],
        hoverlabel=dict(
            bgcolor='white',
            font=dict(
                color='black',
                family="Montserrat, sans-serif"
            )
        )
    )

    fig.update_xaxes(categoryorder='array', categoryarray= categoryarray_to_push, tickangle = -50)
    fig.update_xaxes(showline=True, linewidth=2, linecolor='#77aad9', gridcolor='#77aad9')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='#77aad9', gridcolor='#77aad9')
    fig.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='#77aad9')
    fig.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='#77aad9')
    fig.update_yaxes(range=[-10, 110])
    return fig

def vpn_list_by_type(type_of_vpn):
    if type_of_vpn == 'Любой':
        vp = form_vpn_list(1)
        return vp
    elif type_of_vpn == 'Заблокированные':
        vp = form_vpn_list(2)
        return vp
    elif type_of_vpn == 'Незаблокированные':
        vp = form_vpn_list(3)
        return vp




@app.callback(
    Output('x-time-series', 'figure'),
    Input('VPN', 'value'),
    # Input('City', 'value'),
    Input('OS', 'value'),
    Input('Oper', 'value'),)
def update_y_timeseries(VPN, OS, Oper): # City, 
    if type(VPN) != type([]):
        VPN = [VPN]
    if type(OS) != type([]):
        OS = [OS]
    if type(Oper) != type([]):
        Oper = [Oper]
    return create_time_series(df, VPN, OS, Oper) # City,

@app.callback(
    Output('VPN', 'options'),
    Output('VPN', 'value'),
    Input('Type', 'value'),)
def update_y_timeseries(Type): # City, 
    list_of_vpn = vpn_list_by_type(Type)
    # print(c)
    return list_of_vpn, list_of_vpn[0] # City,


# if __name__ == '__main__':
#     app.run_server(debug=True, port='16600')




