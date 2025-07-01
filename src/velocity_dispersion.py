import numpy as np

def compute_velocity_dispersion(galaxy_redshifts, cluster_redshift):
    c = 299792.458  # speed of light in km/s
    velocities = c * (np.array(galaxy_redshifts) - cluster_redshift) / (1 + cluster_redshift)
    return np.std(velocities, ddof=1)
