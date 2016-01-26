__author__ = 'Tom'
__author__ = 'Tom'
import PropertyDataGenerators as generate
import random
from index import id_list

class Currency:
    def __init__(self):
        self.id = generate.get_rand_int(17)
        self.name = generate.get_rand_text(15, 5)
        self.name_native = generate.get_rand_text(20, 5)
        self.iso4217_alpha3 = generate.get_rand_text(3, 2)
        self.iso4217_num3 = generate.get_rand_text(3, 2)
        self.symbol = generate.get_rand_text(3, 2)


class Continents:
    def __init__(self):
        self.id = generate.get_rand_int(17)
        self.name = generate.get_rand_text(11, 5)


class Country:
    def __init__(self):
        self.id = random.choice(id_list)
        self.common_name = generate.get_rand_text(11, 5)
        self.formal_name = generate.get_rand_text(11, 5)
        self.continent_id = generate.get_rand_int(17)
        self.currency_id = generate.get_rand_int(17)
        self.type = generate.get_rand_text(11, 5)
        self.capital = generate.get_rand_text(11, 5)
        self.telephone_code = generate.get_rand_int(3)
        self.letter_code_2 = generate.get_rand_int(2)
        self.letter_code_3 = generate.get_rand_int(3)
        self.iana_country_code = generate.get_rand_int(4)
        self.lng = generate.get_rand_positive_double(700)
        self.lat = generate.get_rand_positive_double(700)
        self.developing_country = generate.get_rand_boolean()


class Language:
    def __init__(self):
        self.id = random.choice(id_list)
        self.name = generate.get_rand_text(11, 5)
        self.name_native = generate.get_rand_text(20, 5)
        self.code = generate.get_rand_text(4, 2)


class Platform:
    def __init__(self):
        self.id = random.choice(id_list)
        self.name = generate.get_rand_text(11, 5)
        self.url = generate.get_rand_text(11, 5)
        self.year_founded = generate.get_rand_int(4)
        self.created_at = generate.get_current_timestamp()


class WorldBankRanking:
    def __init__(self):
        self.id = random.choice(id_list)
        self.rank = generate.get_rand_int(3)
        self.country_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.url = generate.get_rand_text(101, 5)
        self.external_project_id = generate.get_rand_text(11, 5)
        self.start_date = generate.get_current_timestamp()
        self.currency_date = generate.get_current_timestamp()
        self.language_id = generate.get_rand_int(17)
        self.country_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Type:
    def __init__(self):
        self.id = random.choice(id_list)
        self.name = generate.get_rand_text(11, 5)
        self.created_at = generate.get_current_timestamp()
        self.created_at = generate.get_current_timestamp()

class Platform_Version:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Platform_Review:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.notes = generate.get_rand_text(110, 5)
        self.created_at = generate.get_current_timestamp()
        self.updated_at = generate.get_current_timestamp()


class Platform_Status_Description:
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


class Project_Update:
    def __init__(self):
        self.id = generate.get_rand_int(17)
        self.project_id = generate.get_rand_int(17)
        self.description = generate.get_rand_text(110, 5)
        self.created_at = generate.get_current_timestamp()
        self.created_at = generate.get_current_timestamp()


class Project_Version:
    def __init__(self):
        self.id = random.choice(id_list)
        self.project_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Platform_Type:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.type_id = generate.get_rand_int(17)
        self.version_id = generate.get_rand_int(17)
        self.percentage = generate.get_rand_positive_double(100)
        self.created_at = generate.get_current_timestamp()


class Platform_Countries:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.country_id = generate.get_rand_int(17)
        self.version_id = generate.get_rand_int(17)
        self.percentage = generate.get_rand_positive_double(100)
        self.created_at = generate.get_current_timestamp()


class Platform_Language:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.language_id = generate.get_rand_int(17)
        self.version_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Platform_Office:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.type = generate.get_rand_text(11, 5)
        self.address_line_1 = generate.get_rand_text(15, 5)
        self.address_line_2 = generate.get_rand_text(11, 5)
        self.address_line_3 = generate.get_rand_text(11, 5)
        self.zip = generate.get_rand_text(6)
        self.city = generate.get_rand_text(8)
        self.country_id = generate.get_rand_int(3)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Platform_Stat:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.avg_amount_raised = generate.get_rand_positive_double(5000)
        self.success_rate = generate.get_rand_positive_double(100)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Category:
    def __init__(self):
        self.id = random.choice(id_list)
        self.name = generate.get_rand_text(11, 5)
        self.created_at = generate.get_current_timestamp()
        self.created_at = generate.get_current_timestamp()


class Platform_Description:
    def __init__(self):
        self.id = random.choice(id_list)
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


class Platform_Fee:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.percentage = generate.get_rand_positive_double(100)
        self.fixed = generate.get_rand_positive_double(100)
        self.version_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Social_Media_Site:
    def __init__(self):
        self.id = random.choice(id_list)
        self.name = generate.get_rand_text(11, 5)
        self.created_at = generate.get_current_timestamp()


class Platform_Status:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.code = generate.get_rand_text(11, 5)
        self.version_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Platform_Currency:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.currency_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Location:
    def __init__(self):
        self.id = random.choice(id_list)
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
        self.id = random.choice(id_list)
        self.project_id = generate.get_rand_int(17)
        self.url = generate.get_rand_text(41, 5)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Contact:
    def __init__(self):
        self.id = random.choice(id_list)
        self.project_id = generate.get_rand_int(17)
        self.name = generate.get_rand_text(11, 5)
        self.title = generate.get_rand_text(14, 5)
        self.phone_number = generate.get_rand_int(7)
        self.email = generate.get_rand_text(11, 5)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Stats:
    def __init__(self):
        self.id = random.choice(id_list)
        self.project_id = generate.get_rand_int(17)
        self.total_donors = generate.get_rand_int(1)
        self.amount_goal = generate.get_rand_int(3)
        self.amount_raised = generate.get_rand_int(2)
        self.success_rate = generate.get_rand_positive_double(100)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Description:
    def __init__(self):
        self.id = random.choice(id_list)
        self.project_id = generate.get_rand_int(17)
        self.motto = generate.get_rand_text(20,10)
        self.description = generate.get_rand_text(700, 200)
        self.mini_description = generate.get_rand_text(80, 30)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Category:
    def __init__(self):
        self.id = random.choice(id_list)
        self.project_id = generate.get_rand_int(17)
        self.category_id = generate.get_rand_int(17)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Project_Social_Media_Links:
    def __init__(self):
        self.id = random.choice(id_list)
        self.social_media_site_id = generate.get_rand_int(17)
        self.project_id = generate.get_rand_int(17)
        self.url = generate.get_rand_text(20, 10)
        self.version_id = generate.get_rand_int(17)
        self.created_at = generate.get_current_timestamp()


class Platform_Contact:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.name = generate.get_rand_text(17 ,10)
        self.title = generate.get_rand_text(20,10)
        self.phone_number = generate.get_rand_int(7)
        self.email = generate.get_rand_text(20,10)
        self.version_id = generate.get_rand_int(3)
        self.created_at = generate.get_current_timestamp()


class Platform_Categories_Table:
    def __init__(self):
        self.id = random.choice(id_list)
        self.platform_id = generate.get_rand_int(17)
        self.category_id = generate.get_rand_int(17)
        self.version_id = generate.get_rand_int(17)
        self.percentage = generate.get_rand_positive_double(100)
        self.created_at = generate.get_current_timestamp()


class User:
    def __init__(self):
        self.id = random.choice(id_list)
        self.name = generate.get_rand_text(17, 10)
        self.email = generate.get_rand_text(20, 10)
        self.password = generate.get_rand_text(8, 10)
        self.remember_token = generate.get_rand_text(40,15)
        self.created_at = generate.get_current_timestamp()
        self.created_at = generate.get_current_timestamp()


class Session:
    def __init__(self):
        self.id = random.choice(id_list)
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


