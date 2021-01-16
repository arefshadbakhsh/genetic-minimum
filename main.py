from Genetic import Genetic

# my_func = lambda x: (x ** 2) + 10 * x + 1
my_func = lambda x: (x ** 2)
gen = Genetic(my_func)
for i in range(1000):
    gen.run()
    print('created gen is: ', gen.gen_produced)

print('Number of times mutated', gen.mutation_counter)
print("best answer is :")
print(gen.answers[0])
print("in binary mode x is ........", gen.population[0])
print('in decimal mode x is .......', gen.binary_to_decimal(gen.population[0]))
