from pandas import *

population = read_csv('population_by_country_2020.csv')
wo_ha_re = read_csv('world-happiness-report.csv')
wo_ha_re_2021 = read_csv('world-happiness-report-2021.csv')

with option_context('display.max_rows', None, 'display.max_columns', None):
    # sorted_football_spain = football[(football.Nationality == 'Spain') & (football.Wage <= 1000)]
    # sorted_football = football[football.Wage <= 1000]
    # print(len(sorted_football_spain), len(sorted_football))
    # print(100 / len(sorted_football) * len(sorted_football_spain))
    # print(football.describe())
    print(population.describe())
    print(wo_ha_re.describe())
    print(wo_ha_re_2021.describe())
    print("fffjj")
