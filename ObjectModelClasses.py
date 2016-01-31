__author__ = 'Tom'
__author__ = 'Tom'
import PropertyDataGenerators as generate
import random


# id generator
def id_chooser():
    id_list = [1, 2, 3, 4, 5, 6, 7, 8]
    return  "\'" + str(random.choice(id_list)) + "\'",

#### as you can see to do is check the right data types match up to db and that there are apostrophes enclosing every element
### next to do is change everything from objects to dicts
currencies = {
    'id': id_chooser()
    'name': '\'fdd\'',
    'name_native': '\'fdd\'',
    'iso4217_alpha3': '\'fdd\'',
    'iso4217_num3': '\'gfd\'',
    'symbol': '\'h\''
}

continents = {
    'id': generate.get_rand_int(17),
    'name': generate.get_rand_text(11, 5)
}

countries = {
    'id': id_chooser(),
    'common_name': generate.get_rand_text(11, 5),
    'formal_name': generate.get_rand_text(11, 5),
    'continent_id': generate.get_rand_int(17),
    'currency_id': generate.get_rand_int(17),
    'type': generate.get_rand_text(11, 5),
    'capital': generate.get_rand_text(11, 5),
    'telephone_code': generate.get_rand_int(3),
    'letter_code_2': generate.get_rand_int(2),
    'letter_code_3': generate.get_rand_int(3),
    'iana_country_code': generate.get_rand_int(4),
    'lng': generate.get_rand_positive_double(700),
    'lat': generate.get_rand_positive_double(700),
    'developing_country': generate.get_rand_boolean()
}

languages = {
        'id': id_chooser(),
        'name': generate.get_rand_text(11, 5),
        'name_native': generate.get_rand_text(20, 5),
        'code': generate.get_rand_text(4, 2)
}

platforms = {
        'id': id_chooser(),
        'name': generate.get_rand_text(11, 5),
        'url': generate.get_rand_text(11, 5),
        'year_founded': generate.get_rand_int(4),
        'created_at': generate.get_current_timestamp()
}


world_bank_rankings = {
        'id': id_chooser(),
        'rank': generate.get_rand_int(3),
        'country_id': generate.get_rand_int(3),
        'created_at': generate.get_current_timestamp()
}

projects = {
        'id': id_chooser(),
        'platform_id': generate.get_rand_int(17),
        'url': generate.get_rand_text(101, 5),
        'external_project_id': generate.get_rand_text(11, 5),
        'start_date': generate.get_current_timestamp(),
        'currency_date': generate.get_current_timestamp(),
        'language_id': generate.get_rand_int(17),
        'country_id': generate.get_rand_int(17),
        'created_at': generate.get_current_timestamp()
}


types = {
        'id': id_chooser(),
        'name': generate.get_rand_text(11, 5)
        'created_at': generate.get_current_timestamp()


class Platform_Reviews:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.notes = generate.get_rand_text(110, 5)
        self.created_at = generate.get_current_timestamp()
        self.updated_at = generate.get_current_timestamp()


class Platform_Status_Descriptions:
    def __init__(self):
        self.code = self.name = generate.get_rand_text(30, 5)
        self.description = generate.get_rand_text(101, 5)
        self.created_at = generate.get_current_timestamp()
        self.created_at = generate.get_current_timestamp()


class Project_Status_Description:
    def __init__(self):
        self.code = generate.get_rand_text(20, 5)
        self.description = generate.get_rand_text(110, 5)
        self.created_at = generate.get_current_timestamp()
        self.created_at = generate.get_current_timestamp()


class Project_Updates:
    def __init__(self):
        'id': id_chooser(),
        self.project_id = generate.get_rand_int(17)
        self.description = generate.get_rand_text(110, 5)
        self.created_at = generate.get_current_timestamp()
        self.created_at = generate.get_current_timestamp()



class Platform_Types:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.type_id = generate.get_rand_int(17)
        self.version_id = generate.get_rand_int(17)
        self.percentage = generate.get_rand_positive_double(100)
        self.created_at = generate.get_current_timestamp()


class Platform_Countries:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.country_id = generate.get_rand_int(17)
        self.version_id = generate.get_rand_int(17)
        self.percentage = generate.get_rand_positive_double(100)
        self.created_at = generate.get_current_timestamp()


class Platform_Languages:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.language_id = generate.get_rand_int(17)
        self.version_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Platform_Offices:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.type = generate.get_rand_text(11, 5)
        self.address_line_1 = generate.get_rand_text(15, 5)
        self.address_line_2 = generate.get_rand_text(11, 5)
        self.address_line_3 = generate.get_rand_text(11, 5)
        self.zip = generate.get_rand_text(20, 6)
        self.city = generate.get_rand_text(20, 8)
        self.country_id = generate.get_rand_int(3)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Platform_Stats:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.avg_amount_raised = generate.get_rand_positive_double(5000)
        self.success_rate = generate.get_rand_positive_double(100)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Categories:
    def __init__(self):
        'id': id_chooser(),
        self.name = generate.get_rand_text(11, 5)
        self.created_at = generate.get_current_timestamp()
        self.created_at = generate.get_current_timestamp()


class Platform_Descriptions:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.motto = generate.get_rand_text(11, 5)
        self.description = generate.get_rand_text(500, 5)
        self.mini_description = generate.get_rand_text(40, 5)
        self.logo_url = generate.get_rand_text(101, 5)
        self.developing_world = generate.get_rand_boolean()
        self.api = generate.get_rand_boolean()
        self.directly_funded = generate.get_rand_boolean()
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Platform_Fees:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.percentage = generate.get_rand_positive_double(100)
        self.fixed = generate.get_rand_positive_double(100)
        self.version_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Social_Media_Sites:
    def __init__(self):
        'id': id_chooser(),
        self.name = generate.get_rand_text(11, 5)
        self.created_at = generate.get_current_timestamp()


class Platform_Statuses:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.code = generate.get_rand_text(11, 5)
        self.version_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Platform_Currency:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.currency_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Location:
    def __init__(self):
        'id': id_chooser(),
        self.project_id = generate.get_rand_int(17)
        self.address_line_1 = generate.get_rand_text(11, 5)
        self.address_line_2 = generate.get_rand_text(11, 5)
        self.address_line_3 = generate.get_rand_text(11, 5)
        self.zip = generate.get_rand_text(6, 5)
        self.country_id = generate.get_rand_int(3)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Status:
    def __init__(self):
        'id': id_chooser(),
        self.project_id = generate.get_rand_int(17)
        self.url = generate.get_rand_text(41, 5)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Contact:
    def __init__(self):
        'id': id_chooser(),
        self.project_id = generate.get_rand_int(17)
        self.name = generate.get_rand_text(11, 5)
        self.title = generate.get_rand_text(14, 5)
        self.phone_number = generate.get_rand_int(7)
        self.email = generate.get_rand_text(11, 5)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Stats:
    def __init__(self):
        'id': id_chooser(),
        self.project_id = generate.get_rand_int(17)
        self.total_donors = generate.get_rand_int(1)
        self.amount_goal = generate.get_rand_int(3)
        self.amount_raised = generate.get_rand_int(2)
        self.success_rate = generate.get_rand_positive_double(100)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Descriptions:
    def __init__(self):
        'id': id_chooser(),
        self.project_id = generate.get_rand_int(17)
        self.motto = generate.get_rand_text(20,10)
        self.description = generate.get_rand_text(700, 200)
        self.mini_description = generate.get_rand_text(80, 30)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Categories:
    def __init__(self):
        'id': id_chooser(),
        self.project_id = generate.get_rand_int(17)
        self.category_id = generate.get_rand_int(17)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Social_Media_Links:
    def __init__(self):
        'id': id_chooser(),
        self.social_media_site_id = generate.get_rand_int(17)
        self.project_id = generate.get_rand_int(17)
        self.url = generate.get_rand_text(20, 10)
        self.version_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Platform_Contacts:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.name = generate.get_rand_text(17 ,10)
        self.title = generate.get_rand_text(20,10)
        self.phone_number = generate.get_rand_int(7)
        self.email = generate.get_rand_text(20,10)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Platform_Categories_Table:
    def __init__(self):
        'id': id_chooser(),
        self.platform_id = generate.get_rand_int(17)
        self.category_id = generate.get_rand_int(17)
        self.version_id = generate.get_rand_int(17)
        self.percentage = generate.get_rand_positive_double(100)
        self.created_at = generate.get_current_timestamp()


class Users:
    def __init__(self):
        'id': id_chooser(),
        self.name = generate.get_rand_text(17, 10)
        self.email = generate.get_rand_text(20, 10)
        self.password = generate.get_rand_text(8, 10)
        self.remember_token = generate.get_rand_text(40,15)
        self.created_at = generate.get_current_timestamp()
        self.created_at = generate.get_current_timestamp()


class Sessions:
    def __init__(self):
        'id': id_chooser(),
        self.user_id = generate.get_rand_int(17)
        self.ip_address = generate.get_rand_int(9)
        self.user_agent = generate.get_rand_int(17)
        self.payload = generate.get_rand_int(17)
        self.last_activity = generate.get_rand_int(17)


class Password_Reset:
    def __init__(self):
        self.email = generate.get_rand_int(17)
        self.token = generate.get_rand_int(45)
        self.created_at = generate.get_current_timestamp()


class Migration:
    def __init__(self):
        self.migration = generate.get_rand_int(45)
        self.batch = generate.get_rand_int(25)


