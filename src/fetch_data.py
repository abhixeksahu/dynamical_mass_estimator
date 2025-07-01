from astroquery.sdss import SDSS
from astropy.io import fits
from astropy import coordinates as coords
from astropy import units as u
import numpy as np
import time

def extract_ra_dec_from_fits(filepath):
    """
    Extract RA and Dec from a FITS catalog file (table HDU).
    """
    with fits.open(filepath) as hdul:
        # Check HDU[1], else fallback to HDU[0]
        if len(hdul) > 1 and hdul[1].data is not None:
            data = hdul[1].data
        else:
            data = hdul[0].data

        # Try to find RA and Dec columns
        columns = [col.lower() for col in data.names]
        if 'ra' in columns and 'dec' in columns:
            ra = data['RA'] if 'RA' in data.names else data['ra']
            dec = data['DEC'] if 'DEC' in data.names else data['dec']
        else:
            raise ValueError("RA and DEC columns not found in FITS file")

    return ra, dec

def fetch_redshifts_from_radec(ra_list, dec_list, search_radius_arcmin=2.0, batch_size=50):
    redshifts = []
    total = len(ra_list)

    for i in range(0, total, batch_size):
        batch_ra = ra_list[i:i+batch_size]
        batch_dec = dec_list[i:i+batch_size]
        
        # Prepare SkyCoord array for batch query
        coords_batch = coords.SkyCoord(ra=batch_ra, dec=batch_dec, unit=(u.deg, u.deg))

        try:
            # Query SDSS for all coords in this batch
            result = SDSS.query_region(coords_batch, radius=search_radius_arcmin * u.arcmin, spectro=True)
            
            if result is not None and 'z' in result.colnames:
                redshifts.extend(result['z'].data.tolist())
        except Exception as e:
            print(f"Batch {i//batch_size + 1} query failed: {e}")

        # Be kind to SDSS servers
        time.sleep(1)  # 1 second delay between batches

    return redshifts

def clean_redshifts(z_array):
    z_array = np.array(z_array)
    clean_z = z_array[(z_array > 0) & (z_array < 0.5)]
    return clean_z
