__author__ = 'Tom'
__author__ = 'Tom'
import PropertyDataGenerators as generate
import random


# id generator
def id_chooser():
    id_list = [1, 2, 3, 4, 5, 6, 7, 8]
    res = "\'" + str(random.choice(id_list)) + "\'"
    print(res)
    return res



categories = {
        'id': '5',
        'name': generate.get_rand_text(11, 5),
        'created_at': generate.get_current_timestamp(),
        'updated_at': generate.get_current_timestamp()
}


#### as you can see to do is check the right data types match up to db and that there are apostrophes enclosing every element
### next to do is change everything from objects to dicts
currencies = {
    'id': id_chooser(),
    'name': '\'fdd\'',
    'name_native': '\'fdd\'',
    'iso4217_alpha3': '\'fdd\'',
    'iso4217_num3': '\'gfd\'',
    'symbol': '\'h\''
   # 'version_id': '1'
}

continents = {
    'id': '5',
    'name': generate.get_rand_text(11, 5),
}

countries = {
    'id': '5',
    'common_name': generate.get_rand_text(11, 5),
    'formal_name': generate.get_rand_text(11, 5),
    'continent_id': '5',
    'currency_id': id_chooser(),
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
        'id': '5',
        'name': generate.get_rand_text(11, 5),
        'name_native': generate.get_rand_text(20, 5),
        'code': '\'gfd\''
}

platforms = {
        'id': '5',
        'name': generate.get_rand_text(11, 5),
        'url': generate.get_rand_text(11, 5),
        'year_founded': generate.get_rand_int(4),
        'created_at': generate.get_current_timestamp(),
        'platform_id;': id_chooser()
}


world_bank_rankings = {
        'id': '5',
        'rank': generate.get_rand_int(3),
        'country_id': id_chooser(),
        'created_at': generate.get_current_timestamp()
}

projects = {
        'id': '5',
        'platform_id': id_chooser(),
        'url': generate.get_rand_text(101, 5),
        'external_project_id': generate.get_rand_text(11, 5),
        'start_date': generate.get_current_timestamp(),
        'currency_date': generate.get_current_timestamp(),
        'language_id': id_chooser(),
        'country_id': id_chooser(),
        'created_at': generate.get_current_timestamp()
}


types = {
        'id': '5',
        'name': generate.get_rand_text(11, 5),
        'created_at': generate.get_current_timestamp()
}

platform_reviews = {
    'id': '5',
    'platform_id': id_chooser(),
    'notes': generate.get_rand_text(110, 5),
    'created_at': generate.get_current_timestamp(),
    'updated_at': generate.get_current_timestamp()
}


platform_status_descriptions = {
        'code': 'GHL5',
        'description': generate.get_rand_text(101, 5),
        'created_at': generate.get_current_timestamp()
}


platform_contacts = {
        'id': '5',
        'platform_id': id_chooser(),
        'name': generate.get_rand_text(17 ,10),
        'title': generate.get_rand_text(20,10),
        'phone_number': generate.get_rand_int(7),
        'email': generate.get_rand_text(20,10),
        'version_id': id_chooser(),
        'created_at': generate.get_current_timestamp()
}

platform_categories_table ={
        'id': '5',
        'platform_id': id_chooser(),
        'category_id': '5',
        'version_id': id_chooser(),
        'percentage': generate.get_rand_positive_double(3),
        'created_at': generate.get_current_timestamp()
}


platform_types = {
        'id': '5',
        'platform_id': id_chooser(),
        'type_id': id_chooser(),
        'version_id': id_chooser(),
        'percentage': generate.get_rand_positive_double(3),
        'created_at': generate.get_current_timestamp()
}

platform_countries = {
       'id': '5',
       'platform_id': id_chooser(),
       'country_id': '5',
       'version_id': id_chooser(),
       'percentage': generate.get_rand_positive_double(3),
       'created_at': generate.get_current_timestamp()
}

platform_languages = {
        'id': '5',
        'platform_id': id_chooser(),
        'language_id': id_chooser(),
        'version_id': id_chooser(),
        'created_at': generate.get_current_timestamp()
}

platform_offices = {
        'id': '5',
        'platform_id': id_chooser(),
        'type': generate.get_rand_text(11, 5),
        'address_line_1': generate.get_rand_text(11, 5),
        'address_line_2': generate.get_rand_text(11, 5),
        'address_line_3': generate.get_rand_text(11, 5),
        'zip': generate.get_rand_text(8, 4),
        'city': generate.get_rand_text(8, 4),
        'country_id': '5',
        'version_id': id_chooser(),
        'created_at': generate.get_current_timestamp()
}

platform_stats = {
        'id':'5',
        'platform_id': '5',
        'avg_amount_raised': generate.get_rand_positive_double(5000),
        'success_rate': generate.get_rand_positive_double(100),
        'version_id': id_chooser(),
        'created_at': generate.get_current_timestamp()
}


platform_fees = {
        'id': '5',
        'platform_id': '5',
        'percentage': generate.get_rand_positive_double(100),
        'fixed': generate.get_rand_positive_double(100),
        'version_id': id_chooser(),
        'created_at': generate.get_current_timestamp()
}

platform_statuses = {
        'id': '5',
        'platform_id': '5',
        'code': 'GHL5',
        'version_id': id_chooser(),
        'created_at': generate.get_current_timestamp()
}

platform_currencies = {
        'id': '5',
        'platform_id': '5',
        'currency_id': '5',
        'created_at': generate.get_current_timestamp()
}


platform_descriptions = {
        'id': '5',
        'platform_id': '5',
        'motto': generate.get_rand_text(11, 5),
        'description': generate.get_rand_text(500, 5),
        'mini_description': generate.get_rand_text(40, 5),
        'logo_url': generate.get_rand_text(101, 5),
        'developing_world': generate.get_rand_boolean(),
        'api': generate.get_rand_boolean(),
        'directly_funded': generate.get_rand_boolean(),
        'version_id': id_chooser(),
        'created_at': generate.get_current_timestamp()
}


"""
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

class Social_Media_Sites:
    def __init__(self):
        'id': id_chooser(),
        self.name = generate.get_rand_text(11, 5)
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

"""
