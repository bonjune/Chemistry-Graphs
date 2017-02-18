import matplotlib.pyplot as plt

def getRatio(numerator, denominator):
    if type(denominator) != int and type(numerator) != int:
        print('Parameters should be integer : getRatio')
        return
    return numerator / denominator


def buildHydroCarbon(num_carbons):
    hydro_carbons = [] 
    # C_nH_2n-2, C_nH_2n, C_nH_2n+2
    if num_carbons == 1:
        hydro_carbons.append({'name': 'C_1 H-4', 'num_carbons': 1, 'num_hydrogen': 4})
        return hydro_carbons
    for num in range(1, 4):
        num_hydrogen = num_carbons * 2 + 2 * (num-2)
        name = 'C_%d H_%d' %(num_carbons, num_hydrogen)
        hydro_carbons.append({'name': name, 'num_carbons': num_carbons, 'num_hydrogen': num_hydrogen})
    return hydro_carbons

def howMuchOxygenNeeded(hydro_carbons):
    oxygen_needed = hydro_carbons['num_carbons'] + (hydro_carbons['num_hydrogen'] / 4)
    oxygen_needed_per_gram = oxygen_needed / (12*hydro_carbons['num_carbons'] + hydro_carbons['num_hydrogen'])
    return oxygen_needed_per_gram

for step in range(1, 40):
    hydrocarbons = buildHydroCarbon(step)
    # print(hydrocarbons)
    # (ratio, oxygen_needed)
    ratio, oxygen_needed = 0., 0.
    for num in range(1,4):
        if step == 1:
            ratio, oxygen_needed = \
                getRatio(hydrocarbons[0]['num_hydrogen'], hydrocarbons[0]['num_carbons']), howMuchOxygenNeeded(hydrocarbons[0])
        else:
            ratio, oxygen_needed = \
                getRatio(hydrocarbons[num-1]['num_hydrogen'], hydrocarbons[num-1]['num_carbons']), howMuchOxygenNeeded(hydrocarbons[num-1])
        print(ratio, oxygen_needed)
        plt.plot(ratio, oxygen_needed, 'ro')

plt.ylabel('O2 need per gram')
plt.xlabel('H/C ratio')
plt.axis([0, 5, 0.09, 0.135])
plt.show()