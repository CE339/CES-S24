from pyomo.environ import *
infinity = float('inf')

model = ConcreteModel()

# Factories
model.I = Set(initialize=["F_A","F_B"])
# Pollutants
model.J = Set(initialize=['P_1','P_2'])

# ci - Cost to process waste from factory
model.c    = Param(model.I, initialize={"F_A":15 , "F_B":10})
# rij - Rate of reduction in pollutant type if emission is treated at factory
model.r    = Param(model.I, model.J, initialize={("F_A",'P_1'):0.1, ("F_A",'P_2'):0.4,("F_B",'P_1'):0.2,("F_B",'P_2'):0.16})
# Lower and upper bound on processed waste
model.Wmin = Param(model.I, within=NonNegativeReals, default=0.0)

# Sj - State requirement to reduce pollutants
model.S = Param(model.J,initialize={'P_1':30, 'P_2':40})

# wi - Processed waste from Factory 
model.w = Var(model.I, within=NonNegativeReals)

# Minimize the cost to reduce pollutants
def cost_rule(model):
    return sum(model.c[i]*model.w[i] for i in model.I)
model.cost = Objective(rule=cost_rule)

# Satisfy the state's requeriments on pollutant reduction
def pollutant_rule(model, j):
    return sum(model.r[i,j]*model.w[i] for i in model.I) >= model.S[j]
model.pollutant = Constraint(model.J, rule=pollutant_rule)

# Limit the volume of the decision variables
def waste_rule_min(model, i):
    return model.w[i] >= model.Wmin[i]
model.waste = Constraint(model.I, rule=waste_rule_min)

#Optimizing and Printing Results
opt = SolverFactory('gurobi')
results = opt.solve(model).write()
print('\nDecision Variables')
print('Waste A = ', model.w['F_A']())
print('Waste B = ', model.w['F_B']())
print('Total Cost = ', model.cost())
