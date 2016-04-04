import heapq

class Node(object):

    def __init__(self, name, estimate_to_goal):
        self.name = name
        self.estimate = estimate_to_goal
        self.relationships = []

    def add_relationship(self, relationship):
        self.relationships.append(relationship)

    def __repr__(self):
        return self.name
    

class Relationship(object):
    def __init__(self, to_node, distance):
        self.to_node = to_node
        self.distance = distance

    def __repr__(self):
        return self.to_node.name

#Program: defining datas and relationships
joao_pessoa = Node("joao pessoa", 460)
itabaiana = Node("itabaiana", 360)
campina_grande = Node("campina grande", 300)
santa_rita = Node("santa rita", 451)
mamanguape = Node("mamanguape", 380)
guarabira = Node("guarabira", 340)
areia = Node("areia", 316)
coxixola = Node("coxixola", 232)
soledade = Node("soledade", 243)
picui = Node("picui", 250)
monteiro = Node("monteiro", 195)
patos = Node("patos", 122)
pombal = Node("pombal", 55)
itaporanga = Node("itaporanga", 121)
catole_do_rocha = Node("catole do rocha", 110)
sousa = Node("sousa", 20)
cajazeiras = Node("cajazeiras", 0)

# Adding Relationship
joao_pessoa.add_relationship(Relationship(itabaiana, 68))
joao_pessoa.add_relationship(Relationship(campina_grande, 125))
joao_pessoa.add_relationship(Relationship(santa_rita, 26))

itabaiana.add_relationship(Relationship(campina_grande, 65))

santa_rita.add_relationship(Relationship(mamanguape, 38))
mamanguape.add_relationship(Relationship(guarabira, 42))
guarabira.add_relationship(Relationship(areia, 41))
areia.add_relationship(Relationship(campina_grande, 40))

campina_grande.add_relationship(Relationship(soledade, 58))
campina_grande.add_relationship(Relationship(coxixola, 128))
campina_grande.add_relationship(Relationship(areia, 58))

soledade.add_relationship(Relationship(picui, 69))
soledade.add_relationship(Relationship(patos, 122))

coxixola.add_relationship(Relationship(monteiro, 232))

patos.add_relationship(Relationship(pombal, 55))
patos.add_relationship(Relationship(itaporanga, 108))

pombal.add_relationship(Relationship(catole_do_rocha, 57))
pombal.add_relationship(Relationship(sousa, 56))

sousa.add_relationship(Relationship(cajazeiras, 43))

monteiro.add_relationship(Relationship(itaporanga, 224))
itaporanga.add_relationship(Relationship(cajazeiras, 121))

def add_relationships_node_of_current_node_to_frontier(frontier, current_node):
    for rel in current_node.relationships:
        relationship_node = rel.to_node
        relationship_cost = relationship_node.estimate + rel.distance
        print "Custo total de ", relationship_node, " eh: ", relationship_cost

        index = len(frontier)
        print "Indice inicial alocado: ", index
        
        for i in range(len(frontier)):
            aux_cost = frontier[i][1]

            print "Custo de ", relationship_node, "<= ", frontier[i][0], " comparacao eh", relationship_cost, " < ", aux_cost, ": ", relationship_cost <= aux_cost
            
            if relationship_cost <= aux_cost:
                index = i
                print "Index atualizado para ", i
                break

        
        print "Add ", relationship_node, "em ", index
        frontier.insert(index, (relationship_node, relationship_cost))
        print"-"
        

def search(from_node, to_node):
    frontier = []
    frontier.append((from_node, from_node.estimate))

    current_node = None
    while(len(frontier) > 0):
        print frontier
        current_node = frontier.pop(0)[0]
        print "Current node: ", current_node
        print ""

        if(current_node is to_node):
            print ">>> Finish <<<"
            break
            
        add_relationships_node_of_current_node_to_frontier(frontier, current_node)
            

        
    
search(joao_pessoa, cajazeiras)
