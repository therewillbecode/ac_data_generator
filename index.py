import json
import ObjectModelClasses as obj_class
import inspect


def get_id_list(length):
    return [x for x in range(0, length)]


def get_array(amount, class_name):
    """returns array of multiple objects"""

    arr = []
    for i in range(0, amount):
        arr.append(class_name)
    return arr


def write_to_json(file_name, data):
    """ dump data to json file """

    file_name = file_name.join('.json')
    output_file = open(file_name, "w")
    json.dump(data, output_file, indent=4)
    write_to_json('gg', data)
    output_file.close()

# test first with limited number of elements
platform = {'currencies': obj_class.currencies,
            'countries': obj_class.countries,
            'languages': obj_class.languages,
            'platforms': obj_class.platforms,
            }
# if test works then change these objects to dicts
"""           'world_bank_ranking': obj_class.WorldBankRanking(),
            'platform_type': obj_class.Platform_Type(),
            'platform_countries': obj_class.Platform_Countries(),
            'platform_language': obj_class.Platform_Language(),
            'platform_office': obj_class.Platform_Office(),
            'platform_stat': obj_class.Platform_Stat(),
            'platform_category': obj_class.Category(),
            'platform_description': obj_class.Platform_Description(),
            'platform_fee': obj_class.Platform_Fee(),
            'social_media_site': obj_class.Social_Media_Site(),
            'platform_status': obj_class.Platform_Status(),
            'platform_currency': obj_class.Platform_Currency(),
            'platform_contact': obj_class.Platform_Contact(),
            'platform_categories_table': obj_class.Platform_Categories_Table()
            """

# id_list = get_id_list(5)

