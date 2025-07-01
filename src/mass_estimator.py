def estimate_dynamical_mass(sigma_v, radius_mpc):
    G = 4.302e-6  # (km/s)^2 Mpc / M_sun
    mass = (3 * sigma_v**2 * radius_mpc) / G
    return mass
