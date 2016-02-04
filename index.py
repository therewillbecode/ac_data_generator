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
platform = {'categories' : obj_class.categories,
            'currencies': obj_class.currencies,
            'countries': obj_class.countries,
            'languages': obj_class.languages,
            'platforms': obj_class.platforms,
            'platform_type': obj_class.platform_types,
            'platform_countries': obj_class.platform_countries,
            'platform_language': obj_class.platform_languages,
            'platform_offices': obj_class.platform_offices,
            'platform_stat': obj_class.platform_stats,
            'platform_descriptions': obj_class.platform_descriptions,
            'platform_fee': obj_class.platform_fees,
            'platform_statuses': obj_class.platform_statuses,
            'platform_currencies': obj_class.platform_currencies,
            'platform_contact': obj_class.platform_contacts,
            'platform_categories_table': obj_class.platform_categories_table

            }
# if test works then change these objects to dicts
"""           'world_bank_ranking': obj_class.WorldBankRanking(),

                        'social_media_site': obj_class.Social_Media_Site(),

            """

# id_list = get_id_list(5)
print(platform['platforms'].keys())
print(platform['platforms'].values())


