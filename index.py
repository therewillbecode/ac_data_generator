import json
import ObjectModelClasses as obj_class


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


platform_data = {
    """ Stores all data related to platforms """
    
    'Currency': get_array(70, obj_class.Currency),
    'Country': get_array(300, obj_class.Country),
    'Language': get_array(120, obj_class.Language),
    'Platform': get_array(65, obj_class.Platform),
    'WorldBankRating': get_array(65, obj_class.WorldBankRanking),
    'Platform_Type': get_array(20, obj_class.Platform_Type),
    'Platform_Countries': get_array(100, obj_class.Platform_Countries),
    'Platform_Language:': get_array(40, obj_class.Platform_Language),
    'Platform_Office': get_array(80, obj_class.Platform_Office),
    'Platform_Stat': get_array(65, obj_class.Platform_Stat),
    'Category': get_array(20, obj_class.Category),
    'Platform_Description': get_array(65, obj_class.Platform_Description),
    'Platform_Fee': get_array(65, obj_class.Platform_Fee),
    'Social_Media_Site': get_array(55, obj_class.Social_Media_Site),
    'Platform_Status': get_array(65, obj_class.Platform_Status),
    'Platform_Currency': get_array(65, obj_class.Platform_Currency),
    'Platform_Contact': get_array(65, obj_class.Platform_Contact),
    'Platform_Categories_Table': get_array(100, obj_class.Platform_Categories_Table)
    
}


projects_data = {
    """ Stores all data related to projects """


    'Project': get_array(80000, obj_class.Project),
    'Type': get_array(40, obj_class.Type),
    'Platform_Version': get_array(150, obj_class.Platform_Version),
    'Platform_Review': get_array(65, obj_class.Platform_Review),
    'Project_Status_Description': get_array(8000, obj_class.Project_Status_Description),
    'Project_Update': get_array(160000, obj_class.Project_Update),
    'Project_Version': get_array(150, obj_class.Currency),
    'Project_Location': get_array(65, obj_class.Project_Description),
    'Project_Status': get_array(80000, obj_class.Project_Status),
    'Project_Contact': get_array(350, obj_class.Project_Contact),
    'Project_Stats': get_array(80000, obj_class.Project_Stats),
    'Project_Description': get_array(80000, obj_class.Project_Description),
    'Project_Category': get_array(30, obj_class.Project_Category),
    'Project_Social_Media_Links': get_array(180000, obj_class.Project_Social_Media_Links)
    
}
    

sessions_and_users_data = {
    """ Dict stores all data related to users and sessions """

    'User': get_array(50, obj_class.User),
    'Session': get_array(1000, obj_class.Session),
    'Password_Reset': get_array(200, obj_class.Password_Reset), 
    'Migration': get_array(200, obj_class.Migration)

}


data_collection = {
    """  Entire collections of data objects to be stored in database """    
    
    'Platform': platform_data,
    'Projects': projects_data,
    'Sessions_Users': sessions_and_users_data
    
} 



