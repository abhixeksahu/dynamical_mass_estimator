from src.fetch_data import extract_ra_dec_from_fits, fetch_redshifts_from_radec, clean_redshifts
from src.velocity_dispersion import compute_velocity_dispersion
from src.mass_estimator import estimate_dynamical_mass

filepath = "data/Skyserver_SQL7_1_2025 2_42_38 PM.fits"

print(f"Processing FITS file: {filepath}")

ra_list, dec_list = extract_ra_dec_from_fits(filepath)
print(f"Extracted {len(ra_list)} RA/DEC pairs from the FITS file.")
raw_redshifts = fetch_redshifts_from_radec(ra_list, dec_list, search_radius_arcmin=2.0)
print(f"Starting data cleaning... Found {len(raw_redshifts)} raw redshifts.")
clean_z = clean_redshifts(raw_redshifts)
print(f"Data cleaning complete. Found {len(clean_z)} valid redshifts after cleaning.")

print(f"Number of galaxy redshifts used: {len(clean_z)}")
if len(clean_z) < 5:
    print("Not enough redshifts to compute velocity dispersion.")
else:
    cluster_z = clean_z.mean()
    sigma_v = compute_velocity_dispersion(clean_z, cluster_z)
    print(f"Velocity dispersion: {sigma_v:.2f} km/s")

    cluster_radius = 1.5  # in Mpc, tweak as needed
    mass = estimate_dynamical_mass(sigma_v, cluster_radius)
    print(f"Estimated dynamical mass: {mass:.2e} M☉")
