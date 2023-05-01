from itertools import combinations

names = open('../id_birds.txt', 'r').read().strip('\n').split(',')

ans = []
for comb in combinations(names,4):
    ans.append("{} {}".format(
                      ','.join(sorted(comb)),
                      ','.join(sorted([i for i in names if i not in comb]))
                      )
                  )
    
to_write = open('35_names.txt', 'w')
to_write.write('\n'.join(ans[:35]))
to_write.close()
