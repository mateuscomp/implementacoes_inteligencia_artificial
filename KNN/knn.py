from math import sqrt

def distance(p, q):
    a = (float(p[0]) - float(q[0])) ** 2
    b = (float(p[1]) - float(q[1])) ** 2
    c = (float(p[2]) - float(q[2])) ** 2
    d = (float(p[3]) - float(q[3])) ** 2
    
    return sqrt((a + b + c + d))


def read_trainning_file(name_file, separator_char):
    lista = []
    
    trainning = open(name_file, 'r')
    trainning.readline()
    line = trainning.readline() 
    while(line != ""):
        line_array = line.split(separator_char)
        lista.append(line_array)

        line = trainning.readline()
    trainning.close()
    return lista

def write_answer(rotule):
    answer_file = open('resultado.csv', 'a')
    answer_file.write(content + "\n")
    answer_file.close()

def neighborhood(trainning_list, test, size_max):
    neighbor = []
    #print("Get a trainning list that size is " + str(len(trainning_list)))

    for trainning in trainning_list:
        if(len(neighbor) > 0):
            index_of_insert = len(neighbor)
            
            for i in range(len(neighbor)):
                if (distance(trainning, test) <= distance(neighbor[i], test)): 
                    index_of_insert = i
                    break
            neighbor.insert(index_of_insert, trainning)
                
        else:
            neighbor.append(trainning)

    while(len(neighbor) > size_max): 
        neighbor.pop()

    return neighbor


def to_rank(trainning_list, test, k):
    index_of_rotule = 4

    # Defining neighbor
    neighbors = neighborhood(trainning_list, test, k)
    # print "K = " + str(k) + " neighbors of (" + str(test) + ") are: " + str(neighbors) + "\n\n"

    count_per_rotule = {}
    for neigh in neighbors:
        try:
            count_of_rotule = count_per_rotule[neigh[index_of_rotule][0]]
            count_of_rotule +=1
            count_per_rotule.update({neigh[index_of_rotule][0] : count_of_rotule}) 
        except KeyError as ke:
            count_per_rotule.update({neigh[index_of_rotule][0] : 1})

    print count_per_rotule
    
        

# main
def main():
    k = int(input("Informe k: "))
    trainning_list = read_trainning_file('treinamento.csv', ",")
    
    test_file = open('teste.csv', 'r')
    test_file.readline()
    test_data = test_file.readline()

    while(test_data != ""):
        to_rank(trainning_list, test_data.split(","), k)
        test_data = test_file.readline()

    # write_hit_percentage()

if __name__ == "__main__":
    main()
