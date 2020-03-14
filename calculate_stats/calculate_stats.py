import csv
import matplotlib.pyplot as plt

# Denumirea fisierului CSV
csv_file_name = 'infected_covid19_md.csv'

# Exportarea datelor din csv, returneaza o lista mare de date
def export_data(csv_file_name):
    export_data = []
    with open(csv_file_name, 'r') as csv_data:
        csv_reader = csv.reader(csv_data)
        next(csv_reader)
        for line in csv_reader:
            export_data.append(line)
    csv_data.close()
    return export_data

# Variabila care contine rezultatul exportului din CSV
export_data_var = export_data(csv_file_name)

# Numarul de persoane total infectate, la intrare primeste variabila de date
def num_of_persons(data_from_csv):
    return len(data_from_csv)

# Numarul de persoane filtrate prin sex, la intrare primeste variabila de date
def sort_by_sex(data_from_csv):
    m,f,unknown = 0,0,0
    sort_by_sex = {}
    sort_by_sex['persons'] = []
    for person in data_from_csv:
        if person[2] == 'M':
            m = m + 1
        elif person[2] == 'F':
            f = f + 1
        else:
            unknown = unknown + 1
    sort_by_sex['persons'].append({'Total':len(data_from_csv),'M':m, 'F':f,'Nu sunt date':unknown})
    return sort_by_sex

# Numarul de persone infectate in fiicare zi, la intrare primeste variabila de date
def infected_each_day(data_from_csv):
    date_from_every_list = []
    num_of_infect_in_day = {}
    num_of_infect_in_day['dates'] = []
    for date in data_from_csv:
        date_from_every_list.append(date[0])
    for exact_date in date_from_every_list:
            if date_from_every_list.count(exact_date) > 1:
                num_of_infect_in_day['dates'].append({exact_date:date_from_every_list.count(exact_date)})
                while date_from_every_list.count(exact_date) > 1:
                    date_from_every_list.remove(exact_date)
            else:
                num_of_infect_in_day['dates'].append({exact_date:date_from_every_list.count(exact_date)})
    return num_of_infect_in_day

# Numarul de persoane din fiicare raion, la intrare primeste variabila de date
def infected_each_district(data_from_csv):
    dist_from_every_list = []
    num_of_infect_in_dist = {}
    num_of_infect_in_dist['districts'] = []
    for dist in data_from_csv:
        dist_from_every_list.append(dist[3])
    for exact_dist in dist_from_every_list:
        if dist_from_every_list.count(exact_dist) > 1:
            num_of_infect_in_dist['districts'].append({exact_dist:dist_from_every_list.count(exact_dist)})
            while dist_from_every_list.count(exact_dist) > 1:
                dist_from_every_list.remove(exact_dist)
        else:
            num_of_infect_in_dist['districts'].append({exact_dist:dist_from_every_list.count(exact_dist)})
    return num_of_infect_in_dist

# Histograma, prima valoare primita este numarul total de prsoane, a doua variabila cu date
def infected_age_histogram(num_of_persons,data_from_csv):
    ages_list = []
    for ages in data_from_csv:
            ages_list.append(ages[4])
    ages_list.sort()
    plt.hist(ages_list, bins=num_of_persons, edgecolor='black')
    plt.show()
