countries = [{"name":'Poland', 'population':38000000},
             {"name":"Ukraine","population":37000000},
             {"name":'Germany','population':80000000},
             {"name":'France',"population":60000000},
             {"name":"Spain","population":48000000},
             {"name":'Canada','population':40000000}
             ]

print('COUNTRY  POPULATION')
print()
for i in countries:
    print(i['name'], i['population'])