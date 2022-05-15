from os.path import dirname


file = open(dirname(__file__) + '/best_score.txt', 'r')
best_score = int(file.readline())
best_score += 100
file = open(dirname(__file__) + '/best_score.txt', 'w')
file.write(str(best_score))


file.close()