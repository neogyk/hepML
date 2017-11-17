from dfConvert import convertTree
from pandasPlotting.Plotter import Plotter

makePlots=True
exceptions=['selJetB']

if __name__=='__main__':

    print "Loading DataFrames" 
    signalFile = '/nfs/dust/cms/group/susy-desy/marco/training_sample_new/top_sample_0.root'
    bkgdFile = '/nfs/dust/cms/group/susy-desy/marco/training_sample_new/stop_sample_0.root'

    signal = convertTree(signalFile,signal=True,passFilePath=True,tlVectors = ['selJet','sel_lep'])
    bkgd = convertTree(bkgdFile,signal=False,passFilePath=True,tlVectors = ['selJet','sel_lep'])

    print "Making plots" 
    if makePlots:
        signalPlotter = Plotter(signal,'testPlots/signal',exceptions=exceptions)
        bkgdPlotter = Plotter(bkgd,'testPlots/bkgd',exceptions=exceptions)

        signalPlotter.plotAllHists1D(withErrors=True)
        bkgdPlotter.plotAllHists1D(withErrors=True)
        pass

    #Now add the relevant variables to the DFs (make gram matrix)
    pass

    #Now carry out machine learning (with some algo specific diagnostics)
    pass

    #and carry out a diagnostic of the results
    pass