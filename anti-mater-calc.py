import math

c = 299792458 # speed of light in m/s
gram_to_kg = 0.001 # conversion factor from grams to kilograms
mass_energy_equivalence = c**2 # E = mc^2
tnt_energy_equivalence = 4184000000 # energy released by 1 kg of TNT in joules
hiroshima_bomb_energy = 63000000000 # energy released by the atomic bomb dropped on Hiroshima in joules
blast_energy = 0.5 * tnt_energy_equivalence # assume 50% of energy is released as blast energy
blast_radius = 0.43 * (blast_energy / 1000000)**0.33 # approximate blast radius in kilometers based on the Taylor-Sedov scaling law

grams_of_antimatter = float(input("Enter the mass of antimatter in grams: "))

# convert the mass of antimatter from grams to kilograms
mass_of_antimatter = grams_of_antimatter * gram_to_kg

# calculate the energy released by annihilating the given mass of antimatter
energy = mass_of_antimatter * mass_energy_equivalence

# convert the energy to equivalent TNT energy
tnt_energy = energy / tnt_energy_equivalence

# calculate the percentage of energy released by the Hiroshima bomb
percentage_of_hiroshima = energy / hiroshima_bomb_energy * 100

# calculate the approximate area of effect of the explosion
blast_area = math.pi * (blast_radius**2)


print(grams_of_antimatter, "grams of antimatter is:", round(tnt_energy, 2), "kilograms of TNT")
print(round(percentage_of_hiroshima, 2), "% of the Hiroshima bomb.")
print("Assuming the explosion occurs in an open desert with no buildings\n",
      "approximate blast radius is", round(blast_radius), "kilometers\n",
      "The approximate area of effect is", round(blast_area), "square kilometers.")
