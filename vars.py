file_name_raw = 'data/phonebook_raw.csv'
file_name_formated = 'phonebook.csv'

# last version
# '^(\w*)(,|\s?)(\w*)(,|\s?)(\w*)(,?)(,?)(,?)(\w*)(,?)([\w\s\–]*)(,?)((\+7\s?|8)?([(\s]?)(\d{3})([)|\s]?)([-\s]*)(\d{3})([-\s]*)(\d{2})([-\s]*)(\d{2})(\s*)(\(?)([\w.]*)(\s*)(\d*)(\)?))?(,?)([\w@.]*)'
# lastname - \1
# name - \3
# surname - \5
# organisation - \9
# position - \11
# country_code - \14
# city_code - \16
# xxx - \19
# xx - \21
# xx - \23
# additional number - \28
# email - \31

pattern_all = (
    r'^(\w*)(,|\s?)(\w*)(,|\s?)(\w*)(,?)(,?)(,?)(\w*)(,?)([\w\s\–]*)(,?)((\+7\s?|8)?([(\s]?)(\d{3})([)|\s]?)([-\s]*)(\d{3})([-\s]*)(\d{2})([-\s]*)(\d{2})(\s*)(\(?)([\w.]*)(\s*)(\d*)(\)?))?(,?)([\w@.]*)')
str_replace = r'\1,\3,\5,\9,\11,+7(\16)\19-\21-\23 \26\28,\31,'
str_pattern_empty_phone = '\+7\(\)-- '

index_from_diff = 3