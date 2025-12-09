def split_before_uppercases(formula):
    split_formula = []
    start = 0
    if not formula:
        return []

    for i in range(len(formula)):
        if formula[i].isupper() and i > 0:
            split_formula.append(formula[start:i])
            start = i

    split_formula.append(formula[start:])
    return split_formula

def split_at_digit(formula):
    if not formula:
        return "", 1

    digit_location = -1

    for i in range(len(formula)):
        if formula[i].isdigit():
            digit_location = i
            break

    if digit_location == -1:
        return formula, 1
    else:

        a1= formula[:digit_location]
        a2 = formula[digit_location:]
        return a1, int(a2)

def count_atoms_in_molecule(molecular_formula):
    at = {}

    part = split_before_uppercases(molecular_formula)

    for p in part:
        atom,num = split_at_digit(p)
        
        if atom in at:
            at[atom] += num
        else:
            at[atom] = num

    return at



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
