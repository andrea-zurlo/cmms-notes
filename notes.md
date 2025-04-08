# Notes

## Tricks of the trade

### 1. Initial positions
For small and simple systems the atoms or molecules can be set on a lattice, this is enough to guarantee small initial forces. For more complex systems, such as proteins and polymers, it's convenient to set up a random initial configuration. In this case, in order to avoid too high forces which could cause numerical errors it is needed to apply an energy minimization before starting the MD simulation.

### 2. Boundary conditions

### 3. Short-range interactions

We call *short-range* interaction a potential that drops down to zero faster than $1/r^3$

$$ \textrm{short-range}\qquad \Leftrightarrow\qquad U(r)\propto \frac{1}{r^\alpha}\quad \alpha>3 $$

For instance the London dispersion ($\alpha=6$) and the Pauli repulsion ($\alpha=12$) are short-range, hence the Lennard-Jones potential is considered a short-range interaction. On the other hand 1D electric dipole interaction ($\alpha=3$) and electrostatic interaction ($\alpha=1$) are considered long-range.

In MD, when we deal with short-range interaction we take advantange of the fact that the main contribution to the potential energy of a particle comes from the neighbors within a threshold distance.

minimum image convention
potential cutoff and tail correction

### 4. Neighbor list

In MD simulations, most calculations involve determining the forces between pairs of interacting atoms. For example, the Lennard-Jones potential or Coulombic interactions depend on the positions of atom pairs. However, directly computing interactions between all pairs of atoms in a system (i.e., a $O(N^2)$  problem, where $N$ is the number of atoms) would be prohibitively expensive, especially for large systems.

The neighbor list helps by only considering atoms that are close enough to interact. Atoms that are far apart can be safely ignored, as their interactions are negligible (especially for short-range potentials like the Lennard-Jones potential).

Thus, the neighbor list:
1. Reduces the Number of Interactions to Compute. By storing only the atoms within the cutoff distance, the neighbor list allows the simulation to ignore far-away atoms, drastically reducing the number of interactions that need to be computed. For instance, in a system with $N = 100$  atoms, a brute-force approach would require computing interactions for $N^2 = 10,000$ pairs. With a neighbor list, only a small subset of these interactions (based on proximity) are considered, which could significantly reduce the computation time.
2. Increases Computational Efficiency. The neighbor list allows the MD simulation to focus on only the relevant pairs of atoms, improving the overall performance and enabling simulations of larger systems or longer timescales.
3. Optimizes Memory Usage. Instead of storing interactions between every pair of atoms (which would require a huge amount of memory), the neighbor list stores only a subset of pairs, optimizing memory usage and reducing storage requirements.

- List of Nearby Atoms: For each atom in the simulation, the neighbor list stores the list of atoms that are within a certain cutoff distance, known as the cutoff radius.
- Cutoff Distance: The cutoff distance defines the maximum range within which atoms interact. For example, if the cutoff distance for a potential is 2.5 Å, then only atoms within this distance will be considered for interaction.
- Neighbor List Update: The neighbor list is usually updated periodically (e.g., every few timesteps) because atoms move during the simulation. The update interval is a trade-off between accuracy and computational cost—frequent updates are more accurate but more expensive, while less frequent updates are faster but may miss some interactions. This balance needs to be carefully tuned based on the specifics of the simulation and system size.
- Skin Distance: To avoid having to update the list too often, a skin distance is often used. This is a buffer zone beyond the cutoff distance that helps ensure the list remains accurate between updates.

In LAMMPS, the neighbor list is implemented in a highly optimized manner. The neighbor command is used to control the parameters related to the neighbor list, such as the cutoff distance and the skin distance:
```
neighbor 2.0 bin
neigh_modify every 20 delay 0 check yes
```

- `neighbor 2.0 bin` specifies that the cutoff distance for neighbors is 2.0 units, and the bin method is used for spatial binning (which is an efficient way of finding neighbors).
- `neigh_modify` controls how often the list is updated (every 20 means the list is updated every 20 timesteps), how much delay is allowed between updates, and whether to check for atoms that have moved out of range.


### 24-03-25

- `LJ.data` file, the last 3 cols specify which replica the atoms belongs
the set of coordinates can be given by structure (FCC, BCC, etc.) or by external 'data' files.
- fix npt: iso= the pressure action is isotropical, i.e in all directions;
- CSVR = best thermostat;
- python can read dcd and xtc;
- the `compute` command can be used to compute custom quantities on the fly within lammps; for example ACF
- in order to compute ACF we have to take care

### 27-03-25

threejmm compute klebsh-gordan coefficients
calcbop compute system order parameter

the bond order parameter, differently from g(r), gives information on the local symmetry so it is more useful for small system where there can't be no long-range order.