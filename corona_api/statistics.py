class GlobalStatistics:
    def __init__(self, cases, deaths, recoveries, today_cases, today_deaths, total_critical, active, infected_countries, updated):
        self.cases = cases
        self.deaths = deaths
        self.recoveries = recoveries
        self.today_cases = today_cases
        self.today_deaths = today_deaths
        self.critical = total_critical
        self.active = active
        self.infected_countries = infected_countries
        self.updated = updated


class CountryInfo:
    def __init__(self, _id, iso2, iso3, _lat, _long, flag):
        self.id = _id
        self.iso2 = iso2
        self.iso3 = iso3
        self.latitude = _lat
        self.longitude = _long
        self.flag = flag


class CountryStatistics:
    def __init__(self, info, name, cases, deaths, recoveries, today_cases, today_deaths, critical, active, cases_per_million, deaths_per_million, updated):
        self.info = info
        self.name = name
        self.cases = cases
        self.deaths = deaths
        self.recoveries = recoveries
        self.today_cases = today_cases
        self.today_deaths = today_deaths
        self.critical = critical
        self.active = active
        self.cases_per_million = cases_per_million
        self.deaths_per_million = deaths_per_million
        self.updated = updated


class StateStatistics:
    def __init__(self, name, cases, deaths, today_cases, today_deaths, active):
        self.name = name
        self.cases = cases
        self.deaths = deaths
        self.today_cases = today_cases
        self.today_deaths = today_deaths
        self.active = active


class HistoryEntry:
    def __init__(self, date, value):
        self.date = date
        self.value = value


class HistoricalStatistics:
    def __init__(self, name, case_history, death_history, recovery_history, province):
        self.name = name
        self.case_history = case_history
        self.death_history = death_history
        self.recovery_history = recovery_history
        self.province = province or 'None'

    
class JhuCsseStatistics:
    def __init__(self, country, province, updated, confirmed_cases, deaths, recoveries, _lat, _long):
        self.country_name = country
        self.province_name = province
        self.updated = updated
        self.confirmed_cases = confirmed_cases
        self.deaths = deaths
        self.recoveries = recoveries
        self.latitude = _lat
        self.longitude = _long