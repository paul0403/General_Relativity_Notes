# General Relativity Notes
My notes on general relativity. 

My aim is for them to be in a story-telling tone, and to be more on the intuitive-understanding side of things.

The content is largely based on Profesor Leonard Susskind's [special relativity](https://www.youtube.com/watch?v=toGH5BdgRZ4&list=PLD9DDFBDC338226CA) and [general relativity](https://www.youtube.com/watch?v=SwhOffh0kEE&list=PLpGHT1n4-mAvcXwzOIz3dHnGZaQP1LEib) lectures in his amazing series [The Theoretical Minimum](https://theoreticalminimum.com/).

The content is also based on Sean Caroll's classic text on relativity [Spacetime and Geometry](https://www.amazon.ca/Spacetime-Geometry-Introduction-General-Relativity/dp/1108488390/ref=sr_1_1?crid=1B0MHN7C97QAH&keywords=spacetime+and+geometry+an+introduction+to+general+relativity&qid=1636895964&s=books&sprefix=spacetime+and+%2Cstripbooks%2C161&sr=1-1).

The `notes` directory contains all the notes. The `solutions` directory contains the solutions to the exercises that appear in the notes.

Below is the list of topics and their structure.

## 0. Prelude
- 0.0 Prelude 
- 0.5 The chain rule

## 1. Motivation
- 1.1 Motivation : losing track of time
- 1.2 Motivation : frame-invariant equations, and the Equivalence Principle
- 1.99 Motivation summary


## 2. Geometry 1: straight lines (and a little bit of curvature)
- 2.1 What is a vector; contravariant and covariant vectors
- 2.2 What is a tensor; the metric tensor
	- 2.2.1 An interlude on tensor products
- 2.3 Everything is locally flat
- 2.4 The covariant derivative

***The following is still in construction. The outline can change based on how it will actually go.***
    
- 2.5 The geodesic equation
	- 2.5.1 A slight interlude regarding parametrization: affine parametrization
	- 2.5.2 The geodesic equation only works for an affine parametrization
- 2.6 The Riemann curvature tensor
- 2.99 Flashcard on important geometry equations


## 3. Special relativity 1: particle kinematics (so four-vectors/velocities, Lorentz transforms, Minkowski metric)
- 3.1 The Lorentz Transform; The Minkowski Metric
	- 3.1.1 Quick results from the Lorentz Transform: time dilation, length contraction, velocity addition, the Doppler Effect
    - 3.1.2 Quick results regarding 4-velocities
- 3.2 Using the geodesic equation in Minkowski spacetime
- 3.3 The Equivalence Principle revisited: using the geodesic equation to derive the fictitious gravity in an accelerating frame


## 4. Geometry 2: straight lines again
- 4.1 Of course, a straight line is the shortest path between two points: the Euler-Lagrange equation
- 4.2 The free particle Lagrangian in Minkowski Spacetime; why it has a minus sign: the "Twin Paradox"
- 4.3 Applying the Euler-Lagrange equation to the Minkowski free particle Lagrangian; Lagrangians don't require an affine parametrization!
- 4.9 The four principles of Laws Of Physics
- 4.99 Lagrangian of a particle in a scalar field in Minkowski spacetime, and its Newtonian limit ("KE-PE")


## 5. Lagrangian tricks

Almost all courses in advanced classical mechanics start with telling you "there's this thing called the Euler-Lagrange equation, and the Lagrangian for a system is KE-PE". From there on we can apply this method to most classical systems. I will explicitly do a couple of examples just for illustrating the power of Lagrangian mechanics, but they are not necessary for general relativity. Skip it if you wish. 

- 5.0 Examples of classical Lagrangian: Newton's second law, harmonic oscillator, inclined wedge sliding on a plane, the double pendulum

From here on it's necessary. 

- 5.1 Symmetry and conserved quantities
- 5.2 Conservation of energy: the Hamiltonian


## 6. Special relativity 2: particle dynamics (so four-momentum, energy)




## 7. Lagrangian for fields
- 7.1 The Euler-Lagrange equation for fields
- 7.2 The free field Lagrangian in Minkowski spacetime; the wave equation
- 7.3 Particle-field interactions: the Poisson equation


## 8. Special relativity 3: electromagnetism
- 8.1 The magnetic vector potential and gauge invariance
- 8.2 The Lorentz Force Law with a classical Lagrangian
- 8.3 The Lorentz Force Law with a relativistic Lagrangian
- 8.4 What is A0? The electromagnetic field strength tensor
- 8.5 The electromagnetic source 4-vector
- 8.6 Maxwell's equations


## 9. Lagrangian for fields: field momentum and field energy 


## 10. The Schwarzschild metric (so black holes)
- 10.0 A reminder about the equivalence principle
- 10.1 Postulating the Schwarzschild metric
- 10.2 Watching your friend falling into a black hole
- 10.3 The photon sphere
- 10.4 Kruskal coordinates
- 10.5 Penrose diagrams


## 11. The Einstein field equations
- 11.0 A reminder about the Riemann curvature tensor
- 11.1 The Einstein field equation
- 11.2 The Einstein field equation from the Einstein-Hilbert action
- 11.99 Solving the Einstein field equations for the Schwarzschild metric



# Computational Files
A list of computational files are available to compute stuff, or to explicitly illustrate some of the phenomena we encounter.

- connection.py: a python script calculating the connection coefficients from a given metric
- stuck_on_horizon.py: a python script showing that it takes an infinite amount of coordinate time (or lab time) for an object to reach the horizon
