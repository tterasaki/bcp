import numpy as np
import h5py
from sotodlib import core

def read_toast_h5(filename):
    f = h5py.File(filename, 'r')

    dets = np.array([v['name'] for v in f['instrument']['focalplane']], dtype='str')
    count = f['detdata']['signal'].shape[1]

    aman = core.AxisManager(
        core.LabelAxis('dets', dets),
        core.OffsetAxis('samps', count, 0),
    )

    aman.wrap_new('signal', ('dets', 'samps'), dtype='float32')
    aman.wrap_new('timestamps', ('samps', ), dtype='float64')

    bman = core.AxisManager(aman.samps.copy())
    bman.wrap('az', f['shared']['azimuth'], [(0, 'samps')])
    bman.wrap('el', f['shared']['elevation'], [(0, 'samps')])
    bman.wrap('roll', 0*bman.az, [(0, 'samps')])
    aman.wrap('boresight', bman)

    aman.timestamps[:] = f['shared']['times']
    aman.signal[:] = f['detdata']['signal']

    if 'hwp_angle' in f['shared']:
        aman.wrap('hwp_angle', f['shared']['hwp_angle'][...], [(0, 'samps')])

    aman.wrap('toast_focalplane', f['instrument']['focalplane'], [(0, 'dets')])

    return aman

def main():
    import sys
    loadfilepath = sys.argv[1]
    savefilepath = sys.argv[2]

    aman = read_toast_h5(loadfilepath)
    aman.save(savefilepath)
    return

if __name__ == '__main__':
    main()