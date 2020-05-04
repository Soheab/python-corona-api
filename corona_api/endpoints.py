_SORT_SUFFIX = '?sort={}'
_YESTERDAY_SUFFIX = '?yesterday=true'
_YESTERDAY_SORTED = '?yesterday=true&sort={}'

GLOBAL_DATA = '{}/all'
GLOBAL_YESTERDAY = GLOBAL_DATA + _YESTERDAY_SUFFIX

ALL_COUNTRIES = '{}/countries'
ALL_COUNTRIES_SORTED = ALL_COUNTRIES + _SORT_SUFFIX
ALL_COUNTRIES_YESTERDAY = ALL_COUNTRIES + _YESTERDAY_SUFFIX
ALL_COUNTRIES_YESTERDAY_SORTED = ALL_COUNTRIES + _YESTERDAY_SORTED

COUNTRY_DATA = '{}/countries/{}'
COUNTRY_DATA_YESTERDAY = COUNTRY_DATA + _YESTERDAY_SUFFIX

ALL_STATES = '{}/states'
ALL_STATES_SORTED = ALL_STATES + _SORT_SUFFIX
ALL_STATES_YESTERDAY = ALL_STATES + _YESTERDAY_SUFFIX
ALL_STATES_YESTERDAY_SORTED = ALL_STATES + _YESTERDAY_SORTED

SINGLE_STATE = '{}/states/{}'
SINGLE_STATE_YESTERDAY = SINGLE_STATE + _YESTERDAY_SUFFIX

HISTORICAL_COUNTRY = '{}/historical/{}?lastdays={}'
HISTORICAL_PROVINCE = '{}/historical/{}/{}?lastdays={}'
STATE_COUNTY = '{}/historical/usacounties/{}?lastdays={}'

ALL_CONTINENTS = '{}/continents'
ALL_CONTINENTS_SORTED = ALL_CONTINENTS + _SORT_SUFFIX
ALL_CONTINENTS_YESTERDAY = ALL_CONTINENTS + _YESTERDAY_SUFFIX
ALL_CONTINENTS_YESTERDAY_SORTED = ALL_CONTINENTS + _YESTERDAY_SORTED

CONTINENT_DATA = '{}/continents/{}'
CONTINENT_YESTERDAY = CONTINENT_DATA + _YESTERDAY_SUFFIX

JHU_CSSE = '{}/jhucsse'
JHU_CSSE_COUNTIES = '{}/jhucsse/counties/{}'

NYT_USA = '{}/nyt/usa'
NYT_ALL_STATES = '{}/nyt/states'
NYT_SINGLE_STATE = '{}/nyt/states/{}'
NYT_ALL_COUNTIES = '{}/nyt/counties'
NYT_SINGLE_COUNTY = '{}/nyt/counties/{}'

APPLE_COUNTRIES = '{}/apple/countries'
APPLE_SUBREGIONS = APPLE_COUNTRIES + '/{}'
APPLE_SINGLE_SUBREGION = APPLE_SUBREGIONS + '/{}'