# Dynamical Mass Estimator (Real Data Edition)

Estimate the dynamical mass of a galaxy cluster using:

-   FITS files containing RA/Dec from infrared survey data
-   Redshift data fetched from SDSS via Astroquery

## Usage

```bash
python main.py
```

## Folder Structure

```
dynamical_mass_estimator/
├── data/
│   ├── Skyserver_SQL7_1_2025 2_42_38 PM.fits
│   └── sample_galaxies.csv               # Backup redshift data
├── src/
│   ├── fetch_data.py                     # Extract RA/Dec, query SDSS for redshifts
│   ├── velocity_dispersion.py            # Compute velocity dispersion
│   └── mass_estimator.py                 # Estimate cluster mass
├── main.py                               # Pipeline entry point
├── requirements.txt
└── README.md
```
