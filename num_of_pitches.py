#inputs for centraliser calcualtion

#test for github

Total_Pipeline_Length = 16860   #unit m
Joint_Length = 18.1 #unit m
Exculsion_Zone = 0.4 #unit m, +/- distance to the welds
Max_Centraliser_Pitch = 2.15 #unit m, from centraliser center to center
First_Centraliser_Location = 1.08 #unit m, the locaiton of the first centralsier

with open('listing_centraliser.txt', 'w') as f:
    f.write('Total_Pipeline_Length (m): {} \n'.format(Total_Pipeline_Length))
    f.write('Joint_Length (m): {} \n'.format(Joint_Length))
    f.write('Exculsion_Zone to Girth Weld +/- (m): {} \n'.format(Exculsion_Zone))
    f.write('Max_Centraliser_Pitch (m): {} \n'.format(Max_Centraliser_Pitch))
    f.write('First_Centraliser_Location (m): {} \n'.format(First_Centraliser_Location))
    f.write('{} \n'.format('')) #print two blank lines
    f.write('{} \n'.format(''))


ranges = []
n = 0
num_of_p = 0

while n < Total_Pipeline_Length:
    ranges.append((n+Joint_Length-Exculsion_Zone, n+Joint_Length+Exculsion_Zone))
    n += Joint_Length
    num_of_p += 1

total_pitch = 0
covered_len = First_Centraliser_Location
Num_Of_C = 1
Num_Of_S = 0 # Num of reuqired shift for centraliser


with open('listing_centraliser.txt', 'a') as f:
    f.write('Num of J, Weld Loc, Num of Cen, Location of Cen \n')
    f.write('{},{:>10} \n'.format(1, round(0,2)))
    f.write('{:>20}, {:>20} \n'.format(Num_Of_C,round(covered_len,2)))


#while(ranges)
for n in range(0,len(ranges)):
#for n in range(0,5):

    cur_range = ranges.pop(0)
    Weld_Loc = (cur_range[0] + cur_range[1])/2.0
    cur_no_joint = num_of_p - len(ranges)

    Dis_to_Exlusion_Zone = cur_range[0] - covered_len

    while Dis_to_Exlusion_Zone  >= Max_Centraliser_Pitch:
        covered_len =   covered_len + Max_Centraliser_Pitch
        Dis_to_Exlusion_Zone = cur_range[0] - covered_len

        if covered_len < Total_Pipeline_Length:
            Num_Of_C += 1
            with open('listing_centraliser.txt', 'a') as f:
                f.write('{:>20},{:>20} \n'.format(Num_Of_C,round(covered_len,2)))

    if Dis_to_Exlusion_Zone <= Max_Centraliser_Pitch - 2*Exculsion_Zone:
        covered_len = covered_len + Max_Centraliser_Pitch

        if covered_len < Total_Pipeline_Length:
            Num_Of_C += 1
            with open('listing_centraliser.txt', 'a') as f:
                f.write('{:>20},{:>20} \n'.format(Num_Of_C,round(covered_len,2)))

    else:
        covered_len = cur_range[0]
        if covered_len < Total_Pipeline_Length:
            Num_Of_C += 1
            Num_Of_S += 1
            with open('listing_centraliser.txt', 'a') as f:
                f.write('{:>20},{:>20}* \n'.format(Num_Of_C,round(covered_len,2)))

    with open('listing_centraliser.txt', 'a') as f:
            f.write('{},{:>10} \n'.format(cur_no_joint+1, round(Weld_Loc,2)))

with open('listing_centraliser.txt', 'a') as f:
    f.write('{} \n'.format('')) #print two blank lines
    f.write('{} \n'.format(''))
    f.write('Total Number of Centraliser,{:>10} \n'.format(Num_Of_C))
    f.write('Total Number of Shift of Centraliser,{:>10} \n'.format(Num_Of_S))
