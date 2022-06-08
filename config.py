# TELEGRAM
# Токен от BotFather
TG_TOKEN = ''
# ID канала, куда делаем посты
CHANNEL_ID = ''
# Таймаут между отправкой постов в канал
TG_REQUEST_TIMEOUT = 30

# VK
# Токен пользователя
VK_ACCESS_TOKEN = ''
# или
VK_LOGIN = ''
VK_PASSWORD = ''
# Количество постов, запрашиваемых за раз из одного сообщества
COUNTER_PER_REQ = 10
# ID сообществ, от которых будем получать обновления
OWNERS_ID = {
        -83390588: 'Toptovar',
        -141418707: 'plum gun magazine',
        -162270934: 'личная полка',
        -206640804: 'рессейл беларусь',
}

# MAIN
# Таймаут между запросами
MAIN_TIMEOUT = 1200
ATTACHMENTS = True
# HTML шаблон поста в телеграме в соответствии с полями из vk_response_example.json (в 'items') из корневой
# директории + есть возможность использовать 'signer_name', если у ответа есть поле 'signer_id'
POST_HTML_TEMPLATE = "<b>%owner_name</b>\n\n%text\n\n<b>Продавец: </b><a href=\"https://vk.com/id%signer_id\">" \
                     "%signer_name</a>"

# ADDITIONAL
# Если заполнен, выполняет поиск по тексту по указанным ключевым словам и добавляет соответствующие хэштэги к посту в
# телеграме
TAGS = {'adidas': '#adidas', 'nike': '#nike', 'new balance': '#newbalance', 'reebok': '#reebok',
        'carhartt': '#carhartt', 'jack wolfskin': '#jackwolfskin', "levi’s": '#levis', 'eastpak': '#eastpak',
        'champion': '#champion', 'stussy': '#stussy', 'c.p. company': '#cpcompany', 'dickies': '#dickies',
        'ralph lauren': '#ralphlauren', 'everlast':  '#everlast', 'dolce gabbana': '#dolcegabbana',
        'under armour': '#underarmour', 'burberry': '#burberry', 'saucony': '#saucony', 'supreme': '#supreme',
        'jordan': '#jordan', 'puma': '#puma', 'gap': '#gap', 'lyle&scott': '#lylescott', 'ellesse': '#ellesse',
        'patagonia': '#patagonia', 'tommy hilfiger': '#tommyhilfiger', 'yves saint laurent': '#saintlaurent',
        'obey': '#obey', 'ripndip': '#ripndip', 'stone island': '#stoneisland', 'lacoste': '#lacoste',
        'wrangler': '#wrangler', 'berghaus': '#berghaus', 'balenciaga': '#balenciaga', 'fred perry': '#fredperry',
        'north face': '#thenorthface', 'asics': '#asics', 'vans': '#vans', 'calvin klein': '#calvinklein',
        'guess': '#guess', 'alpha industries': '#alphaindustries', 'martens': '#drmartens',
        'helly hansen': '#hellyhanses',
        'weekend offender': '#weekendoffender', 'lee': '#lee', 'napapijri': '#napapijri', 'kappa': '#kappa',
        'fila': '#fila', 'lyle scott': '#lylescott', 'hundreds': '#thehundreds', 'edwin': '#edwin',
        'lonsdale': '#lonsdale'
        }
