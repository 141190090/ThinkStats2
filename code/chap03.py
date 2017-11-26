import thinkstats2

def PmfMean(pmf):
    mean =0
    for val, p in pmf.Items():
        mean += val*p
    return mean

def PmfVar(pmf):
    var = 0
    mean = PmfMean(pmf)
    for val, p in pmf.Items():
        var+=p*(val-mean)*(val-mean)

    return var

