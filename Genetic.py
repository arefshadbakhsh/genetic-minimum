import random


def generate_random_number(start=0, end=100):
    return random.randint(start, end)


class Genetic(object):

    def __init__(self, f, pop_size=100):
        self.gen_produced = 0
        self.mutation_counter = 0
        self.func = f
        self.byte = 7
        self.pop_size = pop_size
        self.population = self.init_population()
        self.answers = []
        self.byte_counter = self.byte - 1

    def init_population(self):
        init = []
        for _ in range(self.pop_size):
            arr = []
            for i in range(self.byte):
                arr.append(generate_random_number(0, 1))
            init.append(arr)
        return init

    def fitness(self):
        fit_value = []
        for i in self.population:
            ch_value = self.binary_to_decimal(i)
            fit_value.append(ch_value)
        self.answers = [self.func(item) for item in fit_value]
        self.custom_sort()

    def custom_sort(self):
        for i in range(len(self.answers)):
            for j in range(len(self.answers)):
                if self.answers[i] < self.answers[j]:
                    self.answers[i], self.answers[j] = self.answers[j], self.answers[i]
                    self.population[i], self.population[j] = self.population[j], self.population[i]

    def binary_to_decimal(self, code):
        ch_value = 0
        for i in range(len(code) - 1, 0, -1):
            ch_value += code[i] * (2 ** (self.byte_counter - i))
        ch_value = -1 * ch_value if code[0] == 1 else ch_value
        return ch_value

    def select_parent(self, index):
        return self.population[index: index + 2]

    def crossover(self):
        next_gen = []
        x = 0
        while len(next_gen) < self.pop_size:
            # rand_a = generate_random_number(0, self.pop_size - 1)
            # rand_b = generate_random_number(0, self.pop_size - 1)
            # p1 = self.population[rand_a]
            # p2 = self.population[rand_b]
            parents = self.select_parent(x)
            p1 = parents[0]
            p2 = parents[1]
            change_point = generate_random_number(0, self.byte)
            p1_child = p1[0: change_point] + p2[change_point:]
            p2_child = p2[0: change_point] + p1[change_point:]
            next_gen.extend([p1, p2, p1_child, p2_child])
            x += 2
        self.gen_produced += 1
        self.population = next_gen

    def mutation(self):
        random_number = generate_random_number(0, self.pop_size - 1)
        if random_number == 35:
            rn1 = generate_random_number(0, self.pop_size - 1)
            rn2 = generate_random_number(0, self.byte_counter)
            self.mutation_counter += 1
            self.population[rn1][rn2] = 1 - self.population[rn1][rn2]
            self.answers[rn1] = self.func(self.binary_to_decimal(self.population[rn1]))

    def run(self):
        self.fitness()
        self.crossover()
        self.mutation()
