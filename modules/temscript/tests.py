#!/usr/bin/env python3

if __name__ == "__main__":
    import instrument
    from  enums import *
    import logging
    import pickle
    import matplotlib.pyplot as plt

    logging.basicConfig(level=logging.INFO)

    instrument = instrument.Instrument()
    # instrument.acquisition.addDetectorByName('DF4')
    # instrument.acquisition.stemDetectors.dwellTime(1e-7)
    # instrument.acquisition.stemDetectors.setFrameSize(AcqFrameSize.Full)
    # instrument.acquisition.stemDetectors.setMaxFrameSize(AcqMaxFrame.Full)
    instrument.illumination.stemMagnification(5343)

    print(instrument.acquisition.stemDetectors.dwellTime())

    #print(instrument.vacuum.runBufferCycle())
    instrument.projection.mode(ProjMode.Imaging.value)
    instrument.projection.lensProgram(ProjLensProg.Regular.value)

    print(instrument.gun.htValue(216230))
    #print(instrument.mode(InstrumentMode.TEM.value))
    #print(instrument.projection.normalize(ProjNormalization.All.value))
    #print(instrument.camera.mainScreenPosition(0))




    # plt.imshow(instrument.acquisition.acquireImages()[0])
    # plt.show()
