# Dynamical Mass Estimator (Real Data Edition)

Estimate the dynamical mass of a galaxy cluster using:
- FITS files containing RA/Dec from infrared survey data
- Redshift data fetched from SDSS via Astroquery

## Usage
```bash
python main.py
```

## Folder Structure
```
dynamical_mass_estimator/
├── data/
│   ├── qKHJ_asky_971031n0960197.fits     # Infrared catalog with RA/Dec
│   └── sample_galaxies.csv               # Backup redshift data
├── src/
│   ├── fetch_data.py                     # Extract RA/Dec, query SDSS for redshifts
│   ├── velocity_dispersion.py            # Compute velocity dispersion
│   ├── mass_estimator.py                 # Estimate cluster mass
│   └── utils.py                          # Helper tools
├── main.py                               # Pipeline entry point
├── requirements.txt
└── README.md
```
