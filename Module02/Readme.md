This module shows examples of concrete and abstract models using Pyomo
We are attempting to solve the following problem:

There are two factories on the Momus's River (A and B). Each emits two types of pollutants (1 and 2) into the river. If the waste from each factory is processed, the pollution in the river can be reduced
It costs $15 to process a ton of factory A waste, and each ton processed reduces the amount of pollutant 1 by 0.10 ton and the amount of pollutant 2 by 0.4 ton. It costs $10 to process a ton of factory B waste, and each ton processed will reduce the amount of pollutant 1 by 0.20 ton and the amount of pollutant 2 by 0.16 ton.

The state wants to reduce the amount of pollutant 1 in the river by at least 30 tons and of pollutant 2 in the river by at least 40 tons. Find the minimum cost of reducing pollution by the desired amounts
