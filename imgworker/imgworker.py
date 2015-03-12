import numpy as np
iw = __import__('_ImgWorker')

def check_tgt(tgt, otype, oshape):
    assert tgt.dtype == otype, "tgt dtype is incorrect"
                               " {} vs {}".format(tgt.dtype, otype)
    assert tgt.shape == oshape, "tgt shape is incorrect"
                               " {} vs {}".format(tgt.shape, oshape)

def decode_list(jpglist, tgt, orig_size, crop_size,
                center=False, rgb=True, flip=False, nthreads=5):

    channels = 3 if rgb else 1
    out_shape = (len(jpglist), channels * crop_size * crop_size)

    if tgt is None:
        tgt = np.zeros(out_shape, dtype=np.uint8)
    else:
        check_tgt(tgt, np.uint8, out_shape)

    iw.decodeTransformListMT(jpglist=jpglist, tgt=tgt, orig_size=orig_size,
                             crop_size=crop_size, center=center, rgb=rgb,
                             flip=flip, nthreads=nthreads, calcmean=False)

    return tgt

def calc_batch_mean(jpglist, tgt, orig_size, rgb=True, nthreads=5):
    channels = 3 if rgb else 1
    out_shape = (orig_size, orig_size, channels)

    if tgt is None:
        tgt = np.zeros(out_shape, dtype=np.uint8)
    else:
        check_tgt(tgt, np.uint8, out_shape)

    iw.decodeTransformListMT(jpglist=jpglist, tgt=tgt, orig_size=orig_size,
                             crop_size=orig_size, center=True, rgb=rgb,
                             flip=False, nthreads=nthreads, calcmean=True)